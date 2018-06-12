"""Bank Notes"""
def main():
    """Bank Notes"""
    moeny = int(input())
    print(moeny//1000)
    moeny %= 1000
    print(moeny//500)
    moeny %= 500
    print(moeny//100)
    moeny %= 100
    print(moeny//50)
    moeny %= 50
    print(moeny//20)
    moeny %= 20
    print(moeny//10)
main()
