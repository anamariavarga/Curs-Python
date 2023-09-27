from flask import Flask, render_template

app = Flask('My First webapp')


@app.route('/')
@app.route('/acasa/')
def acasa():
    return 'Bine ati venit! Pagina este in constructie.'


@app.route('/portofoliu/')
def portofoliu():
    return 'In curand'


if __name__ == '__main__':
    app.run(debug=True)
