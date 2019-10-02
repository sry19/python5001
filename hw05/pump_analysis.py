MINUTE_PER_HOUR = 60
HOUR_PER_DAY = 24
FLOW_RATE = 2
SET_5_GALLONS = 5
SET_100_GALLONS = 100
KW_INTO_WATT = 1000
RUNNING_JUDGE = 500
STANDARD_POWER_PER_MIN = 1000
RUNTIME_AT_LEAST = 120


def main():
    '''user input a filename and the function analyse the data in that file
        None -> None'''

    # read the data file, count the total time ans running time
    # build a list to store data
    filename = input("Please enter the file name: ")
    try:
        f = open(filename, "r")
    except:
        print("Unable to open", filename)
        return
    minute = 0
    running_time = 0
    lst_data = []
    for line in f:
        data_per_minute = int(line.rstrip())
        lst_data.append(data_per_minute)
        if data_per_minute > RUNNING_JUDGE:
            running_time += 1
        minute += 1

    # Report the duration of the data file in both hours and days
    hour = minute / MINUTE_PER_HOUR
    day = hour / HOUR_PER_DAY
    print("Data covers a total of", hour, "hours")
    print("(That's", day, "days)")
    print()

    # Report both the total number of gallons produced and the average daily
    # consumption.
    print("Pump was running for", running_time, "minutes, ", end='')
    gallon_produce = FLOW_RATE * running_time
    print("producing", gallon_produce, "gallons")
    gallon_per_day = (HOUR_PER_DAY * MINUTE_PER_HOUR / minute) * gallon_produce
    print("(That's", gallon_per_day, "gallons per day)")
    print()

    # Report the total power used by the pump
    total_watt_mins = sum(lst_data)
    print("Pump required a total of", total_watt_mins, "watt minutes of power")
    total_kwh = total_watt_mins / (KW_INTO_WATT * MINUTE_PER_HOUR)
    print("That's", total_kwh, "kWh")
    print()

    # Print how long it took to consume a certain quantity of water
    time_5 = time_certain_quantity(SET_5_GALLONS, lst_data)
    time_100 = time_certain_quantity(SET_100_GALLONS, lst_data)
    print("It took", time_5, "minutes of data to reach 5 gallons.")
    print("It took", time_100, "minutes of data to reach 100 gallons.")
    print()

    # look through the data file for times when the pump runs for at least
    # 120 minutes in a row, and report when the long run started and how
    # long it lasted.
    i = 0
    has_sth = False
    while i < len(lst_data):
        if lst_data[i] > RUNNING_JUDGE:
            start_point = i + 1
            while i < len(lst_data):
                if lst_data[i] > RUNNING_JUDGE:
                    i += 1
                else:
                    if i + 1 - start_point >= RUNTIME_AT_LEAST:
                        time_last = i + 1 - start_point
                        if not has_sth:
                            print("Information on water softener recharges:")
                            has_sth = True
                        print(time_last, "minute run started at", start_point)
                    break
            if i == len(lst_data) and i + 1 - start_point >= RUNTIME_AT_LEAST:
                time_last = i + 1 - start_point
                if not has_sth:
                    print("Information on water softener recharges:")
                    has_sth = True
                print(time_last, "minute run started at", start_point)
        i += 1


def time_certain_quantity(set_quantity, lst_data):
    '''compute how long it took to consume a certain quantity of water
       number(quantity), list(data) ->
       number(time needed, -1 if cannot reach that quantity) '''
    needed_power = set_quantity / FLOW_RATE * STANDARD_POWER_PER_MIN
    time = -1
    sums = 0
    for i in range(len(lst_data)):
        sums = sums + lst_data[i]
        if sums > needed_power:
            time = i + 1
            break
    return time


main()
