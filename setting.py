import sys
import configparser
import re
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QGroupBox
from ui import controlpanel


class Config(object):
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.list_of_value = []

    def write_config_file(self, section, options):
        cfg = configparser.ConfigParser()
        cfg.read(self.path + '/config/motor.ini')
        cfg[section] = {}
        cfg[section]['high_pin'] = options[0]
        cfg[section]['low_pin'] = options[1]
        cfg[section]['pwm_pin'] = options[2]
        cfg[section]['freq'] = options[3]

        with open(self.path + '/config/motor.ini', 'w') as configfile:
            cfg.write(configfile)

    def write_config_sensor(self, section, options):
        cfg = configparser.ConfigParser()
        cfg.read(self.path + '/config/sensor.ini')
        cfg[section] = {}
        cfg[section]['input_1'] = options[0]
        cfg[section]['input_2'] = options[1]
        cfg[section]['input_3'] = options[2]
        cfg[section]['input_4'] = options[3]
        cfg[section]['input_5'] = options[4]
        cfg[section]['input_6'] = options[5]

        with open(self.path + '/config/sensor.ini', 'w') as configfile:
            cfg.write(configfile)

    def read_config_file(self, section):
        self.list_of_value = []
        cfg = configparser.ConfigParser()
        cfg.read(self.path + '/config/motor.ini')
        try:
            for option in cfg[section].values():
                if option != "":
                    self.list_of_value.append(int(float(option)))
                else:
                    self.list_of_value.append(0)
        except KeyError:
            pass
        return self.list_of_value

    def read_config_sensor(self, section):
        self.list_of_value = []
        cfg = configparser.ConfigParser()
        cfg.read(self.path + '/config/sensor.ini')
        try:
            for option in cfg[section].values():
                if option != "":
                    self.list_of_value.append(int(float(option)))
                else:
                    self.list_of_value.append(0)
        except KeyError:
            pass
        return self.list_of_value


class Ui(object):
    def __init__(self):

        self.list_used_pin = []

        self.high_pin = 0
        self.low_pin = 0
        self.pwm_pin = 0
        self.freq = 0

        self.window = QMainWindow()
        self.uic = controlpanel.Ui_ControlPanelMW()
        self.uic.setupUi(self.window)

        self.load()

        self.uic.saveMotor1.clicked.connect(self.save)
        self.uic.saveMotor2.clicked.connect(self.save)
        self.uic.saveSensor.clicked.connect(self.save_sensor)
        self.uic.saveAll.clicked.connect(self.save_all)
        self.uic.loadAll.clicked.connect(self.load)
        self.window.show()

    def unique_pin(self):
        self.list_used_pin = []
        self.list_used_pin.append(self.uic.highPinM1.text())
        self.list_used_pin.append(self.uic.highPinM2.text())
        self.list_used_pin.append(self.uic.lowPinM1.text())
        self.list_used_pin.append(self.uic.lowPinM2.text())
        self.list_used_pin.append(self.uic.pwmPinM1.text())
        self.list_used_pin.append(self.uic.pwmPinM2.text())
        self.list_used_pin.append(self.uic.input1.text())
        self.list_used_pin.append(self.uic.input2.text())
        self.list_used_pin.append(self.uic.input3.text())
        self.list_used_pin.append(self.uic.input4.text())
        self.list_used_pin.append(self.uic.input5.text())
        self.list_used_pin.append(self.uic.input6.text())
        print(len(self.list_used_pin))
        print(len(set(self.list_used_pin)))
        if len(self.list_used_pin) > len(set(self.list_used_pin)):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error : Duplicate Pin")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return False
        else:
            return True

    def save(self):

        if self.unique_pin():
            sender = self.window.sender()
            list_of_line_edit = sender.parent().findChildren(QLineEdit)

            section = sender.parent().title()
            for item in list_of_line_edit:
                reg_name = re.sub(r'\w\d', r'', item.objectName())

                if reg_name == "highPin":
                    self.high_pin = item.text()
                elif reg_name == "lowPin":
                    self.low_pin = item.text()
                elif reg_name == "pwmPin":
                    self.pwm_pin = item.text()
                elif reg_name == "freqPin":
                    self.freq = item.text()

            list_of_pin = [self.high_pin,
                           self.low_pin, self.pwm_pin, self.freq]
            Config().write_config_file(section, list_of_pin)

    def save_sensor(self):
        if self.unique_pin():
            section = "Sensor"
            list_of_input = [self.uic.input1.text(), self.uic.input2.text(), self.uic.input3.text(),
                             self.uic.input4.text(), self.uic.input5.text(), self.uic.input6.text()]
            Config().write_config_sensor(section, list_of_input)

    def load(self):

        name_gb = []
        for gb in self.uic.centralwidget.findChildren(QGroupBox):
            name_gb.append(gb.objectName())

        name_gb.sort()

        i = 0
        sorted_gb = []
        while i < 2:
            for gb in self.uic.centralwidget.findChildren(QGroupBox):
                if gb.objectName() == name_gb[i]:
                    sorted_gb.append(gb)
                    i += 1
                    break

        section = ""
        for i in range(2):
            section = "Motor " + str(i + 1)

            value = Config().read_config_file(section)

            if len(value) == 0:
                pass
            else:
                gb = sorted_gb[i]

                list_of_line_edit = gb.findChildren(QLineEdit)
                for item in list_of_line_edit:
                    reg_name = re.sub(r'\w\d', r'', item.objectName())

                    if reg_name == "highPin":
                        item.setText(str(value[0]))
                    elif reg_name == "lowPin":
                        item.setText(str(value[1]))
                    elif reg_name == "pwmPin":
                        item.setText(str(value[2]))
                    elif reg_name == "freqPin":
                        item.setText(str(value[3]))
##########################################################################
        # Load to sensor section
        section = "Sensor"
        value = Config().read_config_sensor(section)
        if len(value) == 0:
            pass
        else:
            self.uic.input1.setText(str(value[0]))
            self.uic.input2.setText(str(value[1]))
            self.uic.input3.setText(str(value[2]))
            self.uic.input4.setText(str(value[3]))
            self.uic.input5.setText(str(value[4]))
            self.uic.input6.setText(str(value[5]))

    def save_all(self):
        self.uic.saveMotor1.click()
        self.uic.saveMotor2.click()
        self.uic.saveSensor.click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Ui()
    sys.exit(app.exec_())
