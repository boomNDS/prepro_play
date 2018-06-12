import math
"""Germany Trip"""
def main():
    """Germany Trip"""
    total = 0
    a_x,a_y = int(input()), int(input())
    b_x,b_y = int(input()), int(input())
    c_x,c_y = int(input()), int(input())
    d_x,d_y = int(input()), int(input())
    f_x,f_y = int(input()), int(input())
    total += dis(a_x,a_y,b_x,b_y)
    total += dis(b_x,b_y,c_x,c_y)
    total += dis(c_x,c_y,d_x,d_y)
    total += dis(d_x,d_y,f_x,f_y)
    print(round(total))
def dis(num_x1,num_y1,num_x2,num_y2):
    return math.sqrt((num_x1-num_x2)**2 + (num_y1-num_y2)**2)
main()
