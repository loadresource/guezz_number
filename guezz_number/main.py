import random
import time



def main():
    print("""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have select chances to guess the correct number.
    """)

    print("""
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
          """)


    exi = ""

    while exi != 'Q':
        trys = 0
        cycles = 1

        guessing_number = random.randint(1, 100)

        while True:
            try:
                input_difficult = int(input("Select your difficulty level (1-3): "))
                if input_difficult in [1, 2, 3]:
                    break
                else:
                    print("Please enter 1, 2, or 3 only!")
            except ValueError:
                print("Invalid input! Please enter a number (1, 2, or 3).")

        if input_difficult == 1:
            trys = 10
        elif input_difficult == 2:
            trys = 5
        elif input_difficult == 3:
            trys = 3

        ini = time.time()
        while cycles <= trys:
            cycles += 1

            while True:
                try:
                    choice_number = int(input("Enter your guess: "))
                    if 1 <= choice_number <= 100:
                        break
                    else:
                        print("Please enter a number between 1 and 100!")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            if choice_number < guessing_number:
                  print(f"Incorrect! The number is less than {choice_number}")
            elif choice_number > guessing_number:
                  print(f"Incorrect! The number is greater than {choice_number}.")
            elif choice_number == guessing_number:
                  print(f"Congratulations! You guessed the correct number in {cycles} attempts.")
                  break
              
        end = time.time()
        print(f"Guessing time in {round(end - ini)}sec")

        while True:
            try:
                exi = input("press Q to exit o Y for repeat the game:").upper()
                if exi in ['Q','Y']:
                    break
                else:
                    print("plz insert Q or Y")
            except ValueError:
                print("insert only character Q or Y")

if __name__=="__main__":
    main()