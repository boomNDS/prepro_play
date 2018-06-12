"""Is This Calculus?"""
def main():
    """Is This Calculus?"""
    numa, numb = float(input()), float(input())
    numb, numa = max(numa, numb), min(numa, numb)
    print("%.2f" %(round((((numb**3) / 3) +numb) - (((numa**3)/3)+numa), 2)))
main()
