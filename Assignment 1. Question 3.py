scores=[]
courses=11
for i in range(11):
    score=int(input("Enter the final score for course"))
    scores.append(score)

    totalscore=sum(scores)
    averagescore=(totalscore/sum)

    if averagescore>90:
        grade="A"
    elif averagescore>80:
        grade="B"
    elif 75<=averagescore<=79:
        grade="C"
    elif averagescore>60:
        grade="D"
    else:
        grade="F"
