import openpyxl

sheet = openpyxl.open("table.xlsx", read_only=True).active

def get_group_schedule(cst: str, day: str):
    group = {"CST 1": 4, "CST 2": 7, "CST 3": 10, 'CST 4': 16, "CST 5": 19, "CST 6": 22, "CST 7": 28, "CST 8": 31,
             "CST 9": 34}

    lessons = [str(i).replace('-','').strip() for i in [sheet[i][group[cst]].value for i in range(11, 73)]]
    classes = [str(i).replace('-','').strip() for i in [sheet[i][group[cst] + 1].value for i in range(11, 73)]]
    schedule = list(map(lambda x, y: x + "  " + y, lessons,classes))
    days = {"Monday": [1, 8], "Tuesday": [12, 18], "Wednesday": [23, 31], "Thursday": [34, 42], "Friday": [45, 53],
            "Saturday": [56, 64]}
    lessons_time = ["1) 8:00-9:20", "2) 9:30-10:50", "3) 11:10-12:30", "4) 13:00-14:20", "5) 14:40-16:00",
                    "6) 16:20-17:40", "7) 18:10-19:30", "8) 19:40-21:00"]

    result = schedule[days[day][0]:days[day][1]]
    result = dict(zip(lessons_time, result))
    result = [k +": " +  v + "\n" for k, v in result.items() if "None" not in v]
    res = ''
    for i in result:
        res += i
    return res