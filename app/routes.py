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

    difference = []

    # Loop in all the above list 
    # All the above list has same length
    for index in range(len(device_start_dates)):
        d_start = device_start_dates[index]
        d_end = device_end_dates[index]
        s_start = stop_watch_starts[index]
        s_end = stop_watch_ends[index]

        each_node = {}
        d_start_obj = dt.strptime(d_start,date_format)
        d_end_obj = dt.strptime(d_end, date_format)
        
        timedelta = d_end_obj - d_start_obj
        # print("For Device ",timedelta)

        d_diff = timedelta.total_seconds()

        s_start_obj = dt.strptime(s_start,date_format)
        s_end_obj = dt.strptime(s_end, date_format)
        timedelta = s_end_obj - s_start_obj
        # print("For StopWatch ", timedelta)

        s_diff = timedelta.total_seconds()

        # Total Difference between the StopWatch and Device Time
        if s_diff > d_diff:
            total_diff = s_diff - d_diff
        else:
            total_diff = d_diff - s_diff

        each_node['name'] = "Device "+ str(index+1)
        each_node['diff'] = str(datetime.timedelta(seconds=total_diff))
        each_node['d_start'] = d_start
        each_node['d_end'] = d_end
        each_node['s_start'] = s_start
        each_node['s_end'] = s_end

        print("For {0}, the time difference is {1}".format(each_node['name'],each_node['diff'] ))
        difference.append(each_node)

    
    return render_template('thanks.html',
                            diff =difference,                            
                            )