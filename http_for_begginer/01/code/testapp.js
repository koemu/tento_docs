// node.js サンプルページ
// HTTPの挙動を知るために利用します
// required: Node.js 0.6 or later, express@3.0
 
var express = require('express');
var app = express();
 
app.get('/', function(req, res){
    res.set('Content-Type', 'text/plain');
    res.send('Hello World\n');
});
 
app.listen(8888);
