while True:
    try:
        fraction=input("Fraction: ")
        x, y= fraction.split("/")
        x=int(x)
        y=int(y)
        if y==0 or x>y or x<0:
            continue
        fuel=round(x/y*100)
        break
    except (ValueError,ZeroDivisionError):
            continue
if fuel>=99:
    print("F")
elif fuel<=1:
    print("E")
else:
    print(f"{fuel}%")
