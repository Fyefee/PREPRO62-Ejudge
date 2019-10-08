"""Jeffy Recoding"""
def main(num1, num2, num3, num4, num5):
    """1014: Secret Code"""
    print("%s+%s+%s+%s+%s = %s"%(num1 % 10, num2 % 100 // 10, num3 % 1000 // 100, \
        num4 % 10000 // 1000, num5 % 100000 // 10000, num1 % 10 + num2 % 100 // 10 + \
            num3 % 1000 // 100 + num4 % 10000 // 1000 + num5 % 100000 // 10000))
main(int(input()), int(input()), int(input()), int(input()), int(input()))
