weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ind = 0
while ind < len(weather):
    if weather[ind].isdigit() == True and weather[ind] != '"' or weather[ind].startswith(("-", "+")):
        weather[ind] = weather[ind].zfill(2)
        if weather[ind].startswith(("-", "+")):
            weather[ind] = weather[ind].zfill(3)
        weather.insert(ind, '"')
        weather.insert(ind +2, '"')
        ind += 2
    ind += 1
print(weather)
