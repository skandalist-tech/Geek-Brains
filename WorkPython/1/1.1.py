duration = int(input("Введите время в секундах : "))
second = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // 86400
print("дней:", days, "часов:", hours, "минут:", minutes, "секунд:", second)
