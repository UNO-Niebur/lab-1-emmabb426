#FirstProgram.py
#Name:Emma Barnes
#Date:01/22/2026
#Assignment: Lab 01

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  user_name = input("Please give your name: ")
  #Use the user's name in the program.
  print(f"The user's name is {user_name}.")
  #Ask the user for their age.
  age = int(input("Please give your age: "))
  #Tell the user what year they were born in.
  print(f"You were born in {2025-age}")
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
