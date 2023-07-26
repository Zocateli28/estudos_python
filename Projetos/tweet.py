T: str = input()

Tweet = len(T)
if Tweet > 140:
    print("MUTE")
else:
    print("TWEET")