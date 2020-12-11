# 큰수 만들기
#%%
import collections 
number = "4177252841"
length = len(number)
number = collections.deque(list(number))
count = 0 
k = 4 
candidate = []
while len(candidate) != length - k:
    for i in range(len(number)-1):
        if number[i] < number[i+1]:
            print("a",number.popleft())
            break
        else:
            candidate.append(number[i])
            print("b",number.popleft())
            break
    
        candidate.append(number[-1])
    

print(candidate)
#%%







    for i in range(len(number)-1):

        if number[i] == '9':
            continue
        
        elif number[i] < number[i+1]:
            number.popleft()
            count += 1
            break
            
    else:
        number.pop(-1)
        count += 1 

print(join(number))


#%% 
# 구명보트
#%%
import collections
people = [50,50,50,50]

people.sort()
people = collections.deque(people)
answer = 0

while people:
    if len(people) == 1:
        answer += 1
        break

    if people[0] + people[1] > limit:
        answer += len(people)
        break
    elif people[0] + people[-1] > limit:
        answer += 1
        people.pop()
    else:
        answer += 1
        people.popleft()
        people.pop()    




    
        



# while people:
#     if people[0] + people[1] > limit:
        
#         answer += len(people)
#         break
    
#     elif people[0] + people[-1] > limit:
#         answer += 1
#         people.pop()
#     else:
#         answer += 1
#         people.popleft()
#         people.pop()    
        
