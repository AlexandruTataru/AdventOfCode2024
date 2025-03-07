first_list = []
second_list = []
with open('/Users/atataru/Desktop/input.txt', 'r') as file:
    for line in file:
        first, second = line.split('   ')
        first, second = int(first), int(second)
        first_list.append(first)
        second_list.append(second)

first_list.sort()
second_list.sort()

total_diff = 0

for i in range(len(first_list)):
    total_diff += abs(first_list[i] - second_list[i])

print(total_diff)