#%% 기능개발 

import copy
import numpy as np

n = 0

ans = []

progresses = [93,30,55]	
speeds = [1,30,5]	
answer = [2,1]

def decision(input_array,speeds,n,ans):
    n = n + 1

    input_array = np.array(input_array)
    speeds = np.array(speeds)
    ref = np.sum([input_array,n*speeds],axis=0)
  
    index_candidate = ref>=100
    index = []
       
    i = 0

    if len(index_candidate) != 0:
                
        while index_candidate[i] == True :
            index.append(i)
            i = i+1
            if i >= len(index_candidate):
                break

    if len(index) != 0:
        ans.append(len(index))

    input_array = np.delete(input_array,index)
    speeds = np.delete(speeds,index)

    if input_array.shape[0] == 0:
        return ans
    else:
        return decision(input_array,speeds,n,ans)

def solution(progresses, speeds):
    answer = decision(progresses,speeds,n,ans)    
    return answer

######

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


#%%
## 다리를 지나는 트럭 
end = len(truck_weights)
answer = 0
time = 0
truck_passing_weight = []
truck_passing_time = []
truck_passed = []


while len(truck_passed) != end:

    if len(truck_passing_time) == 0:
        pass

    elif time - truck_passing_time[0] >= bridge_length:
        truck_passed.append(truck_passing_weight.pop(0))
        truck_passing_time.pop(0)


    if len(truck_weights) == 0:
        pass

    elif sum(truck_passing_weight) + truck_weights[0] <= weight:
        truck = truck_weights.pop(0)
        truck_passing_weight.append(truck)
        truck_passing_time.append(time)

    time = time + 1 
answer = time

####

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


#%%
# 프린터
def solution(priorities, location):

    import collections
    
    def decision(prior,index,count,location):

        ref_value = prior[0]
        ref_index = index[0]
    
        if ref_value < max(prior):
            prior.append(prior.popleft())
            index.append(index.popleft())
            return decision(prior,index,count,location)

        elif ref_index == location:
            count = count + 1
            return count 

        else:     
            count = count + 1
            prior.popleft()
            index.popleft()
            return decision(prior,index,count,location)


    
    prior = collections.deque(priorities)

    index = collections.deque(list(range(len(priorities))))
    
    count = 0
    count = decision(prior,index,count,location)

    answer = count 
    return answer
###

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
