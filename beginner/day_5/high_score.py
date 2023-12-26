
student_scores = input().split()
num_students = len(student_scores)

# Convert scores to int
for n in range(0, num_students):
  student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]

for score in student_scores:
  if highest_score < score:
    highest_score = score

print(f"Highest score is: {highest_score}")
    
