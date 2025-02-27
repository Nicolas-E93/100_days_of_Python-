# Python built-in function sum
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
total_exam_score = sum(student_scores)
print(total_exam_score)

# We can create this built-in function by using a for loop
sum = 0
for sum_score in student_scores:
    sum += sum_score
print(sum)

# Max built-in function using for loops
max_score = 0
for result in student_scores:
    if result > max_score:
        max_score = result
print(max_score)