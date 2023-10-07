"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output
56.00
The query_name is 'beta'. beta's average score is .

Harsh 25 26.5 28
Anurag 26 28 30
Harsh
26.50
"""

if __name__ == '__main__':
    n = int(input("How many students ? : "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Students Scores :").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Query :")

    for key, value in student_marks.items():
        print(f"{key}  {value} {query_name}")
        if query_name == key:
            sum_score = 0
            average = 0
            for item in value:
                sum_score = sum_score + item
            average = sum_score / len(value)
            print(format(average, ".2f"))



