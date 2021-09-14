
secret_word = "giraffe"
guess = ""
count = 0
limit = 4
out = False

while guess != secret_word and not(out):
    if count < limit:
        guess = input("Enter guess: ")
        count += 1
    else:
        out = True

if out:
    print("Out of Guesses, you Lose!")
else:
    print("You Win!")