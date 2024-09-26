from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
#initilaize flask app
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin123@localhost/student_management'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS']=False
#initialize the database
db=SQLAlchemy(app)
#define student model
class Students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    course=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"Student('{self.name}','{self.age}','{self.course}')"

@app.route('/')
def home():
    students=Students.query.all()
    return render_template('index.html',students=students)
if __name__=='__main__':
    app.run(debug=True)
