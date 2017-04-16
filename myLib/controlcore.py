import RPi.GPIO as GPIO


class Motor(object):
    """
    Motor Object --> connect 3 pins, high, low, pwm
    """

    def __init__(self, l_pin, r_pin, freq):
        GPIO.setwarnings(False)
        self.l_pin = l_pin
        self.r_pin = r_pin
        self.freq = freq
        self.l_dc = 0
        self.r_dc = 0

        self.channel = [self.l_pin, self.r_pin]

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)
        self.pl = GPIO.PWM(self.l_pin, freq)
        self.pl.start(self.l_dc)

        self.pr = GPIO.PWM(self.r_pin, freq)
        self.pr.start(self.r_dc)

    def r_drive(self, dc=None):
        if dc is None:
            dc = self.r_dc
            self.pl.ChangeDutyCycle(0)
            self.pr.ChangeDutyCycle(dc)
        else:
            self.pl.ChangeDutyCycle(0)
            self.pr.ChangeDutyCycle(dc)
        print("-->> Drive")

    def l_drive(self, dc=None):
        if dc is None:
            dc = self.l_dc
            self.pl.ChangeDutyCycle(dc)
            self.pr.ChangeDutyCycle(0)
        else:
            self.pl.ChangeDutyCycle(dc)
            self.pr.ChangeDutyCycle(0)
        print("<<-- Drive")

    def change_duty(self, dc):
        print("Current LDC : " + str(self.l_dc))
        self.l_dc = dc
        print("New LDC : " + str(self.l_dc))
        print("Current RDC : " + str(self.r_dc))
        self.r_dc = dc
        print("New RDC : " + str(self.r_dc))

    def l_change_duty(self, dc):
        print("Current LDC : " + str(self.l_dc))
        self.l_dc = dc
        print("New LDC : " + str(self.l_dc))

    def r_change_duty(self, dc):
        print("Current RDC : " + str(self.r_dc))
        self.r_dc = dc
        print("New RDC : " + str(self.r_dc))

    def change_freq(self, freq):
        print("Current Freq : " + self.freq)
        self.freq = freq
        self.pl.ChangeFrequency(self.freq)
        self.pr.ChangeFrequency(self.freq)
        print("New Freq : " + self.freq)

    def stop(self):
        print("Stop motor")
        self.pl.ChangeDutyCycle(0)
        self.pr.ChangeDutyCycle(0)


class H_Bridge_Motor(object):
    """
    Motor Object --> connect 3 pins, high, low, pwm
    """

    def __init__(self, high_pin, low_pin, freq):
        GPIO.setwarnings(False)
        self.highPin = high_pin
        self.lowPin = low_pin
        self.freq = freq
        self.DC = 100

        self.channel = [self.highPin, self.lowPin]
        self.chanDrive = [self.highPin, self.lowPin]

        GPIO.setmode(GPIO.BOARD)
        GPIO.getmode()

        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)

    def l_drive(self):
        GPIO.output(self.chanDrive, (GPIO.HIGH, GPIO.LOW))
        print("cwDrive")

    def r_drive(self):
        GPIO.output(self.chanDrive, (GPIO.LOW, GPIO.HIGH))
        print("ccwDrive")

    def change_freq(self, freq):
        print("Current Freq : " + self.freq)
        self.freq = freq
        self.p.ChangeFrequency(self.freq)
        print("New Freq : " + self.freq)

    def stop(self):
        print("Stop motor")
        GPIO.output(self.chanDrive, (GPIO.LOW, GPIO.LOW))


class Sensor(object):
    def __init__(self, sensor_pin):
        self.sensor_pin = sensor_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor_pin, GPIO.IN)

    def get_value(self):
        return GPIO.input(self.sensor_pin)
