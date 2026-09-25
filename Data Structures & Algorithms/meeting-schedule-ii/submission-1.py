"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []
        for i in range(len(intervals)):
            points.append((intervals[i].start, 1))
            points.append((intervals[i].end, 0))

        points.sort()
        count = 0
        rooms = 0
        for point, flag in points:
            if flag == 1:
                count += 1
            else:
                count -= 1
            rooms = max(count, rooms)
        return rooms