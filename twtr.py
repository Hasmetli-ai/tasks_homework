vowels=['a','e','i','o','u']
tweet=input("Enter your tweet: ")
for i in vowels:
    if tweet.find(i)>0:
        tweet=tweet.replace(i,'')
print(tweet)