import numpy as np

def check_next_day(day, n):
    dayAWeek = np.array(["Mon", "Tues", "Wed", "Thus", "Fri", "Sat", "Sun"]*(n+1))
    nextDays = []
    for index in range(len(dayAWeek)):
        if day == dayAWeek[index]:
            nextDays.append(dayAWeek[index+1:index+n+1])
    return nextDays

def signal():
    signal = {}
    signalFile = open("kyhieu.txt", "r")
    lines = signalFile.readlines()
    for line in lines:
        splittedLine = line.split(":")
        signal[splittedLine[0]] = splittedLine[1].strip()
    signalFile.close()
    return signal

def date_and_signal():
    days = []
    weathers = []
    file = open("dubaothoitiet.txt", "r")
    lines = file.readlines()
    for line in lines:
        splittedLine = line.split(":")
        days.append(splittedLine[0])
        weathers.append(splittedLine[1].strip())
    file.close()
    return days, weathers

if __name__ == "__main__":
    now = ""
    while  "-" not in now:
        now  = input("To day is: ")
    dayOfWeek = now.split("-")[0].capitalize()
    date = now.split("-")[1]

    nextdayAmount = int(input("Enter next-day numbers to check weather:  "))
    days, weathers = date_and_signal()
    # print(date)
    signals = signal()
    dayOfWeekeek = check_next_day(dayOfWeek, nextdayAmount)
    for dateD in days:
        if dateD != date:
            print("No information to check!")
        break
    for index in range(len(days)):
        # print(days[index])
        if date == days[index]:
            nextDays = days[index+1:index+nextdayAmount+1]
            print(f"Weather forcast for {nextdayAmount} days: ")
            for i in range(len(nextDays)):
                # print(len(day_of_week))
                print(f"{dayOfWeekeek[i][i]} - {nextDays[i]}: {signals[weathers[index+i+1]]} ")









