"""Restaurant"""
def main():
    """Restaurant"""
    moeny = int(input())
    service = moeny*0.1
    vat = moeny*0.07
    print("Service Charge : %.2f Baht" %service)
    print("VAT : %.2f Baht" %vat)
    print("Total : %.2f Baht" %(moeny+vat+service))
main()
