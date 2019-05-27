def count_vowels(word):
	count = 0
	vowels = ['a','e','i','o','u']
	for letter in word.lower():
		if letter in vowels:
			count += 1
	return count

#contoh
print(count_vowels("INDONESIAtanahAIRku"))
