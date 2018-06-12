"""Motion"""
import math
def main():
    """Motion"""
    speed = int(input())
    radians = int(input())*(math.pi/180)
    time = (2*speed*math.sin(radians)) / 9.8
    high = ((speed**2) * (math.sin(radians)**2)) / (2*9.8)
    long = ((speed**2) * (math.sin(2*radians)))/9.8
    print("t = %.2f" %time)
    print("H = %.2f" %high)
    print("R = %.2f" %long)
main()
