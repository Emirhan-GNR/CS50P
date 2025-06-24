def main():

    t = input("What time is it? ")
    time_hour = convert(t)

    if 7 <= time_hour <= 8:
        print("breakfast time")
    elif 12 <= time_hour <= 13:
        print("lunch time")
    elif 18 <= time_hour <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    return int(hour) + int(minute) / 60

if __name__ == "__main__":
    main()