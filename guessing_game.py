# https://djangocentral.com/creating-a-guessing-game-in-python/
import random

number = random.randint(1, 10)

player_name = input("Hello, What's your name?\nName: ")

print('okay! ' + player_name + ' Guess my number.\nRemember you have 5 tries')

number_of_guesses = 0

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
        break
if number_of_guesses == 6:
    print('You did not guess the number, The number was ' + str(number))
