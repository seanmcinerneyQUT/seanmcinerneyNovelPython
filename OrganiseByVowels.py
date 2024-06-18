fruits = ["Apple", "Banana", "Cherry", "Melon", "Strawberry", "Orange"]

def vowel_count(input_word):
    c=0
    for char in input_word:
        if char.lower() in "aeiou":
            c+=1
    return c

sorted_fruits = sorted(fruits, key = vowel_count)

print(sorted_fruits)
    