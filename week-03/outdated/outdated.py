months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    if "/" in date:
        
        try:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04}-{m:02}-{d:02}")
                break

        except:
            continue

    elif "," in date:

        try:
            first_part, year = date.split(",")
            parts = first_part.strip().split(" ")

            if len(parts) != 2:
                continue

            month_name = parts[0]
            day = int(parts[1])
            year = int(year.strip())

            if month_name in months and 1 <= day <= 31:
                month_num = months.index(month_name) + 1
                print(f"{year:04}-{month_num:02}-{day:02}")
                break

        except:
            continue