from flask import Flask
from flask import render_template, request
from markupsafe import escape
from books import books as b

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'])
@app.route('/')
def hello_world():
    a = 10
    page_content = "<h1> testststst </h1>"
    page_content += f"<h1> h-1 abcdefg {a} </h1>"
    return page_content


@app.route("/books/<int:name>")
def nama(name):
    try:
        return render_template('test.html', name=name, books=b[name])
    except:
        return render_template('test.html', name="nothing is there")


@app.route("/post/<int:post_id>")
def asd(post_id):
    return f"Hello, {escape(post_id)}!"


@app.route("/author", methods=['GET', 'POST'])
def author():
    if 'author_id' in request.form:
        b[request.form['author_id']] = []

    return render_template('author.html', books=b)


if __name__ == '__main__':
    app.run(debug=True)
