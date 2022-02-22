report_file = open("day1.txt", "r")
data = report_file.read()
# Split according to \n(newline) and convert into integers using map
report = list(map(int, data.split("\n")))
count = 0
for i in range(len(report) - 1):
    if report[i] < report[i + 1]:
        count += 1
        print("{}<{}, Count:{}".format(report[i + 1], report[i], count), end=" ")
print(count)
report_file.close()
