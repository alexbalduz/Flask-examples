from flask import render_template

@app.route('/rendered')
def hello(name=None):
    return render_template('template.html', name=name)


