"""Sleepy"""
def main():
    """Sleepy"""
    time = 10+40+15
    day = 1
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)
    day = time_converter(time, day)

def time_converter(time, day):
    """Time Converter"""
    wakeup_hour = int(input())
    wakeup_min = int(input())
    lazy_level = int(input())
    time += lazy_level*6
    hour = (time//60)
    minu = time%60
    print("[Day %02d] %02d:%02d - %02d:%02d (Time Used: %d Hour(s) %d Minute(s))" \
    %(day, wakeup_hour, wakeup_min, (wakeup_hour+hour)+((wakeup_min+minu)//60), \
    (wakeup_min+minu)%60, hour, minu))
    return day+1

main()
