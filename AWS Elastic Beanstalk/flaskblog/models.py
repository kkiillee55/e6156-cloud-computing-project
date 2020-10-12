from flaskblog import db,app,login_manager
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

'''
this function is a must if using flask-login
for user management, place it with the User model, and just write this function
nothing needs to be changed
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


'''
the User model defined using flask-sqlalchemy,
it creates a schema in database, 
id, username, email, image, password are database columns
here image stores the path of user profile image file, and the default image is default.jpg

User will have posts, and Post is another database schema

posts=db.relationship('Post',backref='author',lazy=True)
this line specifies the relation between User and Post model
user.posts contain all post objects of user
post.author shows the user object

get_reset_token can generate a hashed timed token if user requests to change password
expires_sec=1800 means the token will expire after 1800 seconds

verify_reset_token can decode the token and know which user is trying to change password

'''
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(40),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)

    #user.posts is Post, post.author is User
    posts=db.relationship('Post',backref='author',lazy=True)

    def get_reset_token(self,expires_sec=1800):
        s=Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(app.config['SECRET_KEY'])
        try:
            user_id=s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    def __repr__(self):
        return 'ID:{}, User:{}, Email:{}, Profile_Pic:{}\n'.format(self.id,self.username,self.email,self.image_file)

'''
the Post class is a database schema,
it contains title, content and date_posted
date_posted is automatically generated based on the datetime.utcnow

user_id is a foreignkey to User table
in one-to-many relation, one User could have multiple posts
we define db.relation in User and db.foreignkey in Post
check https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html for more info
'''
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return 'Title:{}, Author:{}, Date:{}\n'.format(self.title,self.author.username,self.date_posted)





