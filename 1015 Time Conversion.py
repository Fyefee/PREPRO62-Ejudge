"""Jeffy Recoding"""
def main(num):
    """1015 Time Conversion"""
    print("%d hour(s) %d minute(s) %d second(s)."%(num//3600, (num%3600) // 60, num%60))
main(int(input()))
