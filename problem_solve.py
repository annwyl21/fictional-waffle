#I can solve it if I have the data...

data = "5 Harry 37.21 Berry 37.21 Tina 37.2 Akriti 41 Harsh 39"

mylist = data.split()
num = mylist.pop(0)

student_list = []
for number in range(int(num)):
    student = []
    name = mylist.pop(0)
    score = mylist.pop(0)
    student.append(name)
    student.append(score)
    student_list.append(student)

print(student_list)
