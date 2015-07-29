from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.args)
    print(request.form)
    message = ''
    if request.method == 'POST':
        filename = request.files['input_file'].filename
        now = datetime.now().isoformat()
        full_name = '%s_%s_%s' % (filename, request.form['name'], now)
        with open(full_name, 'w') as f:
            f.write(request.files['input_file'].read())
        # message = 'Uplaod successful!'
        return redirect(url_for('next_page'))
    return render_template('index.html', message=message)

@app.route('/next-page/')
def next_page():
    return 'woo!'

if __name__ == "__main__":
    app.run(debug=True)
