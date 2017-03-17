/* eslint-disable no-unused-vars */

function handleKeyPress (e) {
  var key = e.keyCode || e.which
  if (key === 13) {
    search()
  }
}

function search () {
  let data = document.getElementsByClassName('search_field')[0].value
  console.log(data)
  const xmlhttp = new XMLHttpRequest()
  xmlhttp.onreadystatechange = () => {
    if (xmlhttp.readyState === XMLHttpRequest.DONE) {
      if (xmlhttp.status === 200) {
        console.log(xmlhttp.responseText)
      } else if (xmlhttp.status === 400) {
        alert('There was an error 400')
      } else {
        alert('something else other than 200 was returned')
      }
    }
  }
  xmlhttp.open('POST', '/list_profile')
  xmlhttp.send('key=data')
}

function active (e) {
  let selectProfile = e.path[1].getElementsByTagName('section')[0].getElementsByTagName('h1')[0].innerHTML
  // console.log(selectProfile)
  const xmlhttp = new XMLHttpRequest()
  xmlhttp.onreadystatechange = () => {
    if (xmlhttp.readyState === XMLHttpRequest.DONE) {
      if (xmlhttp.status === 200) {
        console.log(xmlhttp.responseText)
      } else if (xmlhttp.status === 400) {
        alert('There was an error 400')
      } else {
        alert('something else other than 200 was returned')
      }
    }
  }
  xmlhttp.open('POST', '/active')
  xmlhttp.send(selectProfile)
}
