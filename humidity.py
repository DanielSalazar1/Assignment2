humidity = input("Please input humidity value: ")
humidity = int(humidity)
if humidity < 30:
    print("Dry")
elif normal_humidity > 60:
    print("Hight humidity")
else:
    print("ok")
