import time
import sys

print("\033[90m-----------------------------\n     Grade Calculator\n-----------------------------\n\033[0m")
## collect student name
student_Name = str(input("What's your name? "))


## define a variable for total score
total_score =0;
##define a variable for average
average ="";
grade =""
score = 0;
grade_Arr = {"A":5.0,"B":4.0, "C":3.0, "D":2.0, "E":1.0, "F":1.0 }
score_comparisonArr = {}



  ##--- set a function for calculations---
  
def calc(val):
      ## calculate average
    average = round((total_score/val),2)
    print(f"\033[90m----\033[0m Your average score is \033[90m----\033[0m {average}")
    grade = ""
    ## set the grade
    if average >= 70 and average <= 100:
        grade = "A"      
    elif average >= 60 and average < 70:   
        grade = "B"
    elif average >= 50 and average < 60:
        grade = "C"
    elif average >=40 and average < 50:
        grade = "D"    
    elif average >=20 and average < 40:
        grade = "E"       
    elif average >=0 and average < 20:
        grade = "F"    
    
    word =  "###---- required data received ----###\n"
    
          
    for t in word:
           ##   sys.stdout.write(f"\r {word}{t}")
              sys.stdout.write(f"\r{' '*1}")
             ## sys.stdout.write(f"{t}")
              print(t,end="",flush=True)
              sys.stdout.flush()
              time.sleep(0.05)
              word = "calculating average"
    
    print(f" \n   \033[90m Data Allocated\033[0m \n===================== \n Student Name: {student_Name}\n Average Score: {average}\n Grade: {grade}\n=====================")
    

while True:
    
   menu = print(f"\n  \033[90m Hi {student_Name}. Welcome onboard \033[0m \n ----------------------------\n  1.Calculate Course Grade\n  2.Grade Multiuple Assignments\n  3.Check Pass/Fail Status\n  4.Calculate GPA\n  5.Grade Comparison Tool\n  6.Exit\n ----------------------------\n")
   time.sleep(0.5)

   selected_no = int(input("\033[90m Select a number:-\033[0m "));



   if selected_no == 1:
    
       no_Assignment = input("Enter the amount of assignment:- ")
    
    
    
    ## use while instead of if to avoid unexpected digit error as while will keep running
       while not no_Assignment.isdigit():
           print("Enter a valid number")
           no_Assignment = input("Enter the amount of assignment:- ")
        
    
    ##course_Grade = ""
    
    
    
    ##score = int(input("\033[90m Enter the course score:-\033[0m "))
    
       no_Assignment = int(no_Assignment)                    
       print("°°°°°°°°°°°°°°°°°°°°°°")
       for i in range(no_Assignment):             
                score = input(f"\033[90m Enter score {i+1}:-\033[0m ")
             
             ##increase the total score by adding all scores together
                total_score+=int(score)
    
       calc(no_Assignment)
    
   elif selected_no == 2:
       print(f"°°°°°°°°°°°°°°°°°°°°°°")
       score = input(f"\033[90m Enter score(100):-\033[0m ")
       total_score += int(score)
       counter = 0    
       while True:
           counter +=1
           option = input("Do you want to continue (y/n):- ")
        
           if option == "n" or option == "no":
               average = round((total_score/counter),2)
            
               break
            
           else:
            
               score = input("\033[90m Enter score(100):-\033[0m ")
               total_score += int(score)
               continue
            
            ##perform calculations
       calc(counter)
        
   elif selected_no == 3:             
                passing_Score = int(input("Enter the passing score: "))
                student_Score = int(input("What did you score?: "))     
                if student_Score >= passing_Score:
                    print("♪---Passed---♪")      
                else:
                    print(f"  <•\033[90m---\033[0mYou can do better\033[90m---\033[0m•> \n   <•<\033[90mYou are just {passing_Score-student_Score} marks below \033[0m>•>")
                
   elif selected_no == 4:
                grade_Letter = str(input("select the grade point(A,B,C,D,E,F): "))
                if grade_Letter.isdigit():
                    grade_Letter = str(input("\033[94m please enter a valid grade point (A, B, C, D, E, F): \033[0m")).upper();
                while True:                                     
                    if grade_Letter in grade_Arr:
                        print(f":::: \033[90mThe equivalent grade is \033[0m {grade_Arr[grade_Letter]} ::::")
                        break                  
                   
                    else:                           
                       grade_Letter = str(input("\033[94m INVALID GRADE POINT\033[0m.\n Input a valid grade point (A, B, C, D, E, F): ")).upper()
                           
   elif selected_no == 5:
                    print("*** Grade Comparison ***")
                    amt_Compared = int(input("Enter the amount of students' results to be compared: "))
                    
                    #loop the amt
                
                    for num in range(amt_Compared):
                        score = input(f"Enter student {num+1} score: ")
                        score_comparisonArr[num] = score
                    #find the maximum score
                    sorted_Score = dict(sorted(score_comparisonArr.items(), key = lambda x: int(x[1]),reverse=True))
                   
                              ##print the header
                    print(f"\n\033[90mProcessed Data (Highest to smallest)\033[0m\n **______________________**\n")
                 
                    #loop the array
                    for i, (index,value) in enumerate(sorted_Score.items()):
                        
                            print(f"  \033[90mStudent {index+1} scored: {value} \033[0m|")            
                    print(" **______________________**")
             
                     
    