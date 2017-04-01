import threading
import time


def main():
    t1_stop = threading.Event()
    t1 = threading.Thread(target=thread1, args=(1, t1_stop))

    t2_stop = threading.Event()
    t2 = threading.Thread(target=thread2,  args=(2, t2_stop))
    t1.start()
    t2.start()
    time.sleep(2)
    # stop the thread2
    t2_stop.set()


def thread1(arg1, stop_event):
    while(not stop_event.is_set()):
        print("Before 1")
        # similar to time.sleep()
        stop_event.wait(5)
        print("After 1")
        pass


def thread2(arg1, stop_event):
    while(not stop_event.is_set()):
        print("Before 2")
        stop_event.wait(5)
        print("After 2")
        pass


if __name__ == '__main__':
    main()
