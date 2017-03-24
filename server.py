# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import configparser

from flask import Flask, render_template, request, url_for, redirect

# import controller
import profile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_profile_page')
def load_add_profile_page():
    return render_template('add_profile.html')


@app.route('/add_profile', methods=['POST'])
def add_profile():
    data = request.form
    name = data['name']
    section1 = data['round1']
    section2 = data['round2']
    speed = data['speed']

    """
    save Profile
    """
    profile_manager = profile.Profile()
    profile_manager.add([section1, section2], speed)
    profile_manager.write_config(name=name)
    return redirect(url_for('index'))


@app.route('/select_profile_page')
def load_select_profile_page():
    return render_template('select_profile.html', file=list_profile())


@app.route('/list_profile', methods=['POST'])
def list_profile():
    profile_manager = profile.Profile()
    full_list = profile_manager.load_file()
    list_file = profile_manager.load_file(option="file")
    obj = {}
    for i in range(len(list_file)):
        obj[list_file[i]] = profile_manager.read_config(full_list[i])
    return obj


@app.route('/active', methods=['POST'])
def active():
    data = request.data.decode('utf8')
    profile_manager = profile.Profile()
    # full_list = profile_manager.load_file()
    list_file = profile_manager.load_file(option="file")
    for item in list_file:
        if data + ".ini" == item:
            if not check_queue():
                src = os.path.dirname(os.path.abspath(__file__)) + \
                    "/config/profile/" + data + ".ini"
                dest = os.path.dirname(os.path.abspath(
                    __file__)) + "/queue/work.ini"
                with open(src, 'r') as fsrc:
                    with open(dest, 'wb') as fdest:
                        shutil.copy2(src, dest)
                return url_for('index')
            else:
                return url_for('index')


def check_queue():
    return os.path.exists(os.path.dirname(os.path.abspath(__file__)) +
                          "/queue/work.ini")


@app.route('/shutdown')
def shutdown():
    subprocess.call("reboot")


@app.route('/get_process', methods=['POST'])
def get_process():
    with open(os.path.dirname(os.path.abspath(__file__)) +
              "/queue/process.ini", 'r') as process_file:
        cfg.read_file(process_file)
        success = cfg['process']['success']
    return success


if __name__ == '__main__':
    # control = controller.Control()
    cfg = configparser.ConfigParser()
    app.run(debug=True, host='0.0.0.0')
