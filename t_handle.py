import os
import sys
import profile
import time
import threading
import configparser
import controller

controller = controller.Control()
working_path = os.path.dirname(os.path.abspath(__file__)) + "/queue"


class SignalHandler:
    """
    The object that will handle signals and stop the worker threads.
    """

    #: The stop event that's shared by this handler and threads.
    stopper = None

    #: The pool of worker threads
    workers = None

    def __init__(self, stopper, workers):
        self.stopper = stopper
        self.workers = workers

    def __call__(self, signum, frame):
        """
        This will be called by the python signal module

        https://docs.python.org/3/library/signal.html#signal.signal
        """
        self.stopper.set()

        for worker in self.workers:
            worker.join()

        sys.exit(0)


class StatusChecker(threading.Thread):
    """
    The thread that will check HTTP statuses.
    """

    #: An event that tells the thread to stop
    stopper = None

    def __init__(self, worker, stopper):
        super().__init__()
        self.worker = worker
        self.stopper = stopper

    def run(self):
        while not self.stopper.is_set():
            if self.worker.isAlive():
                pass
            else:
                pass


class thread_working(threading.Thread):
    def __init__(self, threadID, name, work_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.work_list = []
        print("INIT THREADING")
        self.profile_manager = profile.Profile()

    def run(self):
        if os.path.exists(working_path + "/work.ini"):
            self.work_list = self.profile_manager.read_config(working_path +
                                                              "/work.ini")
        print(self.name, "Threading")
        all_round = int(self.work_list[0]) + int(self.work_list[1])
        print("All Round : ", all_round)
        controller.motor1.change_duty(float(self.work_list[2]))
        controller.motor1.ccw_drive()
        while (controller.sensor3.get_value() and
               controller.sensor4.get_value()):
            pass
        controller.motor1.stop()
        time.sleep(2)
        print("Thread Doing", self.work_list)
        # Loop in section 1
        for i in range(int(self.work_list[0])):
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


def main():
    last_command = 100
    cfg = configparser.ConfigParser()
    stopper = threading.Event()

    while 1:
        with open(working_path + "/status.ini", 'r') as status_file:
            cfg.read_file(status_file)
        active = cfg['status']['active']
        new_command = cfg['status']['command']

        if new_command != last_command:
            if new_command == 0:
                working = thread_working(threadID=1, name="work")
                worker = StatusChecker(worker=working, stopper=stopper)
                worker.start()
            elif new_command == 1:
                if active:
                    stopper.set()
            elif new_command == 2:
                stopper.clear()
                if os.path.exists(working_path + "/work.ini"):
                    os.remove(working_path + "/work.ini")
                    os.remove(working_path + "/process.ini")

            last_command = new_command
