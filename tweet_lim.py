import sys
import tweepy

cons_key = ""
cons_secret = ""
access_key = ""
access_secret = ""
#enter the consumer and access details
def get_tweets(screen_name):
		
	ath = tweepy.OAuthHandler(cons_key, cons_secret)
	ath.set_access_token(access_key, access_secret)
	api = tweepy.API(ath)
	#making api call
	tweets = []	
	tweets_new = api.user_timeline(screen_name = screen_name,count=10)
	
	tweets.extend(tweets_new)
	#extending list to store tweets
	oldest = tweets[-1].id - 1
			
	for tweet in tweets:
	#obtain only text	
		res = tweet.text	
		print res

if __name__ == '__main__':
	
	get_tweets(sys.argv[1])
	#give input diectly from command line
