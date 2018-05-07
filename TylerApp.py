from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
        # return "hello world"
        return render_template('index.html')

@app.route('/users/<string:username>')
def users(username):
    # return "<h1>hello %s</h1>" % usernamew
    return render_template('user.html', uname=username)
@app.route('/user')
def user():
    return "this is the page for users"

@app.route('/form')
def form():
        # return "hello world"
        return render_template('form.html')

if __name__ == '__main__':
    app.run()
