document.addEventListener('DOMContentLoaded', function() {

        var current = document.querySelector('.contain');
        for(let i = 0; i < 4; i++) {
          if(i % 2 == 0) {
            var containerleft = document.createElement('div');
            containerleft.className = 'container left';
            current.insertAdjacentElement('afterend', containerleft);
            current = containerleft;

            var dataleft = document.createElement('div');
            dataleft.innerHTML = 'some text';
            dataleft.className = 'dataleft';
            current.append(dataleft);

            var icon = document.createElement('i');
            icon.className = 'icon fa fa-home';
            current.append(icon);

            var content = document.createElement('div');
            content.className = 'content';
            current.append(content);

            var h2 = document.createElement('h2');
            h2.innerHTML = 'text here';
            content.append(h2);

            var p = document.createElement('p');
            p.innerHTML = 'paragraph here';
            content.append(p);
          } else {
            var containerright = document.createElement('div');
            containerright.className = 'container right';
            current.insertAdjacentElement('afterend', containerright);
            current = containerright;

            var dataright = document.createElement('div');
            dataright.innerHTML = 'some text';
            dataright.className = 'dataright';
            current.append(dataright);

            var icon = document.createElement('i');
            icon.className = 'icon fa fa-gift';
            current.append(icon);

            var content = document.createElement('div');
            content.className = 'content';
            current.append(content);

            var h2 = document.createElement('h2');
            h2.innerHTML = 'text here';
            content.append(h2);

            var p = document.createElement('p');
            p.innerHTML = 'paragraph here';
            content.append(p);
          }
        }
        document.getElementsById("image").style.visibility = "hidden";
      }, false);
  
function functionget() {
  console.log(document.getElementById("searchfield").value);
  readTextFile("Testfile.json", function(text){
  var data = JSON.parse(text);
  console.log(data);
  })
}

function readTextFile(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == 200) {
          callback(rawFile.responseText);
      }
  }
  rawFile.send(null);
}
fetch("https://newexample.s3.ir-thr-at1.arvanstorage.com/example.json")
  .then(response => response.json())
  .then(json => console.log(json));