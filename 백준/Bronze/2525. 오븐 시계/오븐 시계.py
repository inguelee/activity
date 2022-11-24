import datetime
from sys import stdin

A, B = map(int, stdin.readline().split())
C = int(stdin.readline())

time1 = datetime.datetime(2021, 11, 24, A, B)
time2 = datetime.timedelta(minutes=C)

time3 = time1 + time2
print(time3.hour, time3.minute)