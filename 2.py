times = int(input("Введите время в секундах: "))
sec =(times % 60)
hours = times // 3600
minuts = (times // 60) % 60
print("Время в формате чч:мм:сс: {}:{}:{}".format(hours, minuts, sec))