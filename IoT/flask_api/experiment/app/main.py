from pydoc import render_doc
from flask import Flask, render_template

app = Flask(__name__)


def show_home() -> render_doc:
    initial_information = {
        'title':'Experiment AI',
    }
    return render_template('index.html', context=initial_information)

if __name__=='__main__':
    app.add_url_rule('/', view_func=show_home)
    app.run(debug=True, port=5005, host='0.0.0.0')