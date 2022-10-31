import datetime as dt
H, M = map(int, input().split())
to = dt.datetime(2020, 11, 23, H, M)
m45 = dt.timedelta(minutes=45)
r = to - m45
print(r.hour, r.minute)