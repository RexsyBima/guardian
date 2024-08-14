import datetime

now = datetime.datetime.now()
print(now, type(now))
# string format time
print(now.strftime("%d/%B/%Y %H:%M:%S"))
