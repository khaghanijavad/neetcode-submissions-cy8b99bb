class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> {followeeId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        followees = self.following[userId] | {userId}

        for followeeId in followees:
            if self.tweets[followeeId]:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, (time, tweetId, followeeId, idx - 1))

        while heap and len(feed) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(heap)
            feed.append(tweetId)

            if idx >= 0:
                next_time, next_tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, (next_time, next_tweetId, followeeId, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)