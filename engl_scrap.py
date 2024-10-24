with open("engl.txt", "r") as file:
    data = [i.strip() for i in file.read().split('\n') if i]
    data[0] = data[0][1:]
dbe = [i.split(', ')  for i in data]
