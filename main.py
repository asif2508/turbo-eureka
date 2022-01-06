import math
import sys
def Duplicate_main():
    try:
        new =[]
        print("###############################")
        print("     DUPLICATION CALCULATOR    ")
        print("    Dev By Rakibul Hasan Asif     ")
        print("###############################")
        dup = input("Enter your list: ")
        duplicate = dup.split()
        for i in range(len(duplicate)):
            duplicate[i] = int(duplicate[i])
        sets = set(duplicate)
        undup = list(sets)
        new_list =[]
        for i in duplicate:
            new =  duplicate.count(i)
            if new > 1:
                new_list.append(i)
        new_list_1 = sorted(new_list)
        print("--------------------------------------------------------")
        print("Here is the total duplicate numbers from the given list:")
        print(f"->{new_list_1}")
        print("Here is the list without any duplicate number: ")
        print(f"->{undup}")
        print("--------------------------------------------------------")
        print("Thank you!")
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted!")
        sys.exit()
    except ValueError:
        print("Please enter a correct list!")
        sys.exit()
Duplicate_main()
try:
    while True:
        choice = input("Do you want to run it again?(y or n): ")
        if choice == 'y':
            Duplicate_main()
        elif choice == 'n':
            print("---------------------")
            print("Thanks for using me!")
            print("Have a Good Day :)")
            print("---------------------")
            sys.exit()
        else:
            print("Invalid Input!")
except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted!")
        sys.exit()
except ValueError:
    print("Please enter a correct choice!")




