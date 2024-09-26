from flask import Flask,render_template
#initialize flask
app=Flask(__name__)
#define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return render_template('CONTACT.html')

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ =='__main__':
    app.run(debug=True)