"""Health Check"""
def main():
    """Health Check"""
    height1 = float(input())
    most = height1
    low = height1
    total = height1
    height2 = float(input())
    most = max(height2, most)
    low = min(height2, low)
    total += height2
    height3 = float(input())
    most = max(height3, most)
    low = min(height3, low)
    total += height3
    height4 = float(input())
    most = max(height4, most)
    low = min(height4, low)
    total += height4
    height5 = float(input())
    most = max(height5, most)
    low = min(height5, low)
    total += height5
    print("The Tallest is %.1f" %most)
    print("The Shortest is %.1f" %low)
    print("Average is %.1f" %(total/5))

main()
