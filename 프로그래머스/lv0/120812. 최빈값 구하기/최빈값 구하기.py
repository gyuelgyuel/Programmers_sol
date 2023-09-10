def solution(array):
    freq_list = [0] * (max(array)+1)
    for i in array:
        freq_list[i] += 1
    copy = freq_list[:]
    copy.remove(max(freq_list))
    if max(freq_list) == max(copy):
        return -1
    else:
        return freq_list.index(max(freq_list))