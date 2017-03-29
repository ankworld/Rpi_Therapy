import controller
import time


def main():
    control = controller.Control()

    motor = control.motor1
    motor.change_duty(50)
    motor.cw_drive()
    time.sleep(4)
    motor.ccw_drive()
    time.sleep(4)
    pass


if __name__ == '__main__':
    main()
