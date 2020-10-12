from flaskblog import db,bcrypt
from flaskblog import app as application
from flaskblog.models import User,Post
import os


def initialize_database():
    if os.path.exists(os.path.join(application.root_path,'site.db')):
        return
    db.create_all()
    password='password'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    admin=User(username='admin',email='fake@email.com',password=hashed_password)
    db.session.add(admin)
    db.session.commit()
    user=User.query.filter_by(username='admin').first()
    post=Post(title='Admin test post',content='test content',author=user)
    db.session.add(post)
    db.session.commit()
    



if __name__=='__main__':
    initialize_database()
    application.run(port=8000)

'''
from db initialization
1. db.create_all()
2. create a user
3. create a post with post.author=user

it seems the code above cannt create post and user,idk why
we can adda existing db file to .zip and upload to AWS EB, will work
'''