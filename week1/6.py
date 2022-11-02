x, y, w, h = map(int, input().split())

if w/2 >= x :
    x_min = x
else :
    x_min = w - x

if h/2 >= y :
    y_min = y
else :
    y_min = h - y

if x_min > y_min :
    print(y_min)
else : 
    print(x_min)

