from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.postMap = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.postMap[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.postMap:
                index = len(self.postMap[followeeId]) - 1
                time, tweetId = self.postMap[followeeId][index]
                heap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, tweetId, followeeId, nextIndex = heapq.heappop(heap)
            res.append(tweetId)
            if nextIndex >= 0:
                newtime, nextTweetId = self.postMap[followeeId][nextIndex]
                heapq.heappush(heap, [newtime, nextTweetId, followeeId, nextIndex - 1])
             
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
