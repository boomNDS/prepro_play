"""Functions"""
def main():
    """Functions"""
    total = 0
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total *= 0.90
    print("Total : %.2f Baht" %total)

def promotion(drink, cake):
    """return price"""
    return (drink+cake)*0.80
main()
