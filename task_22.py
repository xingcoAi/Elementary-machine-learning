#第一种快排实现
def quick_sort(sort_list, start_index, end_index):
    print(sort_list)
    if start_index < end_index:
        basic_value, i, j = sort_list[start_index], start_index, end_index
        while i < j:
            while i < j and basic_value <= sort_list[j]:
                j -= 1

            while i < j and sort_list[i] <= basic_value:
                i += 1

            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

        sort_list[i], sort_list[start_index] = sort_list[start_index], sort_list[i]
        # 左边递归
        quick_sort(sort_list, start_index, i -1)
        # 右边递归
        quick_sort(sort_list, i+1, end_index)


l = [7, 1, 3, 0, 6, 12, 45]
# quick_sort(l, 0, len(l) - 1)

# 第二种快排实现
def quick_sort2(quick_list):
    if  quick_list == []:
        return []

    else:
        first = quick_list[0]
        less = quick_sort2([l for l in quick_list[1:] if  l < first])
        more = quick_sort2([m for m in quick_list[1:] if  m >= first])
        return less + [first] + more

# r = quick_sort2(l)
# print(r)

