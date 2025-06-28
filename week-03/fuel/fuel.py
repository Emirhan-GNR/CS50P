while True:
    try:
        x , y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        fraction = round(x/y*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if fraction <= 1:
            print("E")
        elif fraction >= 99:
            print("F")
        else:
            print(f"{fraction}%")
        break