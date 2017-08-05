var every = require('every-moment');
var express = require('express');
var app = express();
 
 
 var timer = every(15, 'minutes', function() {
	  console.log("enter");
    var python = require('child_process').spawn(
 'python', ["pr.py"]
 );});
 
app.use(express.static('views'));

var phpnode = require('php-node')({bin:"E:\\xampp1\\php\\php.exe"});
app.engine('php', phpnode);
app.set('view engine', 'php');


app.get('/', function(req, res, next) {
    res.render('index.php');
});

app.listen(1337);
 
