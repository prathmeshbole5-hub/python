#kwargs - variable length keyword argumnt 

def func(**kwargs):
    print(kwargs)

func(x=10,y=20)
    


def student_details(sid,sname,**marks):
    if len(marks)==0:
        print(f"{sname}with id {sid}was absent for all the exams !")
    else:
        percent =sum(marks.values())/len(marks)
        print(f"{sname}with id {sid} secured {percent}%")

student_details(101,"john",sub1=78.5,sub2=65.2,sub3=45)
student_details(101,"corn",sub1=67.5,sub2=89.5,sub3=90.5)
