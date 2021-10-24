from pynput.keyboard import Key, Controller
import timeit
import time as time
import threading
import sys

counter_w = 0
counter_s = 0


def print_time():
    seconds = 0
    minutes = 0
    print("Running for:")
    while True:

        print("\r" + str(minutes) + " minutes and " +  str(seconds) + " seconds" ,end="")
        time.sleep(1)
        seconds+=1

        if seconds == 60:
            seconds = 0
            minutes +=1





def start_time():
    t1 = threading.Thread(target=print_time)
    t1.start()


def run_forward():
    global counter_w
    keyboard = Controller()
    key = "w"

    keyboard.press(key)
    time.sleep(1)
    keyboard.release(key)
   # print('W press')

    if counter_w >= 5:
        counter_w = 0
        time.sleep(10)
    else:
        counter_w+=1

def run_backward():
    global counter_s
    keyboard = Controller()
    key = "s"

    keyboard.press(key)
    time.sleep(3)
    keyboard.release(key)
    #print('S press')

    if counter_s >= 10:
        counter_s == 0
        time.sleep(8)

    else:
        counter_s +=1




if __name__ == "__main__":
    print('*'*30)
    print('Starting Auto Run...')
    print('*' * 30)
    start_time()
    while True:
        run_forward()
        run_backward()


