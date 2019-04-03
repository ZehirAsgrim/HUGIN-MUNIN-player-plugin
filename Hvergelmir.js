const child = require('child_process').exec;
var cmdString = '';
for(i=1; i<40; i++) {
    cmdString+='sudo -u mpd amixer -D equal1 cset numid='+i+' '+50+'; ';
}
child(cmdString, (err, stdout, stderr) => {
    console.log(cmdString);
});
