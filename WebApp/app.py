from flask import Flask, render_template

app = Flask(__name__)

# Define the main route:
@app.route('/')
def index():
    return render_template('index.html')

# Other routes are:
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    # Run code server and app:
    app.run(debug=True, host='0.0.0.0')
