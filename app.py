import os

from flask import Flask, render_template, request

 
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services/mopidy', methods=['PATCH'])
def set_service_status():
    os.system('sudo service mopidy restart')

@app.route('/server', methods=['PATCH'])
def set_server_status():
    status = request.form.get('status', '')
    if status == 'shutdown':
        os.system('sudo shutdown -t 1')        
#    elif status == 'reboot':

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
