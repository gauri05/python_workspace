import schedule
import time
import datetime
def fun_Minute():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular excucted after Minute")
def fun_Hour():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular excucted after Hour")
def fun_Day():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular excucted after Day")
def fun_Afternoon():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular excucted at 12")
def main():
    print("Python task Schedular")
    print(datetime.datetime.now())
    schedule.every(1).minute.do(fun_Minute)
    schedule.every().hour.do(fun_Hour)
    schedule.every().day.at("20:18").do(fun_Day)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
