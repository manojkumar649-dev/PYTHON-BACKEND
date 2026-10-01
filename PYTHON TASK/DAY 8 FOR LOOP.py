

#TASK 1

word = "Python"

for i in range(len(word), 0, -1):
    print(word[:i])

#TASK 2


word = "python"

for i in range(1, len(word) + 1):
    print(word[:i])


#TASK 3

word = "python has biggest library"

words = word.split()

longest = words[0]
shortest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

    if len(i) < len(shortest):
        shortest = i

print("Longest word:", longest)
print("Shortest word:", shortest)

#TASK 4

s = "python is easy"

words = s.split()

for i in words:
    print(i.capitalize(), end=" ")













