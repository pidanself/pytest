import collections


def shortestCompletingWord(licensePlate, words):
    cntr_l, res = collections.defaultdict(int), [None, None]
    for char in licensePlate:
        if char.isalpha(): cntr_l[char.lower()] += 1
    for word in words:
        check = dict(cntr_l)
        for char in word:
            char = char.lower()
            if char in check:
                check[char] -= 1
                if check[char] == 0: del check[char]
        if not check and (not all(res) or len(word) < res[1]): res = [word, len(word)]
    return res[0]


# match, dct = [e.lower() for e in licensePlate if e.isalpha()], {}
# for e in match:
#     dct[e] = match.count(e)
#
# ret, size = '', 0
# for e in words:
#     for i in dct:
#         if e.count(i) < dct[i]: break
#     else:
#         tmp = len(e)
#         if not ret or tmp < size:
#             ret = e
#             size = tmp
# return ret