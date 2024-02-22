from flask import Flask, render_template

app = Flask(__name__)

# This is the main page of the website which is the dashboard
@app.route("/")
def dashboard():
    return render_template('dashboard_page/dashboard.html')

# This is the second page of the website which is the raw data
@app.route("/rawdata")
def raw_data():
    return render_template('raw_data_page/raw_data.html')

if __name__ == '__main__':
    app.run(debug=True)