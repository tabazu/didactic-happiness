import tweet
import music

def main():
    rank=music.getrank()
    tweet.post(rank)

if __name__=="__main__":
    main()
