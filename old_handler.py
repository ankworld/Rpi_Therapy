import os
import profile
import time
import threading
import configparser
import controller

controller = controller.Control()


# Read work.ini and doing work
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
               controller.sensor4.get_value())
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


# Write Process File
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


# Write Status File
class thread_status(threading):
    def __init__(self, threadID, name, status, command):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        """
        active : inactive(0), active(1)
        command : work(0), terminate(1), delete(2)
        """
        self.cfg = configparser.ConfigParser()
        self.cfg['status'] = {}
        self.cfg['status']['active'] = status
        self.cfg['status']['command'] = command

    def run(self):
        with open(os.path.dirname(os.path.abspath(__file__)) +
                  "/queue/status.ini", 'w') as status_file:
            self.cfg.write(status_file)


# Kill thread_working
class thread_terminate(threading):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cfg = configparser.ConfigParser()

    def run(self):
        pill2kill = threading.Event()
        pass


def main():
    profile_manager = profile.Profile()

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
            status = thread_status(3, "Status Writer", 1, 0)
            time.sleep(5)
            worker.start()
            status.start()
            worker.join()
            os.remove(os.path.dirname(
                os.path.abspath(__file__)) + "/queue/work.ini")
            print("File Deleted")
        else:
            print("Not Found")
            time.sleep(1)


"""
with open(os.path.dirname(os.path.abspath(__file__)) +
          "/queue/status.ini", 'r') as status_file:
    self.cfg.read_file(status_file)

    # status : inactive(0), active(1)
    # command : working(0), terminate(1), delete(2)
    active = self.cfg['status']['active']
    command = self.cfg['status']['command']

    if command == 0:

        pass
    elif command == 1:
        pass
    elif command == 2:
        pass
pass
"""

print("Working at ", os.path.dirname(os.path.abspath(__file__)) +
      "/queue/work.ini")
if __name__ == '__main__':
    main()
