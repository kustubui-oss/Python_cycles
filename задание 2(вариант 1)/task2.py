#задание 2 вариант 1
for two_dight_num in range(10, 100):
    sum_current = two_dight_num % 10 + two_dight_num // 10
    sum_next = sum([int(ch) for ch in str(2 * two_dight_num)])
    if sum_current == sum_next:
        print(two_dight_num)
