const BASE_URL = "http://127.0.0.1:5000";

const seller_id = localStorage.getItem("user_id") || 2;

fetch(`${BASE_URL}/seller/${seller_id}`)
.then(res => res.json())
.then(data => {

    // stats
    document.getElementById("total_products").innerText = data.stats.total_products;
    document.getElementById("total_orders").innerText = data.stats.total_orders;
    document.getElementById("total_revenue").innerText = data.stats.total_revenue;

    // products
    const container = document.getElementById("seller_products");

    data.products.forEach(p => {
        const div = document.createElement("div");
        div.innerHTML = `
            <p>${p.product_name} - ₹${p.price} (Stock: ${p.stock})</p>
        `;
        container.appendChild(div);
    });
});