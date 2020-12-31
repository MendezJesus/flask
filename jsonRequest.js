// Simulate Firebase Server Request to docker container

var FormData = require('form-data');
var fs = require('fs');


// formData.append('username', myFileInput.files[0], 'rubicCube.jpg');

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

const Http = new XMLHttpRequest();
// const url='https://jsonplaceholder.typicode.com/posts';
const url = 'http://0.0.0.0:8080/classifier';
Http.open("POST", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
