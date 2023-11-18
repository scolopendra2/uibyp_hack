


function sendData() {
	var userInput = document.querySelector('.intro__input-input').value;
	var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
	var count = 0;

	var data = { text: userInput, count: count };

	fetch('/bot/questions/', {
		method: 'post',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
		.then(response => response.json())
		.then(data => {
			console.log('Успешно отправлено:', data);
		})
		.catch(error => {
			console.error('Ошибка:', error);
		});
}


