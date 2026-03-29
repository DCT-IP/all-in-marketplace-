@app.route('/')
def home():
    return render_template('index.html', products=get_all_products())