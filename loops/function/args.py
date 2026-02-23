# *args -variable length positional argument (oto n)

def add(*args):
    return sum(args)

result = add(10,20,4,5,6,7,8,9)
print(result)



def student_details(sid,sname,*marks):
    if len(marks)==0:
        print(f"{sname}with id {sid}was absent for all the exams !")
    else:
        percent =sum(marks)/len(marks)
        print(f"{sname}with id {sid} secured {percent}%")

student_details(101,"john",87.0,78.0,89.0)
student_details(101,"corn",97.0,88.0,89.0)
student_details(101,"mon",89.0,98.0,89.0)
student_details(101,"ton",)
    