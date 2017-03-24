import os
import profile
import time
import threading
import configparser
import controller

controller = controller.Control()


class thread_working(threading.Thread):
    def __init__(self, threadID, name, work_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.list = work_list
        print("INIT THREADING")

    def run(self):
        print(self.name, "Threading")
        all_round = int(self.list[0]) + int(self.list[1])
        print("All Round : ", all_round)
        controller.motor1.change_duty(float(self.list[2]))
        controller.motor1.ccw_drive()
        while (controller.sensor3.get_value() and
               controller.sensor4.get_value()):
            pass
        controller.motor1.stop()
        time.sleep(2)
        print("Thread Doing", self.list)
        # Loop in section 1
        for i in range(int(self.list[0])):
            finish = forward = backward = False
            controller.motor1.cw_drive()
            while finish is False:
                if not(controller.sensor5.get_value() or
                       controller.sensor6.get_value()):
                    if forward is False:
                        controller.motor1.stop()
                        time.sleep(1)
                        controller.motor1.ccw_drive()
                        forward = True
                elif forward and not(controller.sensor3.get_value() or
                                     controller.sensor4.get_value()):
                    backward = True
                finish = forward and backward
            print("End Round : ", i)
            self.process = thread_process(
                2, "Process", ((i + 1) / all_round) * 100)
            self.process.start()
            controller.motor1.stop()
            time.sleep(3)
        time.sleep(2)
        controller.motor1.stop()


class thread_process(threading.Thread):
    def __init__(self, threadID, name, process):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.process = process
        self.cfg = configparser.ConfigParser()
        self.cfg['process'] = {}
        self.cfg['process']['success'] = str(self.process)

    def run(self):
        print(self.name, "Threading", self.process)

        with open(os.path.dirname(os.path.abspath(__file__)) +
                  "/queue/process.ini", 'w') as process_file:
            self.cfg.write(process_file)

        time.sleep(2)
        print("FIN")


class thread_status(threading):
    def __init__(self, threadID, name, command):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cfg = configparser.ConfigParser()
        self.cfg['status'] = {}
        self.cfg['status']['active'] = 0
        self.cfg['status']['command'] = command

    def run(self):
        with open(os.path.dirname(os.path.abspath(__file__)) +
                  "/queue/status.ini", 'w') as status_file:
            self.cfg.write(status_file)


def main():
    profile_manager = profile.Profile()

    # TODO: initial position at start point

    """
    check file every 1 second for get job
    """
    while 1:
        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) +
                          "/queue/work.ini"):
            work_list = profile_manager.read_config(
                os.path.dirname(os.path.abspath(__file__)) +
                "/queue/work.ini")
            worker = thread_working(1, "Worker", work_list)
            time.sleep(5)
            worker.start()
            worker.join()
            os.remove(os.path.dirname(
                os.path.abspath(__file__)) + "/queue/work.ini")
            print("File Deleted")
        else:
            print("Not Found")
            time.sleep(1)


print("Working at ", os.path.dirname(os.path.abspath(__file__)) +
      "/queue/work.ini")
if __name__ == '__main__':
    main()
