from flask import Flask, render_template
app = Flask('Utilities app')


@app.route('/')
@app.route('/acasa')
def acasa_page():
    return render_template('acasa.html')

@app.route('/portofoliu')
def portofoliu_page():
    return render_template('portofoliu.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
