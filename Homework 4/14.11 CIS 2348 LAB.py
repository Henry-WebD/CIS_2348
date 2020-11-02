#Henry Saravia, PSID: 1853318

def selection_sort_descend_trace(user_lst):
    for i in range(len(user_lst) - 1):
        largest_value = i
        for j in range(i + 1, len(user_lst)):
            if user_lst[j] > user_lst[largest_value]:
                largest_value = j
        user_lst[i], user_lst[largest_value] = user_lst[largest_value], user_lst[i]
        for x in user_lst:
            print(x, end=' ')
        print()
    return user_lst


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    selection_sort_descend_trace(nums)

