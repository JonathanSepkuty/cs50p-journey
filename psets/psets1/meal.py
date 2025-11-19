def main():
    user=input("What time is it? ")
    user=convert(user)
    if 7.0<=user<=8.0:
        print("breakfast time")
    elif 12.0<=user<=13.0:
        print("lunch time")
    elif 18.0<=user<=19.0:
        print("dinner time")


def convert(time):
    time=time.replace(":",".")
    hours, minutes=time.split(".")
    hours=float(hours)
    minutes=float(minutes)/60
    time=hours+minutes
    return time

if __name__ == "__main__":
    main()

