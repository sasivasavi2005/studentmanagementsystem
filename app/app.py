from flask import Flask,render_template
#initialize flask
app=Flask(__name__)


#define routes
@app.route('/')
def home():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)