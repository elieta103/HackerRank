"""
Given the names and grades for each student in a class of  students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically
and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: .
Ordered alphabetically, the names are printed as:
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

Second lowest grade:  2.0
Names:
N KAR
"""
list_students_unordered = []
for _ in range(int(input("How many students ? : "))):
    name = input("Name :")
    score = float(input("Score : "))
    list_students_unordered.append([name, score])

# Order List of lists by score
list_students_ordered = sorted(list_students_unordered, key=lambda x: float(x[1]))
print(list_students_ordered)

# Second List
second_lowest_score = 0
for i in range(len(list_students_ordered)):
    if list_students_ordered[0][1] != list_students_ordered[i][1]:
        second_lowest_score = list_students_ordered[i][1]
        break
print(second_lowest_score)

list_students_second_lowest = []
for i in range(len(list_students_ordered)):
    if second_lowest_score == list_students_ordered[i][1]:
        list_students_second_lowest.append(list_students_ordered[i])
print(list_students_second_lowest)

#Order by String first element
list_students_second_lowest_ordered = sorted(list_students_second_lowest, key=lambda x: str(x[0]))
print(list_students_second_lowest_ordered)

#Print only names
for i in range(len(list_students_second_lowest_ordered)):
    print(list_students_second_lowest_ordered[i][0])

