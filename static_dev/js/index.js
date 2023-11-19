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

function sendDataInput() {
    var userInputProfil = document.querySelector('.item__form-input-input').value;
    var userID = document.querySelector('.item__id').textContent
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    var data = {answer: userInputProfil, id: userID};

    fetch('answer_post/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
}

let selectedRating = 0;


function showResponse(event) {
  event.preventDefault(); // Предотвращаем отправку формы, чтобы страница не перезагружалась

  var userInput = document.querySelector('.intro__input-input'); // Получаем введенные пользователем данные
  var messageContainer = document.querySelector('.intro__message');
	var container = document.querySelector('.text__message');
	container.style.display = 'flex';
  messageContainer.textContent = userInput; // Вставляем данные в элемент intro__message
}
function toggleDropdown() {
	var card = document.querySelector(".profil__items");
	if (card.style.display === "none") {
		card.style.display = "grid";
	} else {
		card.style.display = "none";
	}
}

function toggleDropdown2() {
	var card2 = document.querySelector(".profil__items2");
	if (card2.style.display === "none") {
		card2.style.display = "grid";
	} else {
		card2.style.display = "none";
	}
}

document.addEventListener('DOMContentLoaded', function() {
    const image = document.querySelector('.img');

    // Добавляем обработчик события для клика
    image.addEventListener('click', function() {
        // Переключаем класс rotated при каждом клике
        image.classList.toggle('rotated');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const image1 = document.querySelector('.img1').value;

    // Добавляем обработчик события для клика
    image1.addEventListener('click', function() {
        // Переключаем класс rotated при каждом клике
        image1.classList.toggle('rotated');
    });
});

function setRating(rating) {
    document.getElementById('selectedRating').innerText = rating;
}