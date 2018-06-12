"""Election Chance"""
def main():
    """Election Chance"""
    prob = float(input())/100
    year = int(input())-2018
    result = max(int((1 - (prob*year))*100), 0)
    print("%d %%" %result)
main()
