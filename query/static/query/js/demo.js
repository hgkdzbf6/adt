/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2016-07-19 19:49:47
 * @version $Id$
 */

var droptarget;
var pic_data;
var pic_url;

// set the status text in our display
function setStatus(text, show=true) {
    document.getElementById("status").innerHTML = text;
    if(show==false)
        $('#status').hide();
    else
        $('#status').show();
}

// handle drag events in the drop target
function handleDragEnter(evt) {

    // if the browser supports accessing the file
    // list during drag, we display the file count
    var files = evt.dataTransfer.files;

    if (files)
        setStatus("There are " + evt.dataTransfer.files.length +
            " files in this drag.",true);
    else
        setStatus("There are unknown items in this drag.",true);

    droptarget.className = "highlighted";

    evt.stopPropagation();
    evt.preventDefault();

    return false;
}

// preventing the default dragover behavior
// is necessary for successful drops
function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    return false;
}

// reset the text and status when drags leave
function handleDragLeave(evt) {
    setStatus("请拖动图片到这里");

    droptarget.className = "validtarget";
    return false;
}

// handle the drop of files
function handleDrop(evt) {
    // cancel the event to prevent viewing the file
    evt.preventDefault();
    evt.stopPropagation();

    var filelist = evt.dataTransfer.files;

    var message = document.getElementById("status").innerHTML;
    message+="There were " + filelist.length + " files dropped.";

    // show a detail list for each file in the drag
    message += "<ol>";

    [].forEach.call(filelist, function(file) {
        pic_url=file.name
        message += "<li>";
        message += "<strong>" + file.name + "</strong> ";
        message += "(<em>" + file.type + "</em>) : ";
        message += "size: " + file.size + " bytes - ";
        message += "modified: " + file.lastModifiedDate;
        message += "</li>";
    });

    message += "</ol>";

    //message="";
    setStatus(message);
    droptarget.className = "validtarget";

    //shou the picture below
    for (var i = filelist.length - 1; i >= 0; i--) {
        var file = filelist[i];
        var imageType = /image.*/;

        if (file.type.match(imageType)) {
            var img = document.getElementById("img");
            img.classList.add("obj");
            img.file = file;
            document.getElementById("status").style.height="auto";
            var reader = new FileReader();
            reader.onload = (function(aimg) {
                return function(e) {
                    aimg.src = e.target.result;
                    pic_data=e.target.result;
                    // alert("aaa"+ aimg.src);
                };
            })(img);

            reader.readAsDataURL(file);
        }
    }

    return false;
}
function uploadPic(){
    var pic_form=new FormData();
    pic_form.append('image',pic_data);
    var request=new XMLHttpRequest();
    request.open("POST","/query/");
    response=request.send(pic_form);
    console.log(response)
}
function loadDemo() {

    droptarget = document.getElementById("droptarget");
    droptarget.className = "validtarget";

    droptarget.addEventListener("dragenter", handleDragEnter, false);
    droptarget.addEventListener("dragover", handleDragOver, false);
    droptarget.addEventListener("dragleave", handleDragLeave, false);
    droptarget.addEventListener("drop", handleDrop, false);

    setStatus("请拖动图片到这里");
}

window.addEventListener("load", loadDemo, false);
