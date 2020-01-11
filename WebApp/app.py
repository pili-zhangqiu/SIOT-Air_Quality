from flask import Flask, render_template

app = Flask(__name__)

# Define the main route:
@app.route('/')
def index():
    return render_template('data_report2.html')

@app.route("/data_report")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

if __name__ == '__main__':
    # Run code server and app:
    app.run(debug=True, host='0.0.0.0')
