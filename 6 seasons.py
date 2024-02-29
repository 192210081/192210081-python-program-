def find_season(month, day):
    seasons = [("Mar", 20, "Spring"), ("Jun", 21, "Summer"), ("Sep", 22, "Fall"), ("Dec", 21, "Winter")]
    for i in range(len(seasons)):
        if (month == seasons[i][0] and day >= seasons[i][1]) or (month > seasons[i][0]):
            return seasons[i][2]
    return "Winter"

month = input("Enter the month (e.g., Jan, Feb, Mar): ").capitalize()
day = int(input("Enter the day: "))
season = find_season(month, day)
print(f"The season for {month} {day} is {season}.")
