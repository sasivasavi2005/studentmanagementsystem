from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#initilaize flask app
app=Flask(__name__)
#configure the sqlalchemy database
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin123@localhost/student_management'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS']=False#fixed the typo here
#initilaize the database
db=SQLAlchemy(app)
#deine the students model
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

@app.route('/add',methods=['POST'])
def add():
    formName=request.form['name']
    formAge=request.form['age']
    formCourse=request.form['course']

    #create new student record 
    newStudent= Students(name=formName, age=formAge , course=formCourse )
    db. session.add(newStudent)
    db.session.commit()
    return render_template('index.html')

@app.route('/edit<int:id>',methods=['GET','POST'])
def edit_student(id):
    studs = Students.query.get_or_404(id)#get the student id
    if request.method == 'POST':
        studs.name=request.form['name']
        studs.age=request.form['age']
        studs.course=request.form['course']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',student=studs)

@app.route('/delete/<int:id>',methods=['POST'])
def delete_student(id):
    studs = Students.query.get_or_404(id)#get the student id
    db.session.delete(studs)
    db.session.commit()
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)
