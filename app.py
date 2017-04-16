#!/usr/bin/python3
import sys
import os
import logging
import subprocess
import datetime as dt
import configparser
import time
from shutil import copyfile
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
# import controller
import profile
from ui import stack_menu

"""
This main function of this project
"""

__version__ = '0.3'
__author__ = 'Anukul Thienkasemsuk (anukul_thienkasemsuk@hotmail.com)'


class TheadingWork(QThread):
    work_signal = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if os.path.exists(working_path + "/work.ini"):
                self.work_signal.emit()
                break
            self.sleep(1)


class ThreadingTime(QThread):
    update_time = pyqtSignal(dt.datetime)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            current_time = dt.datetime.now()
            self.update_time.emit(current_time)
            self.sleep(1)


class ThreadingProcess(QThread):
    update_sig = pyqtSignal('QString')

    def __init__(self):
        QThread.__init__(self)
        self.cfg = configparser.ConfigParser()

    def __del__(self):
        self.wait()

    def run(self):
        print("PROCESS RUN")
        while True:
            if os.path.exists(working_path + "/process.ini"):
                with open(working_path + "/process.ini", 'r') as process_file:
                    self.cfg.read_file(process_file)
                success = self.cfg['process']['success']
                self.update_sig.emit(success)
            if not(os.path.exists(working_path + "/work.ini")):
                success = "100"
                self.update_sig.emit(success)
            self.sleep(1)


class Ui(object):
    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # create a file handler
        self.handler = logging.FileHandler(
            os.path.dirname(os.path.abspath(__file__)) + '/hist.log')
        self.handler.setLevel(logging.INFO)

        # create a logging format
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        # add the handlers to the logger
        self.logger.addHandler(self.handler)

        # Profile control
        self.profile_ctl = profile.Profile()

        # initial UI
        self.MainWindow = QMainWindow()
        self.ui = stack_menu.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Auto Control Page
        self.ui.btn_auto.clicked.connect(self.set_page_profile)
        self.ui.btn_add.clicked.connect(self.set_page_add_profile)
        self.ui.btn_cancel.clicked.connect(self.set_page_profile)
        self.ui.btn_sel.clicked.connect(self.set_page_process)
        self.ui.btn_auto_back.clicked.connect(self.set_page_main)

        # Profile
        self.ui.btn_add_con.clicked.connect(self.add_profile)
        self.ui.btn_del.clicked.connect(self.delete_profile)
        self.ui.btn_min_1.clicked.connect(self.min_sec1)
        self.ui.btn_min_2.clicked.connect(self.min_sec2)
        self.ui.btn_min_3.clicked.connect(self.min_speed)
        self.ui.btn_plus_1.clicked.connect(self.plus_sec1)
        self.ui.btn_plus_2.clicked.connect(self.plus_sec2)
        self.ui.btn_plus_3.clicked.connect(self.plus_speed)

        # Manual Control Page
        self.ui.btn_man.clicked.connect(self.set_page_manual)
        self.ui.btn_man_back.clicked.connect(self.set_page_main)

        """
        Disable manual for a while
        """
        # self.ui.btn_man_s1.clicked.connect(self.cc_s1)
        # self.ui.btn_man_s2.clicked.connect(self.cc_s2)
        # self.ui.spb_speed.valueChanged.connect(self.change_speed)

        # Shutdown Button
        self.ui.btn_shutdown.clicked.connect(self.shutdown)

        # Cancel Button
        self.ui.pushButton.clicked.connect(self.terminate_thread)

        # self.MainWindow.show()

        self.logger.info("Start System")
        self.MainWindow.showFullScreen()

        self.work_thread = TheadingWork()
        self.work_thread.work_signal.connect(self.set_page_process)
        self.work_thread.start()

    # Power off raspberry pi
    @staticmethod
    def shutdown():
        subprocess.call("poweroff")

    # Terminate all thread and back to main page
    def terminate_thread(self):
        if self.process_thread.isRunning():
            self.process_thread.terminate()
            self.time_thread.terminate()
            self.ui.stackedWidget.setCurrentIndex(0)
            cfg = configparser.ConfigParser()
            # Write command = 1 for stop motor
            if os.path.exists(working_path + "/status.ini"):
                with open(working_path + "/status.ini", 'r') as status_file:
                    cfg.read_file(status_file)
                cfg['status']['command'] = "1"
                cfg['status']['active'] = "0"
                with open(working_path + "/status.ini", 'w') as status_file:
                    cfg.write(status_file)

    # set main page
    def set_page_main(self):
        if not self.work_thread.isRunning():
            self.work_thread = TheadingWork()
            self.work_thread.work_signal.connect(self.set_page_process)
            self.work_thread.start()
        self.ui.stackedWidget.setCurrentIndex(0)

    # set profile page ans load list
    def set_page_profile(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.load_profile_list()

    # set add profile page
    def set_page_add_profile(self):
        self.val_sec1 = 0
        self.val_sec2 = 0
        self.val_speed = 50
        self.ui.lbl_in1.setText(str(self.val_sec1))
        self.ui.lbl_in2.setText(str(self.val_sec2))
        self.ui.lbl_in3.setText(str(self.val_speed))
        self.ui.stackedWidget.setCurrentIndex(2)

    # Increase and Decrease
    def min_sec1(self):
        if self.val_sec1 > 0:
            self.val_sec1 -= 1
        self.ui.lbl_in1.setText(str(self.val_sec1))

    def min_sec2(self):
        if self.val_sec2 > 0:
            self.val_sec2 -= 1
        self.ui.lbl_in2.setText(str(self.val_sec2))

    def min_speed(self):
        if self.val_speed > 0:
            self.val_speed -= 5
        self.ui.lbl_in3.setText(str(self.val_speed))

    def plus_sec1(self):
        self.val_sec1 += 1
        self.ui.lbl_in1.setText(str(self.val_sec1))

    def plus_sec2(self):
        self.val_sec2 += 1
        self.ui.lbl_in2.setText(str(self.val_sec2))

    def plus_speed(self):
        if self.val_speed < 100:
            self.val_speed += 5
        self.ui.lbl_in3.setText(str(self.val_speed))

    def add_profile(self):
        profile_list = [self.ui.lbl_in1.text(), self.ui.lbl_in2.text()]
        speed = self.ui.lbl_in3.text()
        self.profile_ctl.add(profile_list, speed)
        self.profile_ctl.write_config()
        self.set_page_profile()

    def set_page_manual(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def set_page_process(self):
        if os.path.exists(working_path + "/work.ini"):
            self.ui.stackedWidget.setCurrentIndex(4)
        else:
            print(self.select_profile())
            copyfile(self.select_profile(), working_path + "/work.ini")
            if os.path.exists(working_path + "/status.ini"):
                cfg = configparser.ConfigParser()
                with open(working_path + "/status.ini", 'r') as process_file:
                    cfg.read_file(process_file)
                    cfg['status']['active'] = str(1)
                    cfg['status']['command'] = str(0)
                with open(working_path + "/status.ini", 'w') as status_file:
                    cfg.write(status_file)
            self.ui.stackedWidget.setCurrentIndex(4)
        # Create Threading
        self.process_thread = ThreadingProcess()
        self.time_thread = ThreadingTime()
        self.process_thread.start()
        self.process_thread.update_sig.connect(self.update_process)
        self.time_thread.start()
        self.time_thread.update_time.connect(self.update_time)

    def load_profile_list(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['File', 'S1', 'S2', 'Speed'])
        self.ui.tbv_profile.setModel(model)
        list_profile_file = self.profile_ctl.load_file()

        row = []
        for file in list_profile_file:
            list_config = self.profile_ctl.read_config(file)
            item_name = QStandardItem(os.path.basename(file))
            item_sec1 = QStandardItem(list_config[0])
            item_sec2 = QStandardItem(list_config[1])
            item_spd = QStandardItem(list_config[2])
            row.append(item_name)
            row.append(item_sec1)
            row.append(item_sec2)
            row.append(item_spd)
            model.appendRow(row)
            row.clear()

        self.ui.tbv_profile.setColumnWidth(0, 93)
        self.ui.tbv_profile.setColumnWidth(1, 58)
        self.ui.tbv_profile.setColumnWidth(2, 58)
        self.ui.tbv_profile.setColumnWidth(3, 58)

    def delete_profile(self):
        list_file = self.profile_ctl.load_file()
        indexes = self.ui.tbv_profile.selectionModel().selectedRows()
        for index in sorted(indexes):
            for file in list_file:
                if os.path.basename(file) == index.data():
                    self.logger.info('Remove' + os.path.basename(file))
                    os.remove(file)
        self.load_profile_list()

    def select_profile(self):
        # load all file in config/profile
        list_file = self.profile_ctl.load_file()
        indexes = self.ui.tbv_profile.selectionModel().selectedRows()
        for index in sorted(indexes):
            for file in list_file:
                if os.path.basename(file) == index.data():
                    # list_config = self.profile_ctl.read_config(file)
                    # return config data that read from selected file
                    # return list_config
                    return file

    def update_process(self, success):
        # NOTE: If fail change to string
        print(success)
        self.ui.pg_bar.setValue(int(float(success)))
        if int(float(success)) == 100:
            time.sleep(0.5)
            self.done()

    def update_time(self, time_text):
        self.ui.lbl_time.setText(str(
            time_text.hour) + " : " + str(time_text.minute) + " : " +
            str(time_text.second))

    def done(self):
        self.logger.info("Done")
        self.process_thread.terminate()
        self.time_thread.terminate()
        self.set_page_main()


if __name__ == "__main__":
    working_path = os.path.dirname(os.path.abspath(__file__)) + "/queue"
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Ui()
    sys.exit(app.exec_())
