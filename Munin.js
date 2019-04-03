http = require('http');
fpexist = require('fs');
fpwrite = require('fs');
fpgwrite = require('fs');
fpgenre = require('fs');
fpgexist = require('fs');
server = http.createServer(function(req, res)
{
    if (req.method == 'POST')
    {
        var body = '';
        const child = require('child_process').exec;
        req.on('data', function(data)
        {
            body += data;
            console.log('[MUNIN] Receiving from HUGIN...');
            var userdata = JSON.parse(body);
            var filename = userdata.userID+'@'+userdata.songname;
            var cmdString = 'py Odin.py '+userdata.select+' '+filename;
            fpexist.stat('eq_'+filename+'.txt', function(err, stat) {
                if(err) {   //eqfile does not exist
                    console.log(body);
                    cmdString = 'py Odin.py '+2+' '+filename;
                    child(cmdString, (err, stdout, stderr) => {
                        console.log("[MUNIN] Creating new userdata...");
                        setTimeout(function() {
                        var eq = fpexist.readFileSync('eq_'+filename+'.txt', 'utf8');
                        res.writeHead(200, {'Access-Control-Allow-Origin' : '*'});
                        res.end(eq);
                        fpwrite.writeFileSync('log_'+filename+'.txt', body+'\r\n'+eq+'\r\n\r\n', 'utf8');
                        }, 1000);
                    });
                }
                else {  //eqfile exist
                    fpgenre.stat('genre_'+filename+'.txt', function(err, stat) {
                        if(err) {   //without genre analysis
                            console.log(body);
                            cmdString = 'py Odin.py '+userdata.select+' '+filename;
                            child(cmdString, (err, stdout, stderr) => {
                                console.log("[ODIN] Calculating new EQ...");
                                var eq = fpexist.readFileSync('eq_'+filename+'.txt', 'utf8');
                                res.writeHead(200, {'Access-Control-Allow-Origin' : '*'});
                                res.end(eq);
                                fpwrite.appendFileSync('log_'+filename+'.txt', body+'\r\n'+eq+'\r\n\r\n', 'utf8');
                            });
                        }
                        else {  //with genre analysis
                            var readgenre = fpgenre.readFileSync('genre_'+filename+'.txt', 'utf8');
                            var genre = JSON.parse(readgenre);
                            Object.assign(userdata, genre);
                            var body2 = JSON.stringify(userdata);
                            console.log(body2);
                            var gfilename = userdata.userID+'@'+userdata.genre;
                            console.log(gfilename);
                            fpgexist.stat('eq_'+gfilename+'.txt', function(err, stat) {
                                if(err) {   //genre eqfile not exist
                                    cmdString = 'py Odin.py '+2+' '+gfilename;
                                    child(cmdString, (err, stdout, stderr) => {
                                        console.log("[MUNIN] Creating new userdata...");
                                        setTimeout(function() {
                                        var eq = fpgexist.readFileSync('eq_'+gfilename+'.txt', 'utf8');
                                        res.writeHead(200, {'Access-Control-Allow-Origin' : '*'});
                                        res.end(eq);
                                        fpwrite.appendFileSync('log_'+filename+'.txt', body2+'\r\n'+eq+'\r\n\r\n', 'utf8');
                                        fpgwrite.writeFileSync('log_'+gfilename+'.txt', body2+'\r\n'+eq+'\r\n\r\n', 'utf8');
                                    }, 1000);
                                    });
                                }
                                else {  //genre eqfile exist
                                    cmdString = 'py Odin.py '+userdata.select+' '+gfilename;
                                    child(cmdString, (err, stdout, stderr) => {
                                        console.log("[ODIN] Calculating new EQ...");
                                        var eq = fpgexist.readFileSync('eq_'+gfilename+'.txt', 'utf8');
                                        res.writeHead(200, {'Access-Control-Allow-Origin' : '*'});
                                        res.end(eq);
                                        fpgwrite.appendFileSync('log_'+gfilename+'.txt', body2+'\r\n'+eq+'\r\n\r\n', 'utf8');
                                        fpwrite.appendFileSync('log_'+filename+'.txt', body2+'\r\n'+eq+'\r\n\r\n', 'utf8');
                                    });
                                }
                            });
                        }
                    });
                }
            });
        });
        req.on('error', function () {
            console.log('<error> ODIN was not listening to you =[');
        });
        res.writeHead(200, {'Content-Type': 'text/html'});
    }
});
port = 2720;
server.listen(port);
console.log('[MUNIN] Listening at Asgard : ' + port);
