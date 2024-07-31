const socket = new WebSocket('ws://' + window.location.host + '/ws/email_messages/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    updateProgress(data.progress, data.total);
};


const progressBar = $('#progress-bar');
let checkedCount = 0;

const socket = new WebSocket('ws://localhost:8000/ws/messages/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    checkedCount++;
    $('#checked-count').text(checkedCount);
    
    // Если сообщение найдено, добавляем его в таблицу
    // Обновляем прогресс-бар, если нужно
};