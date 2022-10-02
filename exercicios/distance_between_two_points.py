from math import sqrt


x1 = round(int(input()),1)
y1 = round(int(input()),1)

x2 = round(int(input()),1)
y2 = round(int(input()),1)

print(f"{round((sqrt(((x2-x1)**2)+((y2-y1)**2))),4)}")