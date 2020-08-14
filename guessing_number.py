#! /usr/bin/env python3

from random import randint
from time import sleep
import sys
# writing effect function
def write(s):
    for char in s:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
print('welcome to guessing number game 1.1')
write('|||||||||||||||||||||||||||||||||||')
print('\n\n\n')
write('You have to guess the number\n\n')

num3 = 1
	
while True:
	try:
		num = randint(1,20)
		print('enter e for exit')
		number = input('enter the number between 1 to 20\n\n')
		if number == 'e':
			break
		num2 = int(number)
		while True:
			if num2 > 20:
				print('out of range')
				num2 = int(input('enter again'))
			elif num == num2:
				print('wow! correct guess\n') 
				write('number of time you tried-')
				print(num3,'\n\n\n')
				break
		        
			elif num < num2:
				if num2-num > 5:
					print('too high\n\n')
					if num2-num < 5:
						print('little high\n\n')
				num2 = int(input('guess again\n'))
				num3+=1
			elif num > num2:
				if num-num2 > 5:
					print('too low\n\n')
		                
				if num-num2 < 5:
					print('little low\n\n')
				num2 = int(input('guess again\n'))
				num3+=1
			elif num2 == 'e':
				print('thank you for play')
				break
	except ValueError:
		print('invalid input :(')
		continue
input()
