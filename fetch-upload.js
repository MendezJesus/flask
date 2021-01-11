//fetch using a Request and a Headers objects
// uploading an image along with other POST data
//using jsonplaceholder for the data

const url = 'http://0.0.0.0:8080/classifier';

document.addEventListener('DOMContentLoaded', init);

function init(){
    document.getElementById('btnSubmit').addEventListener('click', upload);
}

function upload(ev){
    ev.preventDefault();    //stop the form submitting

    //create any headers we want
    // let h = new Headers();
    // h.append('Accept', 'application/json'); //what we expect back
    //bundle the files and data we want to send to the server
    let fd = new FormData();
    fd.append('user-id', document.getElementById('user_id').value);

    let myFile = document.getElementById('input_image').files[0];
    fd.append('test_image', myFile, "test_image.jpg");

    let req = new Request(url, {
        method: 'POST',
        // headers: h,
        body: fd
    });


    fetch(req)
    .then(response => response.json())
    .then(json => {
      console.log(json);
      document.getElementById('output').innerHTML = JSON.stringify(json)
    })
    .catch( (err) =>{
      console.log('ERROR:', err.message);
    });
}
