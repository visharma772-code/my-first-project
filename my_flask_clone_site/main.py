from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Products Page
@app.route('/products')
def products():
    return render_template('products.html')

# Quality Page
@app.route("/quality")
def quality():
    return render_template("quality.html")

# Manufacturing Page
@app.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

# Clients Page
@app.route('/clients')
def clients():
    return render_template('clients.html')

# Site Map or Index
@app.route('/site')
def site():
    return render_template('site.html')


if __name__ == '__main__':
    app.run(debug=True, port=5123)
