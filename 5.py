def ganti_kata(word, toChange1, toChange2):
    result = ''
    for letters in word:
        if (letters != toChange1):
            result += letters
        else:
            result += toChange2

    return result

# contoh
print(ganti_kata("purwakerta", 'a', 'o'))
