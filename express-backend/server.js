// npm install express body - parser compression  ejs helmet axios cors--save
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var compression = require('compression');
var helmet = require('helmet');

var index = require('./routes/index');
var vector = require('./routes/vector.js');

var app = express();

// View Engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

//Compress all routes
app.use(compression());
app.use(helmet());
// Set Static folder
app.use(express.static(path.join(__dirname, 'client')));

// Body parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// CORS
const cors = require('cors')
app.use(cors())

app.use('/', index);
app.use('/vectorfor', vector);

const port = process.env.PORT || 3000;
app.listen(port, function () {
    console.log('Docker Compose Server started on port ' + port);
});