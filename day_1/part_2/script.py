first_list = []
second_list = []
with open('input.txt', 'r') as file:
    for line in file:
        first, second = line.split('   ')
        first, second = int(first), int(second)
        first_list.append(first)
        second_list.append(second)

total_similarity = 0

for first in first_list:
    total_similarity += (first * second_list.count(first))

print(total_similarity)