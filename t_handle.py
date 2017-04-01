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
        self.worker.start()
        while not self.stopper.is_set():
            print(self.stopper.is_set())
            if self.worker.isAlive():
                time.sleep(0.5)
            else:
                self.stopper.set()


class thread_working(threading.Thread):
    def __init__(self, threadID, name, stopper):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.work_list = []
        self.stopper = stopper
        print("INIT THREADING")
        self.profile_manager = profile.Profile()

    def run(self):
        self.process = thread_process(
            2, "Process", 0)
        self.process.start()
        self.process.join()
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
            if self.stopper.is_set():
                controller.motor1.stop()
                controller.motor2.stop()
                break
        controller.motor1.stop()
        time.sleep(1)
        print("Thread Doing", self.work_list)
        # Loop in section 1
        for i in range(int(self.work_list[0])):
            if self.stopper.is_set():
                controller.motor1.stop()
                controller.motor2.stop()
                break
            finish = forward = backward = False
            controller.motor1.change_duty(float(self.work_list[2]))
            controller.motor1.cw_drive()
            while finish is False:
                if self.stopper.is_set():
                    controller.motor1.stop()
                    controller.motor2.stop()
                    break
                if not(controller.sensor5.get_value() or
                       controller.sensor6.get_value()):
                    if forward is False:
                        controller.motor1.stop()
                        time.sleep(1)
                        # controller.motor1.change_duty(100)
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
        # time.sleep(1)
        controller.motor1.stop()
        # Loop in section 2
        if int(self.work_list[1]) > 0:
            controller.motor2.change_duty(100)
            controller.motor2.ccw_drive()
            while (controller.sensor1.get_value()):
                if self.stopper.is_set():
                    controller.motor1.stop()
                    controller.motor2.stop()
                    break
            controller.motor2.stop()
            time.sleep(1)
            for i in range(int(self.work_list[1])):
                if self.stopper.is_set():
                    controller.motor1.stop()
                    controller.motor2.stop()
                    break
                finish = forward = backward = False
                # controller.motor2.change_duty(100)
                controller.motor2.cw_drive()
                while finish is False:
                    if self.stopper.is_set():
                        controller.motor1.stop()
                        controller.motor2.stop()
                        break
                    if not(controller.sensor1):
                        if forward is False:
                            controller.motor2.stop()
                            time.sleep(1)
                            controller.motor2.ccw_drive()
                            forward = True
                    elif forward and not(controller.sensor2.get_value()):
                        backward = True
                    finish = forward and backward

                print("End Round : ", i)
                self.process = thread_process(
                    2, "Process", ((i + 1) / all_round) * 100)
                self.process.start()
                controller.motor2.stop()
                time.sleep(3)
            # time.sleep(1)
            controller.motor2.stop()
        if os.path.exists(working_path + "/work.ini"):
            os.remove(working_path + "/work.ini")
        if os.path.exists(working_path + "/process.ini"):
            os.remove(working_path + "/process.ini")
        if os.path.exists(working_path + "/status.ini"):
            cfg = configparser.ConfigParser()
            with open(working_path + "/status.ini", 'r') as process_file:
                cfg.read_file(process_file)
            cfg['status']['active'] = str(0)
            cfg['status']['command'] = str(1)
            with open(working_path + "/status.ini", 'w') as status_file:
                cfg.write(status_file)


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
    if os.path.exists(working_path + "/status.ini"):
        pass
    else:
        cfg['status'] = {}
        cfg['status']['active'] = str(0)
        cfg['status']['command'] = str(100)
        with open(working_path + "/status.ini", 'w') as status_file:
            cfg.write(status_file)
    stopper = threading.Event()

    while 1:
        if os.path.exists(working_path + "/status.ini"):
            with open(working_path + "/status.ini", 'r') as status_file:
                cfg.read_file(status_file)
            active = cfg['status']['active']
            new_command = cfg['status']['command']

            if new_command != last_command:
                if new_command == '0':
                    print("Working")
                    stopper.clear()
                    working = thread_working(threadID=1, name="work",
                                             stopper=stopper)
                    working.start()
                    # worker = StatusChecker(worker=working, stopper=stopper)
                    # worker.start()
                elif new_command == '1':
                    if active:
                        print("Terminate")
                        stopper.set()
                elif new_command == '2':
                    print("Reset")
                    stopper.clear()
                    if os.path.exists(working_path + "/work.ini"):
                        os.remove(working_path + "/work.ini")
                        os.remove(working_path + "/process.ini")

                last_command = new_command
            time.sleep(0.5)
        else:
            cfg['status'] = {}
            cfg['status']['active'] = str(0)
            cfg['status']['command'] = str(100)
            with open(working_path + "/status.ini", 'w') as status_file:
                cfg.write(status_file)


if __name__ == '__main__':
    main()
