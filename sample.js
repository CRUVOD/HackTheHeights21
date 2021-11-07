var jsondata = [];

function functionget() {
  fetch("https://raw.githubusercontent.com/CRUVOD/HackTheHeights21/main/Testfile.json")
  .then(response => response.json())
  .then(json => {
      jsondata = json;
    }
  )
  var current = document.querySelector('.contain');
  var counter = 0;
  
  for(let i in jsondata) {
    if(counter % 2 == 0) {
      var containerleft = document.createElement('div');
      containerleft.className = 'container left';
      current.insertAdjacentElement('afterend', containerleft);
      current = containerleft;

      var dataleft = document.createElement('div');
      console.log(jsondata[i][0]);
      dataleft.innerHTML = jsondata[i][0];
      dataleft.className = 'dataleft';
      current.append(dataleft);

      var icon = document.createElement('i');
      icon.className = 'icon fa fa-home';
      current.append(icon);

      var content = document.createElement('div');
      content.className = 'content';
      current.append(content);

      var h2 = document.createElement('h2');
      h2.innerHTML = jsondata[i][1];
      content.append(h2);

      var p = document.createElement('p');
      p.innerHTML = jsondata[i][2];
      content.append(p);

      counter += 1;
    } else {
      var containerright = document.createElement('div');
      containerright.className = 'container right';
      current.insertAdjacentElement('afterend', containerright);
      current = containerright;

      var dataright = document.createElement('div');
      dataright.innerHTML = jsondata[i][0];
      dataright.className = 'dataright';
      current.append(dataright);

      var icon = document.createElement('i');
      icon.className = 'icon fa fa-gift';
      current.append(icon);

      var content = document.createElement('div');
      content.className = 'content';
      current.append(content);

      var h2 = document.createElement('h2');
      h2.innerHTML = jsondata[i][1];
      content.append(h2);

      var p = document.createElement('p');
      p.innerHTML = jsondata[i][2];
      content.append(p);

      counter += 1;
   }
  }
}
