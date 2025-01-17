import random

people = {
    "Neymar, Footballer" : 200000000,
    "Cristiano Ronaldo, Footballer" : 526000000,
    "Lionel Messi, Footballer" : 413000000,
    "Carolina Samani, Model" : 418000,
    "Kim Kardashian, Entrepreneur" : 338000000,
    "Ariana Grande, Artist" : 347000000,
    "Tristan Tate, Influencer" : 2200000,
    "Joe Rogan, Comedian" : 16000000,
    "Barack Obama, Politician" : 35600000,
    "Deepika Padukone, Actor" : 70800000,
    "The Weeknd, Artists" : 47100000,
    "Lebron James, Basketballer Player" : 140000000 
}

score = 0
correct = True
person_a, value_a = random.choice(list(people.items()))
people.pop(person_a)

while correct:
    person_b, value_b = random.choice(list(people.items()))
    people.pop(person_b)
    print(f"Compare A: {person_a}")
    print(f"Against B: {person_b}")
    choice = input("Who has more followers? Type 'a' or 'b'. ")
    if choice == 'a' and value_a > value_b:
        score += 1
    elif choice == 'b' and value_b > value_a:
        score += 1
        person_a = person_b
        value_a = value_b
    else:
        correct = False
print(f"Sorry thans wrong. Score: {score}")



