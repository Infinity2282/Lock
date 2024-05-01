def chapte_one():
    print("""
          __________________________
         /                         \\
        /                           \\
       [_____________________________]
       | ____________________________|
       || For open base login       ||
       || you need enter: base 228  ||
       ||___________________________||
       |_____________________________|
                     []    
                    /  \\   
                   /____\\  
    """)
    print("""
             __________________________
            /                         \\
           /                           \\
          [_____________________________]
          | ____________________________|
          || Enter command:            ||
          ||                           ||
          ||___________________________||
          |_____________________________|
                        []    
                       /  \\   
                      /____\\  
       """)
    command = input("Enter command:")

    if command == "base 228":
        mini_1()
    else:
        print("""
                     __________________________
                    /                         \\
                   /                           \\
                  [_____________________________]
                  | ____________________________|
                  || Err                       ||
                  ||                           ||
                  ||___________________________||
                  |_____________________________|
                                []    
                               /  \\   
                              /____\\  
               """)
        print("GAME OVER")



def start_game():
    print("Игра началась!")
    print("Integer Studio")
    print("          _____    1 person    ")
    print("        /       \       ")
    print("       |  O   O  |      ")
    print("       |    ^    |      ")
    print("        \ \___/ /      ")
    print("        \_______/      ")
    print("            |             ")
    print("          _____   2 person       ")
    print("        /_______\       ")
    print("       |  O   O  |      ")
    print("       |    ^    |      ")
    print("        \  ___  /      ")
    print("        \_______/      ")
    print("1 person: This is a modern person who is interested in cyber security.")
    print("2 person: This is a caveman who works as a blacksmith.")
    Enter = input("Press 'enter' ")
    chapte_one()

def mini_1():
    print("""
                  __________________________
                 /                         \\
                /                           \\
               [_____________________________]
               | ____________________________|
               ||   [ | ]          [ | ]    ||
               ||           ______          ||
               ||___________________________||
               |_____________________________|
                             []    
                            /  \\   
                           /____\\  
            """)

def show_instructions():
    print("Instructions:\n...")

print("╔═════════════════════╗")
print("║      Game menu      ║")
print("╠═════════════════════╣")
print("║  1. Start game       ║")
print("║  2. Instructions     ║")
print("║  3. Exit             ║")
print("╚═════════════════════╝")

while True:
    choice = input("Select an option: ")

    if choice == "1":
        start_game()
        break
    elif choice == "2":
        show_instructions()
        break
    elif choice == "3":
        print("Quitting the game...")
        break
    else:
        print("Incorrect choice. Please select option from 1 to 3.")


