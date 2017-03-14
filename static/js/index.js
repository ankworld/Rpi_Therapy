var data;

function onload() {
    console.log()
}

function search() {
    var data = document.getElementsByClassName('search_field')[0].value
    console.log(data);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200) {
                console.log(xmlhttp.responseText)
            } else if (xmlhttp.status == 400) {
                alert('There was an error 400')
            } else {
                alert('something else other than 200 was returned')
            }
        }
    };
    xmlhttp.open("POST", "/select_profile/search")
    xmlhttp.send("key=data")
}

window.onload = onload()
