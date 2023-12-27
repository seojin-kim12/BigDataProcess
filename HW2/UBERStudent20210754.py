import calendar

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

with open('uber.dat', 'r') as infile:
    lines = infile.readlines()

rst = {}
for line in lines:
    data = line.strip().split(',')
    num, date, active_v, t = data

    month, day, year = map(int, date.split('/'))
    day = calendar.weekday(year, month, day)
    dayname = weekday[day]

    k = f"{num},{dayname}"
    if k in rst:
        rst[k][0] += int(active_v)
        rst[k][1] += int(t)
    else:
        rst[k] = [int(active_v), int(t)]

sorted_rst = sorted(rst.items(), key=lambda x: (x[0].split(',')[0], weekday.index(x[0].split(',')[1])))

with open('uberoutput.txt', 'w') as outfile:
    for k, value in sorted_rst:
        num, dayname = k.split(',')
        active_v, t = value
        outfile.write(f"{num},{dayname} {active_v},{t}\n")