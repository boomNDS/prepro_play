"""Count Fast!"""
def main():
    """Count Fast!"""
    num = 1
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)
    num = again(num)

def count_sir(name, num):
    """format"""
    return name+":"+str(num)+"#"

def again(num):
    """get name and print"""
    name1 = input()
    name2 = input()
    name3 = input()
    name4 = input()
    name5 = input()
    print(count_sir(name1, num), end="\t\t")
    print(count_sir(name2, num+1), end="\t\t")
    print(count_sir(name3, num+2), end="\t\t")
    print(count_sir(name4, num+3), end="\t\t")
    print(count_sir(name5, num+4))
    return num+5
main()
