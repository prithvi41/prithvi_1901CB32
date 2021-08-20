def meraki_helper(n):
    count=0
    for i in n:
        if(i<11):
            print("Yes - ",i ,"is a Meraki number")
            count+=1  
        else:
            j=i
            flag=True
            while i>10:
                k=i%10
                i=i//10
                l=i%10
                if(abs(k-l)!=1):
                    print("NO - ",j ,"is not a Meraki number")
                    flag=False
                    break
            if(flag):
                print("Yes - ",j ,"is a Meraki number")
                count+=1
    print("the input list contains",count," meraki and", len(n)-count," non meraki numbers")
    





#input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
