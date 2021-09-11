import csv
def output_by_subject():
    sub_list=[] #list of all subjects
    data_list=[] #list of all req. data
    with open("regtable_old.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            l1=[] #temp. list to store req data for appending in data_list
            if(row["subno"] not in sub_list):
                sub_list.append(row["subno"])
            l1.append(row["rollno"])
            l1.append(row["register_sem"])
            l1.append(row["subno"])
            l1.append(row["sub_type"])
            data_list.append(l1)
 #writing csv files subno wise
    for i in range(len(sub_list)):
        t=sub_list[i]
        with open(f"output_by_subject\{t}.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["rollno","register_sem","subno","sub_type"])
            for j in range(len(data_list)):
                if t in data_list[j][2]:
                      writer.writerow(data_list[j])
    return

def output_individual_roll():
    rollno_list=[] #list of all unique roll numbers
    data_list=[] #list of all req. data
    with open("regtable_old.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            l1=[]  #temp. list to store req data for appending in data_list
            if(row["rollno"] not in rollno_list):
                rollno_list.append(row["rollno"])
            l1.append(row["rollno"])
            l1.append(row["register_sem"])
            l1.append(row["subno"])
            l1.append(row["sub_type"])
            data_list.append(l1)

    #writing csv files rollno wise
    for i in range(len(rollno_list)):
        t=rollno_list[i]
        with open(f"output_individual_roll\{t}.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["rollno","register_sem","subno","sub_type"])
            for j in range(len(data_list)):
                if t in data_list[j][0]:
                      writer.writerow(data_list[j])
    return   
output_by_subject()
output_individual_roll()

