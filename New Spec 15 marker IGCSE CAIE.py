# specimin IGCSE CAIE 2023 15 marker question
# set up arrays and variables needed
studentName = ["Bill", "Sarah", "Helen", "George"]
studentMark = [[75,68,88],[38,55,65],[90,79,88],[25,65,47]]
totalMarks = []
averageMark = []
#counters
distinctionNo = 0
meritNo = 0
passNo = 0
failNo = 0

subjectNumber = 3
classsize = len(studentName) # obvs
grade = "" # will be worked out later on

# CONTSTANTS - grade boundaries
DISTINCTION = 70
MERIT = 55
PASS = 40

# iteration, selection, totalling, counting and output used. Here working out total and average for each student 

for student in studentMark:
  totalMarks.append(sum(student))
  averageMark.append(round(sum(student)/subjectNumber,0))

# print to check working OK
print(totalMarks)
print(averageMark)

# now outputting required name, combined mark, avarage mark and grade awarded, also adding to disction/merit and pass counters, initialised at 0 above

for i in range (classsize):
  # dist/merit/pass check and add to counter
  if averageMark[i] >= DISTINCTION:
    grade = "Distinction"
    distinctionNo+=1
  elif averageMark[i] >= MERIT:
    grade = "Merit"
    meritNo +=1
  elif averageMark[i] >= PASS:
    grade = "pass"
    passNo += 1
  else:
    grade - "fail"
    failNo +=1
  print(studentName[i], " with a combined mark of ", totalMarks[i]," and an average of ", averageMark[i], " and a grade of ", grade)

print("There were ", distinctionNo, " distinctions")
print("There were ", meritNo, " merits")
print("There were ", passNo, " passes")
  