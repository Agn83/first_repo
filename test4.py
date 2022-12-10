import datetime
import time

today = datetime.date.today()
print(type(today))
print(today)
data1= today.strftime("Dzisiaj jest %d dzień ..... %m miesiąca")
data2= today.strftime("%d--%m--%y")
print(data2)
print(data1)

now = datetime.datetime.now()
print(type(now))

print(now)

for i in range (10):
    name = "raport.txt"
    my_now = now.strftime("%H:%M:%S")
    print(name[:6] + my_now + name[-4:])
    time.sleep(2)
