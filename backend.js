var express = require('express');
var bodyParser = require('body-parser');
require('dotenv').config()
const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;

var dbo;
var userPassword = process.env.userPassword;
var mongoHost = process.env.mongoHost;

var apiBackend = function(){
	/*
	 * Web REST API backend setup.
	 */
	var app = express();
	var jsonParser = bodyParser.json()

	app.get('/note', function(req, res) {
		dbo.collection('notes').find({}).toArray(function(err, docs) {
		    if(err) { console.error(err) }
		    res.send(JSON.stringify(docs));
		});
	});

	app.put('/note', jsonParser, function (req, res) {
		var contentTxt = JSON.stringify(req.body.content);
		console.log(contentTxt);
		if (contentTxt && contentTxt.length > 0){
			dbo.collection("notes").insertOne({'content': req.body.content, 'time': new Date()}, async (err, rslt) => {
				if (err) throw err;
				console.log(rslt);
			});
		}
		res.send('New Note: ' + jsonBody);
	});

	app.delete('/note', jsonParser, function(req, res) {
		const _id = mongodb.ObjectId(req.body._id)
		dbo.collection('notes').deleteOne({'_id': _id}, function(err, docs) {
		    if(err) { console.error(err) }
			console.log('Remove: ' + req.body._id);
		    res.send({'state': 'ok'});
		});
	});

	app.listen(3000, function () {
		console.log('NotesTool app listening on port 3000!');
	});

}

MongoClient.connect('mongodb://'+userPassword+'@'+mongoHost,  { useNewUrlParser: true, useUnifiedTopology: true }, function(err, db) {
    if (err) throw err;
    dbo = db.db("notes");
	apiBackend(dbo);
});







