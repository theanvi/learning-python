while True:
 print("===== STUDY TRACKER =====")
 print("1. Add Study Session")
 print("2. View Study History")
 print("3. Exit")
 try:
  choice =int(input("Enter your choice (1-3): "))
 except ValueError:
    print("Invalid input. please enter a number")
    continue

 if choice==1:
    subject=input("Enter subject name : ")
    hours=float(input("Enter number of hours studied : "))
    with open("study","a") as f:
      f.write("Subject : " +subject+"\n")
      f.write("Hours : "+str(hours)+"\n")
    
 elif choice==2:
    with open("study","r") as f:
        print(f.read())
 
 elif choice==3:
    print("Exiting the program. Goodbye!")
    break 
 else:
    print("Invalid choice. Please enter a number between 1 and 3.")
