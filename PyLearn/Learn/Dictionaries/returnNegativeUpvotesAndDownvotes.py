def getVoteCount(dic):
    for _ in dic.values():
        sore = abs(dic["upvotes"] - dic["downvotes"])
    print(sore)

dic = {"upvotes": 13, "downvotes": 100}

getVoteCount(dic)