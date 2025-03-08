def check_numbers(lst):
    unique = set(lst)
    if len(unique) == 1:
        return "Все числа равны"
    elif len(unique) == len(lst):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

nums = list(map(int, input().split()))
print(check_numbers(nums))