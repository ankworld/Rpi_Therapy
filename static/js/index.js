/* eslint-disable no-unused-vars */

function handleKeyPress(e) {
    var key = e.keyCode || e.which
    if (key === 13) {
        search()
    }
}

function search() {
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

function active(objButton) {
    let selectProfile = objButton.value
    console.log(selectProfile)
    // console.log(selectProfile)
    const xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {
            if (xmlhttp.status === 200) {
                console.log(xmlhttp.responseText)
                window.location = xmlhttp.responseText
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

function remove(objButton) {
    let selectProfile = objButton.value
    console.log(selectProfile)
    // console.log(selectProfile)
    const xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {
            if (xmlhttp.status === 200) {
                console.log(xmlhttp.responseText)
                window.location = xmlhttp.responseText
            } else if (xmlhttp.status === 400) {
                alert('There was an error 400')
            } else {
                alert('something else other than 200 was returned')
            }
        }
    }
    xmlhttp.open('POST', '/remove_profile')
    xmlhttp.send(selectProfile)
}

function shutdown() {
    var r = confirm('Press a button')
    if (r === true) {
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
        xmlhttp.open('POST', '/shutdown')
        xmlhttp.send()
    }
}

var lastPercent
var lastActive

function updateProcess() {
    const xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {
            if (xmlhttp.status === 200) {
                console.log(xmlhttp.responseText)
                let item = JSON.parse(xmlhttp.responseText)
                let percent = item.success
                let active = item.active
                if (lastActive != active) {
                    if (active == "0") {
                        document.getElementsByClassName('dash_section')[0].innerHTML = `<h1 id="idle">ว่าง</h1>`
                    } else {
                        getWork()
                    }
                    lastActive = active
                }
                if (lastPercent != percent) {
                    lastPercent = percent
                    document.getElementById('success').innerHTML = percent + ' %'
                }
            } else if (xmlhttp.status === 400) {
                //alert('There was an error 400')
            } else {
                //alert('something else other than 200 was returned')
            }
        }
    }
    xmlhttp.open('POST', '/get_process')
    xmlhttp.send()
}

function getWork() {
    const xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {
            if (xmlhttp.status === 200) {
                console.log(xmlhttp.responseText)
                let item = JSON.parse(xmlhttp.responseText)
                let section1 = item.section1
                let section2 = item.section2
                let speed = item.speed

                document.getElementsByClassName('dash_section')[0].innerHTML = `
                    <table>
                      <tr>
                        <td>ส่วนที่ 1 : </td>
                        <td id="active">${section1}</td>
                      </tr>
                      <tr>
                        <td>ส่วนที่ 2 : </td>
                        <td id="active">${section2}</td>
                      </tr>
                      <tr>
                        <td>ความเร็ว : </td>
                        <td id="active">${speed}</td>
                      </tr>
                      <tr>
                        <td>ความคืบหน้า : </td>
                        <td id="success">0 %</td>
                      </tr>
                    </table>
                    <button type="reset" name="button" onclick="cancel()">ยกเลิก</button>
                `

            } else if (xmlhttp.status === 400) {
                //alert('There was an error 400')
            } else {
                //alert('something else other than 200 was returned')
            }
        }
    }
    xmlhttp.open('POST', '/get_work')
    xmlhttp.send()
}

function cancel() {
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
    xmlhttp.open('POST', '/cancel')
    xmlhttp.send()
}
