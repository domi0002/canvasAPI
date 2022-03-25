from canvasapi import Canvas

API_URL = "https://canvas.qub.ac.uk"
API_KEY = "enter the key that was generated from canvas"
courseID = <Fill up your course ID here - Numeric value>
assnID   = <Fill up your assignment ID here - Numeric value>

canvas = Canvas(API_URL,API_KEY)

course = canvas.get_course(courseID)

ass = course.get_assignment(assnID)

subms  = ass.get_submissions()

nStudents=143
ns=0

for s in range(0,nStudents):
    status=subms[s].workflow_state
    if status == "submitted":
        ns=ns+1
    
# Print the number of students who have currently submitted the assignment    
print(ns)    
