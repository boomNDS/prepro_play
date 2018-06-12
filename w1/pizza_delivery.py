"""Pizza Delivery"""
def main():
    """Pizza Delivery"""
    long = float(input())*1000
    speed = int(input())
    time = long/speed
    hour = time/3600
    mine = (time%3600)/60
    time = (time%3600)%60
    print("%d Hour(s) %d Minute(s) %d Second(s)" %(hour, mine, time))
main()
