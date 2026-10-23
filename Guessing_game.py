import random
secret_number = random.randint(1,10)

guess_counter = 0


print("HO HO HO WELCOMEE TO THE LUCKY NUMBERS!!")
while True:
    guess = int(input("Guess A Number from 1 to 10\n")) 
    guess_counter=guess_counter +1
    if guess>secret_number:
        print('Nah thats HIGHH TWIN!!')
    elif guess==secret_number:
        print("OMGG YOU WINNN(You didnt cheat did you?)")
        print('Took you',guess_counter,"tries.")
        break
    else:
        print("Nah Nah, Youre loww TWINN")

        