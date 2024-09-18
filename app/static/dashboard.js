const socket = new WebSocket('ws://localhost:8080/metrics');

socket.onmessage = function (event) {
    const transactionData = JSON.parse(event.data);
    updateDashboard(transactionData);
};

function updateDashboard(data) {
    document.getElementById('total-transactions').innerText = data.total_transactions;
    document.getElementById('total-amount').innerText = data.total_amount.toFixed(2);
}
