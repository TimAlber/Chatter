function xml_http_post(url, data, callback) {
    var req = false;
    try {
        // Firefox, Opera 8.0+, Safari
        req = new XMLHttpRequest();
    }
    catch (e) {
        // Internet Explorer
        try {
            req = new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch (e) {
            try {
                req = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Your browser does not support AJAX!");
                return false;
            }
        }
    }
    req.open("POST", url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback(req);
        }
    }
    req.send(data);
}

function msg_button() {
    var msg = document.test_form.msgf.value;
    var nick = document.test_form.nickf.value;
    //var msg =  document.getElementById("msg").value;
    xml_http_post("#",JSON.stringify([nick,msg]), relodframe)
//    alert("Callback was called.");
}

//function nick_button() {
//    var nick = document.test_form.nickf.value;
    //var nick =  document.getElementById("nick").value;
//    xml_http_post("small.html", nick, relodframe)
//    alert("Callback was called.");
//}

function relodframe(req) {
    var elem = document.getElementById('frame')
    elem.contentDocument.location.reload(true);
//    alert("Callback was called.");
}
