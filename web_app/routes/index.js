var express = require('express');
var router = express.Router();
var path = require('path');
var fs = require("fs");


var results = path.normalize(__dirname + '/results.json');


// Rendering HTML
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express Music' });
});

router.get('/home', function(req, res, next){
	res.render("home");
});

router.get('/more', function(req, res, next) {
  res.render('more', { title: 'Express Music' });
});

router.get('/suggestions', function(req, res, next) {
  res.render('suggestions', { title: 'Express Music' });
});

// API rendering

router.get('/results', function(req, res, next) {
	var file = JSON.parse(fs.readFileSync('routes/results.json', 'utf8'));
	var fallback = "../songs/Tor Miller_Carter and Cash.mp3";
	for (var index in file.songs){
		var cluster = file.songs[index];
		for (var j in cluster){
			if(cluster[j].indexOf(".mp3") < 0){
				cluster[j] = fallback;
			}
		}
	}
	res.send(file);
});

module.exports = router;