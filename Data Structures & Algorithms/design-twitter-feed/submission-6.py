class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)
        max_heap = []
        res = []
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet:
                index = len(self.tweet[followeeId])-1
                count, tweetId = self.tweet[followeeId][index]
                heapq.heappush(max_heap,[count,tweetId,followeeId,index-1])
        
        while len(res) < 10 and max_heap: 
            count, tweetId ,followeeId, index = heapq.heappop(max_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet[followeeId][index]
                heapq.heappush(max_heap, [count, tweetId, followeeId, index - 1])

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)