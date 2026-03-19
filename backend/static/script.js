// Load products
fetch('/products')
.then(res => res.json())
.then(data => {
    const container = document.getElementById('products');

    data.forEach(p => {
        const div = document.createElement('div');
        div.innerHTML = `
            <h3>${p.product_name}</h3>
            <p>${p.product_description}</p>
            <p>Stock: ${p.item_count}</p>
            <button onclick="addToCart(${p.product_id})">Add to Cart</button>
            <button onclick="placeOrder(${p.product_id})">Buy Now</button>
        `;
        container.appendChild(div);
    });
});


// Add to cart
function addToCart(product_id) {
    fetch('/add_to_cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 1, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// Place order
function placeOrder(product_id) {
    fetch('/place_order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 1, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// Load cart
function loadCart() {
    fetch('/cart/1')
    .then(res => res.json())
    .then(data => {
        const cartDiv = document.getElementById('cart');
        cartDiv.innerHTML = "";

        data.forEach(item => {
            const div = document.createElement('div');
            div.innerHTML = `
                <p>${item.product_name} - Quantity: ${item.quantity}</p>
            `;
            cartDiv.appendChild(div);
        });
    });
}