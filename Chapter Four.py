magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

for value in range(1, 5):
    print(value)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

squaresTwo = [value**2 for value in range(1, 11)]
print(squaresTwo)

# onemillion = []
# for value in range(1, 1000001):
#     onemillion.append(value)
