import controller
import time

cc = controller.Control()

while 1:
    print("TOP - Left -> Sensor1", cc.sensor1.get_value())
    print("TOP - Right -> Sensor2", cc.sensor2.get_value())
    print("**\n\n")
    print("(Front) -> Sensor3 :", cc.sensor3.get_value())
    print("(Front) -> Sensor4 :", cc.sensor4.get_value())
    print("(BACK) -> Sensor5 :", cc.sensor5.get_value())
    print("(BACK) -> Sensor6 :", cc.sensor6.get_value())
    print("**\n\n")
    time.sleep(1)
