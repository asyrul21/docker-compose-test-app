var express = require('express')

app = express()

app.use(express.static('./dist/angular-frontend'));

app.get('/*', function (req, res) {
    res.sendFile('index.html', { root: 'dist/angular-frontend/' }
    );
});

app.listen(process.env.PORT || 4200, function () {
    console.log('Angular server is listening...');
});