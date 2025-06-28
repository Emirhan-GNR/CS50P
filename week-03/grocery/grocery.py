def main():
    items = {}

    try:
        while True:
            x = input().strip().lower()
            if x in items:
                items[x] += 1
            else:
                items[x] = 1
    except EOFError:
        pass

    print()
    for x in sorted(items.keys()):
        print(f"{items[x]} {x.upper()}")
main()