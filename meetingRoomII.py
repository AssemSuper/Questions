from typing import List;
import heapq
class Solution:
    class Interval(object):
        def __init__(self, start,end):
            self.start=start
            self.end=end
    # def minMeetingRooms(self, intervals):
    def minMeetingRooms(self,intervals):
        # start_arr=[]
        # end_arr=[]
        # for start,end in intervals:
        #     start_arr.append(start)
        #     end_arr.append(end)
        # # print(start_arr)
        # # print(end_arr)
        # start_arr.sort()
        # end_arr.sort()
        # i=0
        # j=0
        # rooms=0
        # max_rooms=0
        # while i<len(start_arr):
        #     if start_arr[i]<end_arr[j]:
        #         rooms+=1
        #         max_rooms=max(max_rooms,rooms)
        #         i+=1
        #     else:
        #         rooms-=1
        #         j+=1
        # return max_rooms
        #Base case
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda x:x[0])
        heap_end=[]
        # heapq.heapify(heap_end)
        heapq.heappush(heap_end,intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0]>=heap_end[0]:
                heapq.heappop(heap_end)
            # else:
            #     room+=1
            heapq.heappush(heap_end,intervals[i][1])
        return len(heap_end)

intervals = [(0,30),(5,10),(15,20)]
# heap_end 30
# i=1 5 >30-> not _> heap_end 30 10
# i=2 15>10 -> yes  heap_end 30 20
print(Solution().minMeetingRooms(intervals))
#Time C: Let n be number of intervals Build start_arr and end_arr O(n) Sort both arrays O(nlogn)+O(nlogn)=O(nlogn) Two pointer traversal O(n)
#-> O(nlogn)
#Space C: extra space is used for 2 arrays start_arr and end_arr O(n)


# Heap solution

"""
1)Sort by starting time the intervals
2 add first meeting  end time  in min heap
3 For each next meeting:
    If the meeting starts after the earliest ending meeting, reuse that room
    Otherwise allocate new room
Push the meeting’s end time into the heap

if next starting greater than min heap we can use same room
"""


