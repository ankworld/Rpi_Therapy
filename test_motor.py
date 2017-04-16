from myLib import controlcore
from time import sleep

motor = controlcore.Motor(11, 13, 1000)

dc = 100


for i in range(10):
    motor.l_drive(dc)

    sleep(5)

    motor.r_drive(dc)

    sleep(5)
