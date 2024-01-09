from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/catelog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db=SQLAlchemy(app)
@app.route('/new')
@app.route('/')
def hello_world():

    return render_template('movie.html')
@app.route('/user')
@app.route('/user/<name>')
def no_query_string(name='sagar'):
    return '<hi> hello there ! {} </h1>'.format(name)
@app.route('/text/<string:name>')
def working_with_string(name):
    return '<hi> Here is a String '+name+'</h1>'
@app.route('/numbers/<int:number>')
def working_with_number(number):
    return '<hi> The Number you Picked is '+str(number)+'</h1>'
@app.route('/add/<int:num1>/<int:num2>')
def adding_integer(num1,num2):
    return '<hi> The Sum is  :{}'.format(num1+num2)+'</h1>'
@app.route('/product/<float:num1>/<float:num2>')
def product_two_number(num1,num2):
    return '<hi> The Product is  :{}'.format(num1*num2)+'</h1>'
@app.route('/temp')
def render_temp():
    movie_list=['iron man',
                'ghost rider',
                'jurassic world',
                'real steel',
                'predator',
                'aliens vs predator'
                ]
    return render_template('movie.html',
                           movies=movie_list,
                           name="sagar"
                           )
@app.route('/table')
def table_display():
    movie_list={'iron man':1,
                'ghost rider':2,
                'jurassic world':3,
                'real steel':4,
                'predator':5,
                'aliens vs predator':6
    }
    return render_template('table_data.html',
                           movies=movie_list,
                           name="sarang"
                           )

class Publication(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Name is {}".format(self.name)
#Book Table
class Book(db.Model):
     __tablename__='book'
     id=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String(500),nullable=False , index=True)
     author=db.Column(db.String(300))
     avg_rating=db.Column(db.Float)
     format=db.Column(db.String(50))
     image=db.Column(db.String(100), unique=True)
     num_pages=db.Column(db.Integer)
     pub_date=db.Column(db.DateTime , default=datetime.utcnow())
     #Establish Relationship
     pub_id=db.Column(db.Integer,db.ForeignKey('publication.id'))

     def __init__(self,title,author,avg_rating,format,image,num_pages,pub_date,pub_id):
         
         self.title=title
         self.author=author
         self.avg_rating=avg_rating
         self.format=format
         self.image=image
         self.num_pages=num_pages
         self.pub_date=pub_date
         self.pub_id=pub_id
     def __repr__(self):
        return '{} by {}'.format(self.title,self.author)     
         
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
