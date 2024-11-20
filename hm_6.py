def binary_search(arr, val):
    n = len(arr)
    result_ok = False
    first = 0
    last = n - 1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == val:
            result_ok = True
            print(f"Элемент найден в индексе {middle}.")
            return middle
        elif arr[middle] < val:
            first = middle + 1
        else:
            last = middle - 1

    if not result_ok:
        print("Элемент не найден.")
        return -1


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]

value_to_search = 9

binary_search(sorted_list, value_to_search)




def selection_sort(lists):
    n = len(lists)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lists[j] < lists[min_index]:
                min_index = j
        lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists


unsorted_list = [29, 10, 14, 37, 13]

print("Начальный список:", unsorted_list)

sorted_list = selection_sort(unsorted_list)

print("Отсортированный список:", sorted_list)


