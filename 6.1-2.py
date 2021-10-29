pars = []
spam = {}
with open("nginx_logs.txt", "r", encoding="utf-8") as a:
    for line in a:
        line = line.split()
        ip = line[0]
        spam.setdefault(ip, 0)
        spam[ip] +=1
        pars.append((ip, line[5][1:], line[6]))
print(pars)
print(max(spam, key=spam.get))