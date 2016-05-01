var express = require('express');
var app = express();
var path = require('path');
app.get('/results', function(req, res){
	res.sendFile(path.normalize(__dirname+'/results.json'));
});

app.listen(8000, function(){
	console.log("running on port 8000");
})