class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:     
        self.tweet[userId].append([self.count,tweetId])
        self.count -= 1 
        
    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweet:
                index = len(self.tweet[followeeId]) - 1 
                count, tweetId = self.tweet[followeeId][index]
                heapq.heappush(min_heap,[count, tweetId , index-1,followeeId])
        
        while min_heap and len(res) < 10: 
            count, tweetId , index,followeeId =  heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet[followeeId][index]
                heapq.heappush(min_heap,[count, tweetId , index-1,followeeId])
            
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
