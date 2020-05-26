var express = require('express');
var router = express.Router();
const axios = require('axios');

// yet to be changed when using docker compose
port = 80
var baseUri = 'http://spacy-vector-api/GetVector/?sentence='

// Get All questions
router.get('/', function (req, res, next) {
    var params = req.query;
    var word = params.word
    var uri = baseUri + word

    if (word) {
        axios.get(uri)
            .then(response => {
                data = response.data
                result = {
                    'vector': data.vector
                }
                res.json(result)
            })
            .catch(error => {
                console.log('ERROR MAKING REQUEST');
                console.log(error);
            });
    }
    else {
        res.json({ 'error': 'Invalid parameter.' })
    }
});

// insert questions
router.post('/', function (req, res, next) {
    var params = req.body
    word = params.word

    result = {
        'vector': 'This feature is yet to be implemented!'
    }

    res.json(result)
});

module.exports = router;