# Uruchamiamy komendą:
# flask run --debug
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/hello/")
def hello():
    return "Hello, world!"


@app.route("/template/")
def hello_template():
    return render_template(
        'hello.html'
    )


@app.route("/hello/<string:name>/")
def hello_name(name):
    return render_template(
        'hello_name.html',
        name=name,
    )


@app.route("/hello_form/", methods=['GET', 'POST'])
def hello_form():
    if request.method == "GET":
        return render_template(
            'hello_form.html'
        )

    if request.method == "POST":
        # parametry metody form siedzą w atrybucie form
        data = request.form

        # parametry metody get siedzą w atrybuce args
        # data = request.args

        name = data.get('name')

        return render_template(
            'hello_name.html',
            name=name
        )
