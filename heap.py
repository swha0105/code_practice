## 더 맵게
scoville = [1, 2, 3, 9, 10, 12]	
K = 7

def solution(scoville, K):
    import heapq
    
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        min_1 = heapq.heappop(scoville)
        
        if min_1 >= K:
            return answer
        else:
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min_1 + 2*min_2)
            answer += 1
            
    if scoville[0] < K:
        answer = -1
            
    return answer

##

import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer


#%%  이중우선순위큐
def solution(operations):
    class Heap:
        def __init__(self):

            self.max_list = []
            self.max_list.append(None)
            self.min_list = []
            self.min_list.append(None)

        def move_up(self,in_idx):
            if in_idx <= 1:
                return False

            pa_idx = in_idx // 2

            if self.max_list[pa_idx] < self.max_list[in_idx]:
                return True
            else:
                return False

        def move_down(self,in_idx):
            if in_idx <= 1:
                return False

            pa_idx = in_idx // 2

            if self.min_list[pa_idx] > self.min_list[in_idx]:
                return True
            else:
                return False

        def insert(self,num):

            self.max_list.append(num)

            in_idx = len(self.max_list) - 1

            while self.move_up(in_idx):
                pa_idx = in_idx // 2
                self.max_list[pa_idx],self.max_list[in_idx] = self.max_list[in_idx],self.max_list[pa_idx]
                in_idx = pa_idx

            self.min_list.append(num)
            in_idx = len(self.min_list) - 1

            while self.move_down(in_idx):
                pa_idx = in_idx // 2
                self.min_list[pa_idx],self.min_list[in_idx] = self.min_list[in_idx],self.min_list[pa_idx]
                in_idx = pa_idx
            return True

        def delete(self,num):
            if  len(self.min_list) == 1 or len(self.max_list) == 1:
                return 
            
            if num == -1:
                self.min_list.pop(1)

            if num == 1:
                self.max_list.pop(1)
            return 

    test = Heap()

    while operations:
        string = operations.pop(0).split()

        if string[0] == "I":
            test.insert(int(string[-1]))
        if string[0] == "D":
            test.delete(int(string[-1]))

    if len(test.min_list) <= 2 or len(test.max_list) <= 2:
        answer = [0,0]
    else:
        answer = [a for a in test.max_list if a in test.min_list]
    

    answer = [ max(answer[1:]),min(answer[1:]) ]
        
   
    return answer