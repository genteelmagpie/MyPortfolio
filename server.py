from flask import Flask, render_template, request
from helperFunctions import writeToCSV

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
        retVal = writeToCSV(data)
        if retVal == 1:
            return ' Thank you for reaching out. We will get in touch shortly.'
        elif retVal == -1:
            return " Thank you for reaching out again. We will contant you shortly."
        elif retVal == 0:
            return " Submission of the form was not completed. Try again later."
        else:
            return " Form Submission failed. "
    else:
        return "Something went wrong. Data was not sent."
