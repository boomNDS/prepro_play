"""Newbie Encoder"""
def main():
    """Newbie Encoder"""
    text = ord(input())
    text = text-(26*(text == 90 or text == 122))
    print(chr(text+1))
main()
