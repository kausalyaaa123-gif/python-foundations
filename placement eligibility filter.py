student_name=input("Enter your name")
cgpa=float(input("Enter your cgpa"))
active_backlogs=input("enter True if you have backlogs or False if not").strip().title()
certifications_count=int(input("Enter your number of certifications"))
if cgpa>=7.5 :
    if active_backlogs=="False":
        if certifications_count >=1:
            print("Congratulations"+" "+student_name+", you are eligible for the interview round!")
        else:
            print("Rejected: more certifications need to be done")
    else:
        print("Rejected: Clearance of backlogs required.")
else:
    print("Rejected: cgpa is too low")
