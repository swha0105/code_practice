# 1. 완주하지 못한 선수
# my solution
#%%
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


import collections

p = collections.Counter(participant)
c = collections.Counter(completion)

p.subtract(c)
answer = []
for name in p:
    if p[str(name)] >=1 :
        answer.append(str(name)) 
    
answer = ','.join(answer)

# best solution 
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#%%
# 2. 전화번호 목록

phone_book = ["123","456","789"]	 # True
phone_book = ["12","123","1235","567","88"]	 # False
def solution(phone_book):
    phone_book = sorted(phone_book,key=len)

    for _ in phone_book:
        ref = phone_book.pop(0)
        
        phone_number_list = [s for s in phone_book if ref in s[:len(ref)]]
        
        if len(phone_number_list) >= 1:
            answer = False
            break
    else:
        answer = True
    return answer

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer    
#%%
# 위장 
import collections
clothes = \
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]  #5

clothes = \
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]] #3

#%%
def solution(clothes):
    import collections 
    import itertools
    
    clothes_dict = collections.defaultdict(list)
    number_list = []
    for value,key in clothes:
        clothes_dict[str(key)].append(value)

    answer =  1

    for key in clothes_dict:
        tmp_answer =  len(list(itertools.combinations(clothes_dict[str(key)],1))) + 1
        answer = (answer*tmp_answer)

    answer = answer - 1
    return answer

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1


#%%


