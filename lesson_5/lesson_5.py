import modul1

def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += 1
        print(summa)


def sum_str(*arg):
    res = ''
    for i in arg:
        res += f' {i}'
    return res


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


def reorder(number, step=1, val1=0):
    if step == number:
        val1 = input("Введи символ: ")
        print(val1, end=" ")
    else:
        val1 = input(f"Введи символ: ")
        reorder(number, step + 1, val1)
        print(val1, end=" ")


def reorder(number):
    if number == 0:
        return ""
    strochechka = input()
    return reorder(number - 1) + strochechka


nums = int(input("Введи количество элементов: "))
print(reorder(nums))

# print(sum_str('a', 'b', 'c', 'd', 'r', 'd'))
# sum_numbers(15)
# print(m1.max1(6, 4))
print(quick_sort([14, 5, 65, 43, 4, 54]))

list1 = [14, 5, 65, 43, 4, 54]
merge_sort(list1)
print(list1)

