# 큰수 만들기
#%%
import collections 
number = "1231234"
number = collections.deque(list(number))
length = len(number)
candidate = collections.deque(list())
count = 0
k = 3
while count != k:
    while number:
        ref = number.popleft()
        if len(number) == 0:
            candidate.append(ref)
        elif ref < number[0]:
            count += 1
            if count == k:
            
                answer = candidate + number
                break
        else:
            candidate.append(ref)
        

    number = candidate
    candidate = collections.deque(list())

print( ''.join(answer))

#%%
while len(number) != length -k:
    while number:
        ref = number.popleft()        
        
        if ref < number[0]:
            count += 1 
            if count == k:
                
                break
        else:
            candidate.append(ref)
            
    number = candidate
    candidate = collections.deque(list())

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

#%%
# 섬 연결하기
#costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
costs = [[0,1,1],[0,2,2],[2,3,1]]
costs_tuple = []
for a in costs:
    costs_tuple.append([(a[0],a[1]),a[2]])

n = 4 
costs_sum = 0
connected_bridge = set()
for i in range(n-1):
    
    min_costs = (n-1)*n/2
    
    
    for island,costs in costs_tuple:
        
        if i in island and set(island).issubset(connected_bridge) == False:

            if costs < min_costs:
                min_costs = costs
                tmp_island = island
                continue
        else:
            continue
    connected_bridge.add(tmp_island[0])            
    connected_bridge.add(tmp_island[1])            


    costs_sum +=  min_costs
    
    print(costs_sum)



    



#%%
def return_min_value(a):
    return min(a,key=lambda x:x[1])


origin,destination,cost = return_min_value(costs[i])
#%%
import collections
class islands:

    def __init__(self):
        self.info = collections.defaultdict(list)


    def add_bridge(self,source_key,des_key,cost):
        
        self.info[str(source_key)].append([des_key,cost])

def return_min_value(a):
    return min(a,key=lambda x:x[1])

test = islands()

for a in costs:
    test.add_bridge(a[0],a[1],a[2])


n = 4 
cost = 0

islands_num = set()

for i in range(len(test.info)):
    des,add_cost = return_min_value(test.info[str(i)])
    print(des,add_cost)
    cost += add_cost

    islands_num.add(str(i))
    islands_num.add(str(des))

    if len(islands_num) == n:
        break
    
print(cost)
#%%


total = 0
for c in '12345678':
    
    total = total + int(c)
    print(total,int(c))
        
#%%
print("a"*2.1)


