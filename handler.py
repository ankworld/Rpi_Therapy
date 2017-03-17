import os
import profile
import time
import threading
import configparser


class thread_working(threading.Thread):
    def __init__(self, threadID, name, work_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.list = work_list

    def run(self):
        print("Thread Doing", self.list)
        for i in range(10):
            self.next_thread = thread_process(2, "Process", i)
            self.next_thread.start()
            self.next_thread.join()
            print("FIN NEXT", i)
        time.sleep(2)


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
        print("Process Thread", self.process)

        with open(os.path.dirname(os.path.abspath(__file__)) +
                  "/queue/process.ini", 'w') as process_file:
            self.cfg.write(process_file)

        time.sleep(2)
        print("FIN")


def main():
    profile_manager = profile.Profile()
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
        else:
            print("Not Found")
            time.sleep(1)
        # break


print("Working at ", os.path.dirname(os.path.abspath(__file__)) +
      "/queue/work.ini")
if __name__ == '__main__':
    main()

# exitFlag = 0
#
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print("Exiting " + self.name)
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Exiting Main Thread")
