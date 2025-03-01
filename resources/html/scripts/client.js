const ws = new WebSocket('ws://localhost:8765');

ws.onopen = function(){
    addMessage("Connected to WebSocket server");

};

ws.onmessage = function (event){
    addMessage("Server: " + event.data);
};

ws.onerror = function(error){
    addMessage("WebSocket Error: " + error.message);
};

ws.onclose = function(){
    addMessage("Disconnected from WebSocket server");
};

function sendMessage() {
    const input = document.getElementById("messageInput");
    if (input.value.trim() !== "") { 
        ws.send(input.value);
        addMessage("You: " + input.value);
        input.value = "";
    }
}


function addMessage(msg){
    const messageDiv = document.getElementById("messages");
    const messageElement = document.createElement("p");
    messageElement.textContent = msg;
    messageDiv.appendChild(messageElement);
}
