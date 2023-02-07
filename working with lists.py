#for looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great performance!")
    print("I can not wait for the next trick" , magician.title() + '.')
    print("Thankyou that was a great magic show" , magician.title() + '.\n')


letters = ['a', 's', 'd', 'f', 'g'] 
print(letters)
for letter in letters:
    print(letter.title() + ',' + " These are the letters at the best ") 
    print("Everone starts learning english by these letters", letter.title() + '.')
    print("Thanks for showing intrest in these letters!" + '.\n')  

#forgetting to indent additional lines
magicians = ['david', 'james', 'alice']
for magician in magicians:
    print(magician.title()+"That was a great trick" + '.')
print("I cant wait for the next trick" + magician.title()+ '.\n')
print("Thankyou everyone that was a great show." + magician.title()+'.\n')

#Making numerical lists
for value in range(1,5):
    print(value)

#using range() to make list of number
numbers = list(range(1,5))
print(numbers)    

even_number = list(range(2,11,2))
print(even_number)

odd_number = list(range(3,11,3))
print(odd_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)    

digits =  [1, 2, 3, 5, 6, 7]
print(min(digits))
print(max(digits))
print(sum(digits))

#slicing list
letters = ['a', 'b', 'c', 'd', 't', 'g']
print(letters[0:4])
print(letters[1:4])
print(letters[:4])
print("Here are my first three letters: ")
for letter in letters[:3]:
    print(letters)

#copying list
my_food = ['pizza', 'carrot', 'cake']
friends_food = my_food

print("my favourite food are:")
print(my_food)

print("my friends food are:")
print(friends_food)

my_food.append('chocolate')
print(my_food)
friends_food.append('lava')
print(friends_food)