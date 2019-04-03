http = require('http');
http2 = require('http');
fp = require('fs');
server = http.createServer(function(req, res)
{
    if (req.method == 'POST')
    {
        const child = require('child_process').exec;
		const getSongname = 'mpc current | sudo tee \"mpc.txt\"; mpc | grep -n \"[0-9]*:[0-9]*/[0-9]*:[0-9*]\" | cut -d \' \' -f 5 | sudo tee -a \"mpc.txt\"';
        //mpc | grep -n \"([0-9]*%)\" | cut -d \'(\' -f 2 | cut -d \')\' -f 1
        //mpc | grep -n \"[0-9]*:[0-9]*/[0-9]*:[0-9*]\" | cut -d \' \' -f 5
        const clearEq = 'sudo node Hvergelmir.js'
        req.on('data', function(data)
        {
            var body = '';
            var name = '';
            var time = '';
            body += data;
            var obj = JSON.parse(body);
            if(obj.select == 2) {
                child(clearEq, (err, stdout, stderr) => {
                    //console.log(clearEq);
                    console.log('[HVERGELMIR] Refreshing EQ...');
                });
            }
            else {
    			child(getSongname, (err, stdout, stderr) => {
                    console.log('[HUGIN] Getting info from Midgard...');
    				//console.log(getSongname);
                    var now = fp.readFileSync('mpc.txt', 'utf8');
                    now = now.split('\n');
                    name += now[0];
                    if(name.length != 0) {
                        name = name.replace(' - ', '-');
                        name = name.replace(/\s+/g, '_');
                        name = name.replace('.mp3', '');
                        name = name.replace('.m4a', '');
                        name = name.replace('.wav', '');
                        name = name.split('/');
                        name = name[name.length-1];
                        console.log('[Now Playing] '+name);
                        time += now[1];
                        console.log('[Time] '+time);
                        var info = {
                            userID : 'zehir',
                            songname : name,
                            playtime : time,
                        }
                        Object.assign(info, obj);
                        var userdata = JSON.stringify(info);
                        var options = {
                            hostname: '192.168.211.5',
                            port: 2720,
                            method: 'POST',
                            headers: {'Content-Type': 'text/html'}
                        };
                        var req2 = http2.request(options, function (res2)
                        {
                            var body2 = '';
                            res2.setEncoding('utf8');
                            res2.on('data', function (data2) {
                                body2 += data2;
                                var eq = JSON.parse(body2);
                                var cmdString = "";
                                var count = 0;
                                Object.keys(eq).reduce(function(prev, name) {
                                    cmdString+='sudo -u mpd amixer -D equal1 cset numid='+count+' '+(50 + eq[name]*4)+'; ';
                                    count++;
                                }, 0);
                                child(cmdString, (err, stdout, stderr) => {
                                    console.log('[ODIN] Changing EQ...');
                                    //console.log(cmdString);
                                });
                            });
                        });
                        req2.on('error', function () {
                            console.log('<error> MUNIN flew away =[');
                        });
                        req2.write(userdata);
                        req2.end();
                    }
    			});
            }
        });
        req.on('error', function () {
            console.log('<error> HUGIN flew away =[');
        });
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.writeHead(200, {'Access-Control-Allow-Origin' : '*'});
        res.end("[HUGIN] Received.");
    }
});
port = 6140;
server.listen(port);
console.log('[HUGIN] Listening at Midgard : ' + port);
