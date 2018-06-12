"""Number Digits"""
def main():
    """Number Digits"""
    num1, num2 = int(input()), int(input())
    num3, num4, num5 = int(input()), int(input()), int(input())
    num1 = int(num1 % 10)
    num2 = int((num2%100)/10)
    num3 = int((num3%1000)/100)
    num4 = int((num4%10000)/1000)
    num5 = int((num5%100000)/10000)
    total = num1+num2+num3+num4+num5
    print("%d+%d+%d+%d+%d = %d" %(num1, num2, num3, num4, num5, total))
main()
