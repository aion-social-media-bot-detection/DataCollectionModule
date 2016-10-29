class TweetCriteria:

	def __init__(self):
		self.maxTweets = -1

	def setSince(self, since):
		self.since = since
		return self

	def setUntil(self, until):
		self.until = until
		return self

	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self

	def setMaxTweets(self, maxTweets):
		self.maxTweets = maxTweets
		return self
