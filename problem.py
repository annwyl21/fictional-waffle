if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
#)

# that is the given code starter, i can tell it is part of a bigger structure because it has a random ) floating at the bottom.
# But this is supposed to be the simple, 'we have given you the code for the input now grab the data and start coding'

# except, i have no idea how to use this to grab the data!

# I can't print it to view the data structure I am receiving

#I should be able to grab something like this...
"5"
'Harry'
'37.21'
'Berry'
'37.21'
'Tina'
'37.2'
'Akriti'
'41'
'Harsh'
'39'

#but I can only get
'Harry' and '37.21'

#I ended up cheating and solving it by editing the given starter code to create my dictionary and list outside the loop...
if __name__ == '__main__':
    student_list = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list[name] = score
        scores.append(score)

scores = list(set(scores))
scores.sort()
second_lowest_score = scores[1]

list = []
for key, value in student_list.items():
    if value == second_lowest_score:
        list.append(key) # names of students with 2nd lowest score
list.sort()
for item in list:
    print(item) # names printed sorted alphabetically on newlines