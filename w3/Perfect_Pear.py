"""Perfect Pear"""
def main():
    """Perfect Pear"""
    pear1 = int(input())
    pear2 = int(input())
    pear3 = int(input())
    most = max(max(pear1, pear2), pear3)
    low = min(min(pear1, pear2), pear3)
    perfect = pear1+pear2+pear3-low-most
    print(perfect)
main()
