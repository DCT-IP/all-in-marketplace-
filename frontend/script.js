const BASE_URL = "http://127.0.0.1:5000";
let user_id = localStorage.getItem("user_id") || 1;


// ---------------- LOAD PRODUCTS ----------------
function loadProducts() {
    fetch(`${BASE_URL}/products`)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById('products');
        if (!container) return;

        container.innerHTML = "";

        data.forEach(p => {
            const div = document.createElement('div');
            div.classList.add("card");

            div.innerHTML = `
                <img src="${p.image_url}" />
                <h3>${p.product_name}</h3>
                <p>${p.product_description}</p>
                <p><b>₹${p.price}</b></p>
                <p>${p.category} | ${p.product_condition}</p>
                <p>Stock: ${p.stock}</p>
                <button onclick="addToCart(${p.product_id})">Add to Cart</button>
                <button onclick="placeOrder(${p.product_id})">Buy Now</button>
            `;

            container.appendChild(div);
        });
    })
    .catch(err => console.error("Products error:", err));
}


// ---------------- ADD TO CART ----------------
function addToCart(product_id) {
    fetch(`${BASE_URL}/add_to_cart`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user_id, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
    })
    .catch(err => console.error("Cart error:", err));
}


// ---------------- PLACE ORDER ----------------
function placeOrder(product_id) {
    fetch(`${BASE_URL}/place_order`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user_id, product_id: product_id })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        loadCart(); // refresh cart
    })
    .catch(err => console.error("Order error:", err));
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
                <p><b>${item.product_name}</b></p>
                <p>Quantity: ${item.quantity}</p>
                <button onclick="placeOrder(${item.product_id})">Order</button>
                <hr>
            `;

            cartDiv.appendChild(div);
        });
    })
    .catch(err => console.error("Cart load error:", err));
}


// ---------------- NAVIGATION ----------------
function goToCart() {
    window.location.href = "/cart";
}

function goHome() {
    window.location.href = "/";
}

function goToDashboard() {
    window.location.href = `/dashboard/${user_id}`;
}


// ---------------- AUTO LOAD BASED ON PAGE ----------------
if (window.location.pathname === "/") {
    loadProducts();
}

if (window.location.pathname === "/cart") {
    loadCart();
}