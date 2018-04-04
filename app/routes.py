from app import app
from flask import render_template,flash, redirect, url_for,jsonify, request
from datetime import datetime as dt
from datetime import timedelta
import datetime

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html') 


@app.route('/compute', methods=['POST'])
def compute():
    # import ipdb; ipdb.set_trace()
    
    form_data = request.form

    # All the data are expected to be serialized
    device_start_dates = form_data.getlist('device_start')
    device_end_dates = form_data.getlist('device_end')
    stop_watch_starts = form_data.getlist('stop_watch_start')
    stop_watch_ends = form_data.getlist('stop_watch_end')

    date_format = "%Y-%m-%d %H:%M:%S"

    # Loop in all the above list 
    # All the above list has same length
    for index in range(len(device_start_dates)):
        d_start_obj = dt.strptime(device_start_dates[index],date_format)
        d_end_obj = dt.strptime(device_end_dates[index], date_format)
        
        timedelta = d_end_obj - d_start_obj
        print("For Device ",timedelta)

        d_diff = timedelta.total_seconds()

        s_start_obj = dt.strptime(stop_watch_starts[index],date_format)
        s_end_obj = dt.strptime(stop_watch_ends[index], date_format)
        timedelta = s_end_obj - s_start_obj
        print("For StopWatch ", timedelta)
        s_diff = timedelta.total_seconds()

        # Total Difference between the StopWatch and Device Time
        total_diff = s_diff - d_diff

        print("For Device {0}, the time difference is {1}".format(index, str(datetime.timedelta(seconds=total_diff))))
    
    return render_template('thanks.html')