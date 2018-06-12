"""Energy"""
def main():
    """Energy"""
    long = float(input())*1000
    energy = int(input())*10
    # print("long %f \nEnergy %d" %(long, Energy))
    # print(long%Energy > 0)
    print(int(long/energy)+((long/energy)%1 > 0))
main()
