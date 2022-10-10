const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

var osUtils = require('os-utils');
var sec = osUtils.sysUptime();
var min = sec / 60;
var hour = min / 60;

sec = Math.floor(sec);
min = Math.floor(min);
hour = Math.floor(hour);

hour = hour % 60;
min = min % 60;
sec = sec % 60; 

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${hour + "Hour(s)" + min + "minute(s)" + sec + "second(s)"} </p>
        <p>Total Memory: ${osUtils.totalmem()}</p>
        <p>Free Memory: ${osUtils.freemem()} </p>
        <p>Number of CPUs: ${osUtils.cpuCount()}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");