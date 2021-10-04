# We will have a set of racial slurs as following
slurs = set(['black','faggot','other_racial_slurs'])

file = open("tweets.txt", "x")      # Opening the input file of tweets

tweets = file.readlines()

profanity = {}              # Dictionary to store degree of profanity of each sentence

for tweet in tweets:
    degree = 0
    for word in tweet.split():      # splitting tweet to read each word
        if(word in slurs):
            # if word is a slur
            degree+=1
    
    profanity[tweet] = degree       # Storing degree with tweet in key,value pair
    
# Now display the degree of profanity
print(profanity)