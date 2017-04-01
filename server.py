# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import configparser

from flask import Flask, render_template, request, url_for, redirect, jsonify

# import controller
import profile

app = Flask(__name__)
profile_path = os.path.dirname(os.path.abspath(__file__)) + "/config/profile"
working_path = os.path.dirname(os.path.abspath(__file__)) + "/queue"


@app.route('/')
def index():
    if os.path.exists(working_path + "/status.ini"):
        cfg = configparser.ConfigParser()
        with open(working_path + "/status.ini", 'r') as status_file:
            cfg.read_file(status_file)
        active = cfg['status']['active']
        return render_template('index.html', active=active)
    else:
        return render_template('index.html', active="0")


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
    # filename.ini
    data = request.data.decode('utf8')
    profile_manager = profile.Profile()
    # full_list = profile_manager.load_file()
    list_file = profile_manager.load_file(option="file")
    for item in list_file:
        if data == item:
            if not check_queue():
                src = profile_path + "/" + data
                dest = working_path + "/work.ini"
                # with open(src, 'r') as fsrc:
                #     with open(dest, 'wb') as fdest:
                shutil.copy2(src, dest)
                if os.path.exists(working_path + "/status.ini"):
                    cfg = configparser.ConfigParser()
                    with open(working_path + "/status.ini", 'r') as process_file:
                        cfg.read_file(process_file)
                        cfg['status']['active'] = str(1)
                        cfg['status']['command'] = str(0)
                    with open(working_path + "/status.ini", 'w') as status_file:
                        cfg.write(status_file)
                return url_for('index')
            else:
                return url_for('index')


@app.route('/remove_profile', methods=['POST'])
def remove_profile():
    data = request.data.decode('utf8')
    os.remove(profile_path + "/" + data)
    return url_for('load_select_profile_page')


def check_queue():
    return os.path.exists(working_path + "/work.ini")


@app.route('/shutdown')
def shutdown():
    subprocess.call("reboot")


@app.route('/get_process', methods=['POST'])
def get_process():
    active = "0"
    success = "0"
    cfg = configparser.ConfigParser()
    if os.path.exists(working_path + "/status.ini"):
        with open(working_path + "/status.ini", 'r') as status_file:
            cfg.read_file(status_file)
            active = cfg['status']['active']
    if os.path.exists(working_path + "/process.ini"):
        with open(working_path + "/process.ini", 'r') as process_file:
            cfg.read_file(process_file)
            success = cfg['process']['success']
    return jsonify({"active": active, "success": success})


@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    if os.path.exists(working_path + "/status.ini"):
        cfg = configparser.ConfigParser()
        with open(working_path + "/status.ini", 'r') as process_file:
            cfg.read_file(process_file)
        # cfg['status'] = {}
        cfg['status']['command'] = str(1)
        with open(working_path + "/status.ini", 'w') as status_file:
            cfg.write(status_file)
    return url_for('index')


@app.route('/get_work', methods=['POST'])
def get_work():
    cfg = configparser.ConfigParser()
    if os.path.exists(working_path + "/work.ini"):
        with open(working_path + "/work.ini", 'r') as status_file:
            cfg.read_file(status_file)
        section1 = cfg['profile']['section1']
        section2 = cfg['profile']['section2']
        speed = cfg['profile']['speed']
    return jsonify({"section1": section1, "section2": section2, "speed": speed})


if __name__ == '__main__':
    # control = controller.Control()
    app.run(debug=True, host='0.0.0.0')
