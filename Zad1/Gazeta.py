def Newspaper():
    numb_of_characters = input()
    letters = {}

    for item in range(int(numb_of_characters)):
        letter, price = input().split()
        letters[letter] = int(price) 

    word = input()
    result = sum([letters[letter] for letter in word]) / 100

    print(result) 

Newspaper()