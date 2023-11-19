function sendData() {
    var userInput = document.querySelector('.intro__input-input').value;
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    var data = {text: userInput};
    fetch('post_question/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
    }

    function showResponse(event) {
      event.preventDefault();
      const userInput = document.querySelector('.intro__input-input').value;
      document.getElementById('overlay').style.display = 'block';
      document.getElementById('response').style.display = 'block';
      document.getElementById('userInputDisplay').innerText = userInput;
    }