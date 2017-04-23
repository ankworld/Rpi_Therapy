from myLib import controlcore
from time import sleep

motor = controlcore.H_Bridge_Motor(33, 35, 1000)

dc = 100


motor.l_drive()

sleep(20)

# motor.r_drive()
#
# sleep(20)

motor.stop()
