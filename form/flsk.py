
from flask import Flask, request, render_template
app = Flask(__name__)
global email, pwds, auth, user
user = []
auth = [
     {
     'User_name': 'Keshav Maheshwari',
     'user_id': 15344563,
     'email': 'keshav1534@gmail.com',
     'pwd'  : 'namskaram',
     'dob' : '02/02/2004',}]

@app.route('/')
@app.route('/<user>')
def index(user=None):
     return render_template('sample2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     return render_template('login.htm')

@app.route('/sign-up')
def sign_up():
     return render_template('sign_up.html')

@app.route('/sign-up?request', methods=['GET', 'POST'])
def sign_in():
     if request.method=='POST':
          fname = request.form.get('fname')
          lname = request.form.get('lname')
          email = request.form.get('email')
          pwd   = request.form.get('pwd')
          stay  = request.form.get('stay')
          for n in auth:
               if n['email'] == email:
                    return '<hr width="99%" size="2px" noshade><div style="text-align:center; font-size:20px;">Email already exist</div><hr width="99%" size="2px" noshade><a href="/login style="text-align:center;">Login?</a>'
          if stay:
               user[0['fname']] = fname
               user [0['lname']] = lname
               user[0['email']] = email
               user[0['pwd']] = pwd
          

@app.route('/more')
def explore():
     return render_template('Umey.htm')

@app.route('/aboutme')
def aboutme():
     return '<h1>About me</h1>'

@app.route('/profile/<int:post_id>')
def show_post(post_id):
     return 'Post id is <h2>%s</h>' %post_id

@app.route(f'/login/user', methods=['GET', 'POST'])
def gfg():
     
     if request.method == 'POST':
          mail = request.form.get('email')
          pwds = request.form.get('pwd')
          for n in auth:
               if n['email'] == mail and n['pwd'] == pwds:
                    return "Email: "+mail+"\nPassword: "+pwds
               else:
                    return "No such user found."
     return render_template('personal_site.htm')


if __name__ == "__main__":
     app.run()