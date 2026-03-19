const BASE_URL = "http://127.0.0.1:5000";

const user_id = localStorage.getItem('user_id') || 1;


// ---------------- LOAD PRODUCTS ----------------
fetch(`${BASE_URL}/products`)
.then(res => res.json())
.then(data => {
    const container = document.getElementById('products');
    if (!container) return;

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


// ---------------- ADD TO CART ----------------
function addToCart(product_id) {
    fetch(`${BASE_URL}/add_to_cart`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user_id, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// ---------------- PLACE ORDER ----------------
function placeOrder(product_id) {
    fetch(`${BASE_URL}/place_order`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user_id, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// ---------------- LOAD CART ----------------
function loadCart() {
    fetch(`${BASE_URL}/cart/${user_id}`)
    .then(res => res.json())
    .then(data => {
        const cartDiv = document.getElementById('cart');
        if (!cartDiv) return;

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