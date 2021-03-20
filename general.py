def splitStringToCharacters(string):
    return [char for char in string]




string = str(input("Enter phrase:"))

length=len(string)


# singlechars=(splitStringToCharacters(string))


# Calculating frequency of each letter
freq = {}
for asinglecharacter in string:
    if asinglecharacter in freq:
        freq[asinglecharacter] += 1
    else:
        freq[asinglecharacter] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(freq)


