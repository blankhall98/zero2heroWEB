from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
############################################################

@app.route('/')
def index():
    return render_template('index.html')

#three principal routes -----
@app.route('/courses')
def courses():
    pass

@app.route('/students')
def students():
    pass

@app.route('/teachers')
def teachers():
    pass

#log-in routes -----
@app.route('/students/login')
def StudentsLogin():
    pass

@app.route('/teachers/login')
def TeachersLogin():
    pass

#sign-up routes -----
@app.route('/students/signup')
def StudentsSignUp():
    pass

@app.route('/teachers/signup')
def TeachersSignUp():
    pass


############################################################
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()