import random

while True:
 choice=input('Roll the dice? (y/n): ').lower()
 if choice == 'y':
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    total= num1 + num2
    print(f'({num1}, {num2}) → Total: {total}')
 elif choice== 'n':
    print('Thanks for playing!')
    break
 else:
   print('Invalid choice! Please enter y or n.')