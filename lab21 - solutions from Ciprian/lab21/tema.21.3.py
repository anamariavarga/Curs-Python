from flask import Flask, render_template

app = Flask('My First webapp')


@app.route('/')
@app.route('/acasa/')
def acasa():
    return render_template('acasa3.html')


@app.route('/portofoliu/')
def portofoliu():
    return render_template('portofoliu3.html')


if __name__ == '__main__':
    app.run(debug=True)
