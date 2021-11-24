import pandas as pd

# to get ltp count
def get_ltp_count(ltp_string):
    ltp=ltp_string.split("-")
    ltpcount=0
    for i in ltp:
        if(i>0):
            ltpcount=ltpcount+1
    return ltpcount


#function to store student details
output_file = pd.DataFrame(columns = ["Roll Number","Registered Sem","Scheduled Sem","Course Code","Name","Email","AEmail","Contact"])

course_taken = pd.read_csv("course_registered_by_all_students.csv")
course_master = pd.read_csv("course_master_dont_open_in_excel.csv")

def feedback_not_submitted():
    roll_list=[]  #list of all roll numbers
    for index, row in course_taken.iterrows():
        rollnum=row['rollno']
        if(rollnum not in roll_list):
            roll_list.append(rollnum) #adding roll num to list

    for i in roll_list:
        sub_of_stud=()
        for index, row in course_taken.iterrows():
            if(i==row['rollno']):
                sub_of_stud.add(course_taken['subno'],'0')


		     



    



