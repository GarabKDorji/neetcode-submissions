class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId,self.count])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        max_heap = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 
                tweetId, count = self.tweetMap[followeeId][index]
                heapq.heappush(max_heap,[count,tweetId,index-1,followeeId])
        res = []
        while len(res) < 10 and max_heap: 
            count , tweetId, index, followeeId = heapq.heappop(max_heap)
            res.append(tweetId)
            if index >= 0 :
                tweetId , count = self.tweetMap[followeeId][index]
                heapq.heappush(max_heap,[count,tweetId,index-1,followeeId])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
