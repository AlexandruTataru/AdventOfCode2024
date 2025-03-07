safe_reports_count = 0
with open('input.txt', 'r') as file:
    for line in file:
        safe_reports_count += 1
        reports = [int(val) for val in line.split(' ')]

        increasing_sort = sorted(reports)
        decreasing_sort = sorted(reports, reverse = True)

        if reports != increasing_sort and reports != decreasing_sort:
            safe_reports_count -= 1
            continue

        good_diff = True
        last = reports[0]
        for i in range(1, len(reports)):
            if abs(reports[i] - last) > 3 or abs(reports[i] - last) < 1:
                good_diff = False
                break
            last = reports[i]
        if not good_diff:
            safe_reports_count -= 1

print(safe_reports_count)