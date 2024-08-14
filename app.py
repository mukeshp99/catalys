from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# In-memory storage
data_storage = {}

# Mock data retrieval endpoint with template
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data
    mock_data = ['apple', 'banana', 'cherry']
    processed_data = process_data(mock_data)
    # Store processed data in memory
    data_storage['processed_data'] = processed_data
    return render_template('fetch_data.html', data=mock_data, processed_data=processed_data)

# Data processing function
def process_data(data):
    # Example processing: convert all text to uppercase
    return [item.upper() for item in data]

# Data retrieval endpoint with template
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Return processed data from memory
    if 'processed_data' in data_storage:
        return render_template('processed_data.html', processed_data=data_storage['processed_data'])
    return render_template('processed_data.html', processed_data=None)

if __name__ == '__main__':
    app.run(debug=True)
