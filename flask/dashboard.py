from flask import Flask, render_template, request, jsonify, Response
from statistics import mean
import pytz
from datetime import datetime
import calendar
import pressure

app = Flask(__name__)

pressure_data = None
# CALL DB DATA
# dummy data
dummy_data = [
    {'sensor': 'Temperature', 'value': 22, 'timestamp': '2023-02-22 12:00'},
    {'sensor': 'Temperature', 'value': 23, 'timestamp': '2023-02-22 12:01'},
    # Assume more temperature data here...
    {'sensor': 'Heart Rate', 'value': 75, 'timestamp': '2023-02-22 12:00'},
    {'sensor': 'Heart Rate', 'value': 76, 'timestamp': '2023-02-22 12:01'},
    # Assume more heart rate data here...
    {'sensor': 'Pressure', 'value': 45, 'timestamp': '2023-02-22 12:00'},
    {'sensor': 'Pressure', 'value': 46, 'timestamp': '2023-02-22 12:01'},
    # Assume more pressure data here...
]
# MODIFY AFTER CALL DB DATA
def prepare_sensor_data(sensor_name):
    # Filter data for the sensor
    sensor_data = [d for d in dummy_data if d['sensor'] == sensor_name]
    
    # Calculate average value (rounding for simplicity)
    avg_value = round(mean([d['value'] for d in sensor_data]), 2)
    
    # Get the last 10 data points
    last_10_data = sensor_data[-10:]
    
    return {
        'name': sensor_name,
        'average': avg_value,
        'timestamp': last_10_data[-1]['timestamp'],
        'data': last_10_data
    }



# This is the main page of the website which is the dashboard
@app.route("/")
def dashboard():
    return render_template('dashboard_page/dashboard.html')

# This is the second page of the website which is the raw data
@app.route("/rawdata")
def raw_data():
    # Prepare data for each sensor
    temperature_data = prepare_sensor_data('Temperature')
    heart_rate_data = prepare_sensor_data('Heart Rate')
    pressure_data = prepare_sensor_data('Pressure')

    return render_template('raw_data_page/raw_data.html', 
                           temperature=temperature_data, 
                           heart_rate=heart_rate_data, 
                           pressure=pressure_data)

@app.route('/api/pressure', methods=['POST'])
def receive_pressure_data():
    global pressure_data
    if request.method == 'POST':
        pressure_data = request.form['vibration']
        pressure.add_one({ "pressure": int(pressure_data), "timestamp": datetime_to_epoch() })
        return "Pressure received and inserted successfully"

@app.route('/api/pressure', methods=['GET'])
def get_all_pressure_data():
    return Response(pressure.retrieve_all(), mimetype='application/json')

@app.route('/api/latestpressure', methods=['GET'])
def get_latest_pressure_data():
    return jsonify(pressure.retrieve_latest())
    
def datetime_to_epoch():
    utc_now = datetime.utcnow()
    utc_timezone = pytz.timezone('UTC')
    utc_now = utc_timezone.localize(utc_now)
    sg_timezone = pytz.timezone('Asia/Singapore')
    sg_now = utc_now.astimezone(sg_timezone)
    epoch_time = calendar.timegm(sg_now.utctimetuple())
    return epoch_time

if __name__ == '__main__':
    app.run(debug=True)