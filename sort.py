#%%
## K번째수
array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
# answer = 5,6,3
def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer
##
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#%%
# 가장 큰 수 

numbers = [6,10,2]
#answer: "6210"

numbers = [3,30,34,5,9]
#answer: "9534330"

def solution(numbers):
    
    str_number = list(map(str,numbers))
    
    str_number.sort(key=lambda x: x*3,reverse=True)

    answer = str(int(''.join(str_number)))
    return answer

#%%
# H-index
citations = [3, 0, 6, 1, 5]	
citations.sort(reverse=True)

print((list(enumerate(citations, start=1))))

#%%
# #answer: 3
def solution(citations):
    import collections 
    
    collect = collections.Counter(citations)
    collect = dict(sorted(collect.items()))
    answer = 0
    
    while collect:

        a,b = collect.popitem() 
        print(a,b)
        if answer + b > a:
            break
        else:
            answer = answer+b
    
    else:
        answer = len(citations)

    return answer

print(solution(citations))

####
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer