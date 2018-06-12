"""Time Converter"""
def main():
    """Time Converter"""
    time = int(input())
    print(time//3600, "Hour(s)", end=" ")
    print(time%3600//60, "Minute(s)", end=" ")
    print(time%3600%60, "Second(s)", end=" ")
main()
