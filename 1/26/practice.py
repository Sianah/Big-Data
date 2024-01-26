import numpy as np

student_scores = np.load("student_scores.npy")
#functions: np.sum, np.sort, np.flip, np.mean, np.min, np.max,

print(student_scores)
#Task 1: Compute every student's mean assignment score
print("Student's mean scores: ")
print(student_scores.mean(axis = 0))
#Task 2: Compute the mean score for each assignment(across all students)
print("Assignment's mean score: ")
print(student_scores.mean(axis = 1))
#Task 3: Compute the global mean score
print("Global mean score: ")
print(student_scores.mean())
#Task 4: Drop the lowest assignment grade for each student, then compute their mean assignment score
print("Mean score of each student after lowest assignment grade is dropped: ")
arr2 = student_scores.min(axis=0)
arr3 = student_scores-arr2
print(arr3)
#Task 5: Report the average scores of the top-3 assignments in which the students performed best on average
print("Average score of top three assignments: ")
assignment_average = student_scores.mean(axis = 1)
