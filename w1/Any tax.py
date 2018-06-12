"""Any tax?"""
def main():
    """Any tax?"""
    moeny = int(input())
    service = moeny*0.1
    vat = (moeny+(moeny*0.1))*0.07
    print(int(moeny+service+vat))
main()
