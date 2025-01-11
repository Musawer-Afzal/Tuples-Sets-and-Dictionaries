# Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
# Show every students record in form of tuples if matches all required criteria.
# It is assumed that there will be only one primry skill.
# If no such candidate found, print No such candidate
# Input:
# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020
# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022



details = []
n = int(input("Enter No of records: "))
for i in range(n):
    print("Enter Details of student", i+1)
    name = input("Enter name of Student: ")
    skill = input("Enter Skill: ")
    education = input("Enter Higher Education: ")
    year = input("Enter Year of Graduation: ")
    details.append((name,skill, education, year))

print("Enter Job Role Requirement")
job_skill = input("Enter Skill: ")
job_education = input("Enter Higher Education: ")
job_year = input("Enter Year of Graduation: ")

print(details)

found = False
for i in details:
    if i[1] == job_skill and i[2] == job_education and i[3] == job_year:
        print("Potential Candidate: ", i)
        found = True

if found == False:
    print("No such candidate")