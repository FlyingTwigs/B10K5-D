def count_vowels(word):
    count = 0
    for letters in word:
        if (letters == 'a' or letters == 'e' or letters == 'i' or letters == 'u' or letters == 'o' or letters == 'A' or letters == 'I' or letters == 'U' or letters == 'E' or letters == 'O'):
            count += 1

    return count

#contoh
print(count_vowels("INDONESIAtanahAIRku"))
