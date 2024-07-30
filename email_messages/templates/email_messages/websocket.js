const socket = new WebSocket('ws://' + window.location.host + '/ws/email/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    updateProgress(data.progress, data.total);
};