def get_memory_score(n):
    score=0
    newlist=[]
    for i in n:
      j=str(i)
      if(j.isdigit()):
        continue
      else:
        newlist.append(i)
    if(len(newlist)!=0):
        print("Please enter a valid input list. Invalid inputs detected:",newlist)
        return
    for i in n:
        if(i in newlist):
            score+=1
            if(len(newlist)==5):
                del newlist[0]
            newlist.append(i)
        else:
            if(len(newlist)==5):
                del newlist[0]
            newlist.append(i)
    return score

#input_nums =[7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
#print("Score:", get_memory_score(input_nums))
