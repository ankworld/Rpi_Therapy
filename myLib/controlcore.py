import RPi.GPIO as GPIO


class Motor(object):
    """
    Motor Object --> connect 3 pins, high, low, pwm
    """

    def __init__(self, high_pin, low_pin, pwm_pin, freq):
        GPIO.setwarnings(False)
        self.highPin = high_pin
        self.lowPin = low_pin
        self.pwmPin = pwm_pin
        self.freq = freq
        self.DC = 100

        self.channel = [self.highPin, self.lowPin, self.pwmPin]
        self.chanDrive = [self.highPin, self.lowPin]

        GPIO.setmode(GPIO.BOARD)
        GPIO.getmode()

        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)
        self.p = GPIO.PWM(self.pwmPin, freq)
        self.p.start(self.DC)

    def cw_drive(self):
        GPIO.output(self.chanDrive, (GPIO.HIGH, GPIO.LOW))
        print("cwDrive")

    def ccw_drive(self):
        GPIO.output(self.chanDrive, (GPIO.LOW, GPIO.HIGH))
        print("ccwDrive")

    def change_duty(self, dc):
        print("Current DC : " + str(self.DC))
        self.DC = dc
        self.p.ChangeDutyCycle(self.DC)
        print("New DC : " + str(self.DC))

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
