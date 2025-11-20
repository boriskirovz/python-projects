import random

gameOptions = ["камък", "ножица", "хартия"]
playerPlay = input("Choose камък, ножица, хартия (k/n/h): ")
computerPlay = random.choice(gameOptions)

match playerPlay:
    case "k":  playerPlay = "камък"    
    case "n":  playerPlay = "ножица"
    case "h":  playerPlay = "хартия"

print("Ти избра", playerPlay, "vs компютърът избра", computerPlay)
if playerPlay == computerPlay:
    print("Равенство!")
elif (playerPlay == "камък" and computerPlay == "ножица") or \
     (playerPlay == "ножица" and computerPlay == "хартия") or \
     (playerPlay == "хартия" and computerPlay == "камък"):
    print("Печелите!")
else:
    print("Губите!")