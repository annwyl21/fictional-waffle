# Full solution when I gave up and just solved it myself using the data given in the exercise

data = "5 Harry 37.21 Berry 37.21 Tina 37.2 Akriti 41 Harsh 39"

mylist = data.split()
num = mylist.pop(0)

student_list = {}
scores = []
for number in range(int(num)):
    name = mylist.pop(0)
    score = mylist.pop(0)
    student_list[name] = score
    scores.append(score)

scores = list(set(scores))
print(scores)
scores.sort()
second_lowest_score = scores[1]

list = []
for key, value in student_list.items():
    if value == second_lowest_score:
        list.append(key) # names of students with 2nd lowest score
list.sort()
for item in list:
    print(item) # names printed sorted alaphabetically on newlines

print("And the nested list:", student_list) # created nested list
