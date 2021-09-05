def output_by_subject():
  #open file in read mode and fetching req data
   f=open("regtable_old.csv","r")
   list2=[]  #containing all values in single list of regtable.csv file
   sub_list=[]  # unique subject list
   for line in f:
      list=line.split(",")
      allvalues=[]  #required values from files
      allvalues.append(list[0])
      allvalues.append(list[1])
      allvalues.append(list[3])
      allvalues.append(list[8].strip())
      if list[3] not in sub_list and list[3]!="subno":
        sub_list.append(list[3])
      list2.append(allvalues)
   
   for i in range(len(sub_list)):
        t=sub_list[i]
        s_file=open(f"output_by_subject\{t}.csv","w") #seprate csv files subno wise containing only req data
        s_file.write(list2[0][0])
        s_file.write(",")
        s_file.write(list2[0][1])
        s_file.write(",")
        s_file.write(list2[0][2])
        s_file.write(",")
        s_file.write(list2[0][3])
        s_file.write("\n")
        for j in range(len(list2)):
            if t in list2[j][2]:
              s_file.write(list2[j][0])
              s_file.write(",")
              s_file.write(list2[j][1])
              s_file.write(",")
              s_file.write(list2[j][2])
              s_file.write(",")
              s_file.write(list2[j][3])
              s_file.write("\n")
   return

def output_individual_roll():
  #open file in read mode and fetching req data
    f=open("regtable_old.csv","r")
    list1=[]  #containing all values in single list of regtable.csv file
    rollno_list=[]  # unique k roll numbers
    for line in f:
      list=line.split(",")
      allvalues=[]  #required values from files
      allvalues.append(list[0])
      allvalues.append(list[1])
      allvalues.append(list[3])
      allvalues.append(list[8].strip())
      if list[0] not in rollno_list and list[0]!="rollno":
       rollno_list.append(list[0])
      list1.append(allvalues)
  #open file in write mode to make k seprate files roll no wise
    for i in range(len(rollno_list)):
        t=rollno_list[i]
        s_file=open(f"output_individual_roll\{t}.csv","w") #seprate csv files roll no wise containing only req data
        s_file.write(list1[0][0])
        s_file.write(",")
        s_file.write(list1[0][1])
        s_file.write(",")
        s_file.write(list1[0][2])
        s_file.write(",")
        s_file.write(list1[0][3])
        s_file.write("\n")
        for j in range(len(list1)):
            if t in list1[j][0]:
              s_file.write(list1[j][0])
              s_file.write(",")
              s_file.write(list1[j][1])
              s_file.write(",")
              s_file.write(list1[j][2])
              s_file.write(",")
              s_file.write(list1[j][3])
              s_file.write("\n")
    return
output_by_subject()
output_individual_roll()
