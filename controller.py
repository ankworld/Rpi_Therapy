import setting
from lib import controlcore


class Control(object):
    """
    Set up motors
    """

    def __init__(self):
        cfg = setting.Config()

        pin_motor1 = cfg.read_config_file("Motor 1")
        pin_motor2 = cfg.read_config_file("Motor 2")

        pin_sensor = cfg.read_config_sensor("Sensor")

        self.motor1 = controlcore.Motor(
            pin_motor1[0], pin_motor1[1], pin_motor1[2], pin_motor1[3])
        self.motor2 = controlcore.Motor(
            pin_motor2[0], pin_motor2[1], pin_motor2[2], pin_motor2[3])

        self.sensor1 = controlcore.Sensor(pin_sensor[0])
        self.sensor2 = controlcore.Sensor(pin_sensor[1])
        self.sensor3 = controlcore.Sensor(pin_sensor[2])
        self.sensor4 = controlcore.Sensor(pin_sensor[3])
        self.sensor5 = controlcore.Sensor(pin_sensor[4])
        self.sensor6 = controlcore.Sensor(pin_sensor[5])

    def stop_all(self):
        self.motor1.stop()
        self.motor2.stop()
