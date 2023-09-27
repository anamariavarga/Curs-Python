from flask import Flask, render_template

app = Flask('My First webapp')


@app.route('/')
@app.route('/acasa/')
def acasa():
    return render_template('acasa5.html')


@app.route('/portofoliu/')
def portofoliu():
    return render_template('portofoliu5.html')


@app.route('/contact/')
def contact():
    return render_template('contact5.html')


if __name__ == '__main__':
    app.run(debug=True)
