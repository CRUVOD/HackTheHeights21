document.addEventListener('DOMContentLoaded', function() {
    for (let i = 0; i < 5; i++) {
        var div = document.createElement('div');
        div.id = 'container';
        div.innerHTML = 'Hi there!';
        div.className = 'border pad';
        
        document.body.appendChild(div);
      }
}, false);