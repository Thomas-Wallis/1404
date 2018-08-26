name = input("Enter your name: ")
print("""(H)ello
(G)oodbye
(Quit""")
menu_choice = input(">>>").upper()
while menu_choice != "Q":
   if menu_choice == "H":
       print("Hello {}".format((name)))
   elif menu_choice == "G":
       print("Goodbye {}".format((name)))
   else:
       print("Invalid message")
   print("""(H)ello
(G)oodbye
(Quit""")
   menu_choice = input(">>>").upper()
print("END")