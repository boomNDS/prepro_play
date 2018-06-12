"""Sort"""
def main():
    """Sort"""
    num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
    num1, num2 = max(num1, num2), min(num1, num2)
    num1, num3 = max(num1, num3), min(num1, num3)
    num1, num4 = max(num1, num4), min(num1, num4)
    num2, num4 = max(num2, num4), min(num2, num4)
    num2, num3 = max(num2, num3), min(num2, num3)
    num3, num4 = max(num3, num4), min(num3, num4)
    print(num1)
    print(num2)
    print(num3)
    print(num4)
main()
