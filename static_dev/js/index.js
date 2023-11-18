
// const gifAnimation = document.querySelector('.main__gif-animation');
// gifAnimation.addEventListener('mouseover', () => {
//   gifAnimation.src = 'https://media1.giphy.com/media/i7C42rkeDTeeRz2KRq/giphy.gif?cid=ecf05e47hh6518c5spmwjfoecgmrn0ay9s7u4ovo5guxw9zk&ep=v1_stickers_search&rid=giphy.gif&ct=s';// Заменяем статическое изображение на gif
// });
// gifAnimation.addEventListener('mouseout', () => {
//   gifAnimation.src = './img/image_2023-11-17_17-31-23.png'; // Заменяем gif на статическое изображение
// });


function sendData() {
    var userInput = document.querySelector('.intro__input-input').value;
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    var data = { text: userInput };

    fetch('/bot/questions/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Успешно отправлено:', data);
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}


