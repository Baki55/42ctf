
f = open("ciphertext", "r")
cipher = f.read()
for symb in cipher:
	if symb == '┼':
		print("C")
	elif symb == '¿':
		print("T")
	elif symb == '¤':
		print("F")
	elif symb == '║':
		print("E")
	elif symb == '±':
		print("A")
	elif symb == '¥':
		print("O")
	elif symb == '╣':
		print("N")
	elif symb == '╗':
		print("I")
	elif symb == '╝':
		print("H")
	elif symb == '═':
		print("S")
	else:
		print(symb)