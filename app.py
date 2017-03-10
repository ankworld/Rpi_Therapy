#!/usr/bin/python3
import sys
import os
import logging
import subprocess
import datetime as dt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep
import controller
import profile
from ui import stack_menu

"""
This main function of this project
"""

__version__ = '0.2'
__author__ = 'Anukul Thienkasemsuk (anukul_thienkasemsuk@hotmail.com)'


# FIXME: Auto start

class ThreadingCounter(QThread):
    limit = 2
    times = 0

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while self.times < self.limit:
            sleep(1)
            self.times += 1
        return True


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
    update_sig = pyqtSignal()

    def __init__(self, control, config):
        QThread.__init__(self)
        self.control = control
        self.config = config

    def __del__(self):
        self.wait()

    def action_1(self):
        finished_round = False
        self.control.motor1.change_duty(100)
        self.control.motor1.cw_drive()
        sleep(0.1)
        self.control.motor1.change_duty(float(self.config[2]))
        while not finished_round:
            print("SensorUp = ", self.control.sensor5.get_value(),
                  " & ", self.control.sensor6.get_value())
            if not self.control.sensor5.get_value() and not self.control.sensor6.get_value():
                self.control.motor1.stop()
                sleep(2)
                self.control.motor1.change_duty(100)
                self.control.motor1.ccw_drive()
                sleep(0.1)
                self.control.motor1.change_duty(float(self.config[2]))
            elif not self.control.sensor3.get_value() and not self.control.sensor4.get_value():
                self.control.motor1.stop()
                sleep(2)
                finished_round = True

    def action_2(self):
        pass

    def run(self):
        self.control.motor1.change_duty(float(self.config[2]))
        self.control.motor2.change_duty(float(self.config[2]))

        for i in range(int(self.config[0])):
            self.action_1()
            self.update_sig.emit()

        for i in range(int(self.config[1])):
            self.action_2()
            self.update_sig.emit()


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

        # Control Variable
        self.cc = controller.Control()
        self.s1_stage = 0
        self.s2_stage = 0

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

        # Manual Control Page
        self.ui.btn_man.clicked.connect(self.set_page_manual)
        self.ui.btn_man_back.clicked.connect(self.set_page_main)
        self.ui.btn_man_s1.clicked.connect(self.cc_s1)
        # self.ui.btn_man_s2.clicked.connect(self.cc_s2)
        self.ui.spb_speed.valueChanged.connect(self.change_speed)

        # Temp Config Button
        self.ui.btn_shutdown.clicked.connect(self.shutdown)

        self.ui.pushButton.clicked.connect(self.terminate_thread)

        self.MainWindow.show()

        self.logger.info("Start System")
        # self.MainWindow.showFullScreen()

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
            self.cc.stop_all()

    # set main page
    # stop all motor and stage to default
    def set_page_main(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.s1_stage = 0
        self.s2_stage = 0
        self.cc.stop_all()

    # set profile page ans load list
    def set_page_profile(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.load_profile_list()

    def set_page_add_profile(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def add_profile(self):
        profile_list = [self.ui.cb_s1.currentText(),
                        self.ui.cb_s2.currentText()]
        speed = self.ui.cb_spd.currentText()
        self.profile_ctl.add(profile_list, speed)
        self.profile_ctl.write_config()
        self.set_page_profile()

    def set_page_manual(self):
        self.cc.motor1.change_duty(self.ui.spb_speed.value())
        self.ui.stackedWidget.setCurrentIndex(3)

    def set_page_process(self):
        # Get profile list that return from select_profile()
        load_profile_list = self.select_profile()
        self.logger.info("Active profile : " +
                         " section 1 " + str(load_profile_list[0]) + "times" +
                         " section 2 " + str(load_profile_list[1]) + "times")
        # Go to next process page when selected profile
        if load_profile_list is not None:
            self.ui.stackedWidget.setCurrentIndex(4)

            # Setup progressbar
            times = int(load_profile_list[0]) + int(load_profile_list[1])
            self.ui.pg_bar.setMaximum(times - 1)
            self.ui.pg_bar.setValue(0)

            # Setup Time Threading
            self.time_thread = ThreadingTime()
            self.time_thread.update_time.connect(self.update_time)
            self.time_thread.start()

            # Setup Process Threading
            self.process_thread = ThreadingProcess(self.cc, load_profile_list)
            self.process_thread.update_sig.connect(self.update_process)
            self.process_thread.finished.connect(self.done)
            self.process_thread.start()

    """
    cc_s1
    working in 4 stage = cw -> stop -> ccw -> stop
    """

    def cc_s1(self):
        if self.s1_stage == 0:
            self.logger.info('Section 1 Manual --> Active --> CW')
            self.cc.motor1.cw_drive()
            self.s1_stage = 1
        elif self.s1_stage == 1:
            self.logger.info('Section 1 Manual --> Active --> CCW')
            self.cc.motor1.ccw_drive()
            self.s1_stage = 0

    def change_speed(self):
        self.cc.motor1.change_duty(self.ui.spb_speed.value())

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
                    list_config = self.profile_ctl.read_config(file)
                    # return config data that read from selected file
                    return list_config

    def update_process(self):
        self.ui.pg_bar.setValue(self.ui.pg_bar.value() + 1)

    def update_time(self, time_text):
        self.ui.lbl_time.setText(str(
            time_text.hour) + " : " + str(time_text.minute) + " : " + str(time_text.second))

    def done(self):
        self.logger.info("Done")
        self.set_page_main()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Ui()
    sys.exit(app.exec_())
