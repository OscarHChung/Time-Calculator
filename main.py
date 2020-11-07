
def add_time(start_time, added_time, start_date = ""):
    days_passed = 0
    start_temp = start_time.split()[0]
    start_hour = int(start_temp.split(":")[0])
    start_min = int(start_temp.split(":")[1])
    added_hour = int(added_time.split(":")[0])
    added_min = int(added_time.split(":")[1])

    final_min = (start_min + added_min) % 60
    final_hour = (start_hour + added_hour) % 12 + int((start_min + added_min) / 60)
    if final_hour == 0:
        final_hour = "12"
    final_hour = str(final_hour)
    if final_min < 10:
        final_min = "0" + str(final_min)
    final_min = str(final_min)

    ampm = start_time.split()[1]
    for i in range(int((start_hour + added_hour + int((start_min + added_min) / 60)) / 12)):
        if ampm == "AM":
            ampm = "PM"
        else:
            ampm = "AM"
            days_passed += 1
    result = final_hour + ":" + final_min + " " + ampm

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_date_index = -1
    for index, i in enumerate(weekdays):
        if start_date == i:
            start_date_index = index
    if start_date_index != -1:
        final_index = (days_passed + start_date_index) % 7
        final_day = weekdays[final_index]
        result += ", " + final_day

    if days_passed >= 2:
        result += " (" + str(days_passed) + " days later)"

    return result


if __name__ == '__main__':
    print(add_time("12:32 PM", "26:12", "Monday"))
