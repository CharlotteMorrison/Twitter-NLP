from utilities import Tweets
# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    twitter_api = Tweets()

    twitter_api.send_dm('@bella_bear7', 'Hi bella, I am sending this from my twitter python program.  Did it work?')
