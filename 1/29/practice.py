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
print(np.mean(np.sort(student_scores,axis=0)[1:],axis=0))#doing this in python with loops is slow

#Task 5: Report the average scores of the top-3 assignments in which the students performed best on average
print("Average score of top three assignments: ")
#Task 5: Give the top-3 assignment average scores.
#expected outcome(shape): (3,) -i.e., 3 scores
#across each row, get the average(average per row, because each row is an assignment)
#-output: (10,) is shape(10 assignments)
#- get top 3 of these 10(sort them first)
print(np.sort(student_scores.mean(axis=1))[7:10][::-1])

#Task 6: Compute a curved score for each assignment and each student:
#i.e. take ach student and each assignment and divide the student's assignment
#score by the max score for that assignment across all students
#(new scores will be between 0 and 1; rescale them)

#Task 7: Count the number of assignments where at least one student got a 90 or above

#Task 8: Compute how similar each student is to every other: each student is a vector
# of assignment scores, so take each student and compute the euclidean distance
#between every other student(the diagonal of this distance matrix should be 0, 
#indicating each student is 0 distance from themselves).


