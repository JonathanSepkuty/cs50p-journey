months_list=[
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
    try:
        date=input("Date: ").strip()
        if "/" in date:
            month,day,year=date.split("/")
            day=int(day)
            month=int(month)
        else:
            month_word, day, year=date.split(" ")
            if "," in date:
                day=int(day.replace(",",""))
                month= months_list.index(month_word) +1
            else:
                continue
        if 1<=day<=31 and 1<=month<=12:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue
    except (ValueError, IndexError):
        continue




