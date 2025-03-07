import re

total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        for match in re.findall('mul\(\d+,\d+\)', line):
            groups = re.search('mul\((\d+),(\d+)\)', match)
            print(f'{groups.group(1)} and {groups.group(2)}')
            total_sum += (int(groups.group(1)) * int(groups.group(2)))

print(total_sum)