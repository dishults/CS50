document.addEventListener('DOMContentLoaded', () => {
    calculateTotal();
    removeElements();
});

function calculateTotal() {
    price = document.querySelectorAll('.price');
    var sum = 0.0;
    
    price.forEach((p) => {
        sum += parseFloat(p.dataset.price);
    });
    document.getElementById('total').innerHTML = sum.toFixed(2) + '$';
}

function removeElements() {
    removeButton = document.getElementsByName('remove');

    removeButton.forEach((button) => {
        button.onclick = () => {
            var orderNb = parseInt(button.dataset.order);
            if (confirm('Are you sure you want to delete this order?')) {
                var url = "/delete/" + orderNb;
                window.location.href = url;
            }
        }
    });
}

function orderPlaced() {
    alert('Thank you for your order!')
}