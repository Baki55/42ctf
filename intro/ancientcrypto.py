#First challenge:
#The Caesar cipher is used to encrypt the plain text.
#The key used here is 16.

cypher = "OKCI_DY_LBEDO_PYBMO"
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' ,'V', 'W', 'X', 'Y', 'Z']

for letter in cypher:
	if letter.isalpha():
		index = alphabet.index(letter) + 16
		if index > 25:
			index = index - 25 - 1
		print(alphabet[index])