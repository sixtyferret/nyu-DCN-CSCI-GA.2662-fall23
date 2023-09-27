from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/time')
def timeteller():
    current_time = datetime.now()
    return "Current Time: " + str(current_time) 

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
