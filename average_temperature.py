file = open('results.txt', 'r')

lowest = 30
lowest_year = 0
highest = 10
highest_year = 0


for line in file.read().splitlines():
    if line[0].isdigit():
        values = line.strip().split()
        low = int(values[3])
        high = int(values[1])

        if low < lowest:
            lowest = low
            lowest_year = values[1]

        if high > highest:
            highest = high
            highest_year = values[1]

print ("Year: ", (lowest_year))
print ("The lowest temperature is: ", (lowest))


print ("Year: ", (highest_year))
print ("The highest temperature is: ", (highest))