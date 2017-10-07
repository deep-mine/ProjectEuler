for i in range(99999,9999999):
    oneX = [int(d) for d in str(i)]
    oneX = set(oneX)

    twoX = [int(d) for d in str(2*i)]
    twoX = set(twoX)

    threeX = [int(d) for d in str(3*i)]
    threeX = set(threeX)

    fourX = [int(d) for d in str(4*i)]
    fourX = set(fourX)

    fiveX = [int(d) for d in str(5*i)]
    fiveX = set(fiveX)

    sixX = [int(d) for d in str(6*i)]
    sixX = set(sixX)

    if oneX==twoX and twoX==threeX and threeX==fourX and fourX==fiveX and sixX==fiveX:
        print(i)
        break
