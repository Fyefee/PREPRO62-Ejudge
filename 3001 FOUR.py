"""Jeffy Recoding"""
def main(text, num):
    """3001: FOUR"""
    _ = [print("It's not as safe as you think, Mista...") if "4" in text or \
        text.count(num) == 4 else print("MISTA, THIS ONE'S 4 U")]

main(input(), input())
