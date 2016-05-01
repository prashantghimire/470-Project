var express = require('express');
var router = express.Router();
var path = require('path');


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

// API rendering

router.get('/results', function(req, res, next) {
	res.sendFile(results);
});

module.exports = router;