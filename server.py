from flask import Flask, render_template, request
from helperFunctions import writeToCSV
from helperFunctionsTwo import sendEmail

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("./index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        retVal = writeToCSV(data)
        if retVal == 1:
            sendEmail(data)
            return 'OK'
        elif retVal == -1:
            return "OK2"
        elif retVal == 0:
            return "ERRORS"
        else:
            return "ERRORS"
    else:
        return "Something went wrong. Data was not sent."
