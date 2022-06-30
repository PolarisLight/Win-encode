import random


def rand_partition(array, start_i, end_i):
    i = random.randint(start_i, end_i)
    temp = array[i]
    array[i] = array[end_i]
    array[end_i] = temp
    j = start_i - 1
    for i in range(start_i, end_i):
        if array[i] < array[end_i]:
            temp = array[i]
            array[i] = array[j + 1]
            array[j + 1] = temp
            j += 1
    temp = array[end_i]
    array[end_i] = array[j + 1]
    array[j + 1] = temp
    return array, j + 1


def quick_sort(array, start_i, end_i):
    if start_i < end_i:
        array, k = rand_partition(array, start_i, end_i)
        array = quick_sort(array, start_i, k - 1)
        array = quick_sort(array, k + 1, end_i)
    return array


def find_k_min(array, k, start_i, end_i):
    array, p = rand_partition(array, start_i, end_i)
    if p == k:
        return array[p]
    elif k < p:
        return find_k_min(array, k, start_i, p - 1)
    else:
        return find_k_min(array, k, p + 1, end_i)


if __name__ == "__main__":
    a = [i for i in range(10)]
    random.shuffle(a)
    print(a)
    sorted_a = quick_sort(a, 0, len(a) - 1)
    print(sorted_a)
