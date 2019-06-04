word1 = "bottles"
word2 = "beer"
for beer_num in range (99,0,-1):
    print (beer_num, word1, "of ", word2, " on the wall.")
    print (beer_num, word1, "of ", word2)
    print ("Take one down.")
    print ("Pass it around.")
    if beer_num == 1:
            print ("no more bottles of beer on the Wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word1 = "bottle"
        print (new_num, word1, "of beer on the Wall.")
    print()
