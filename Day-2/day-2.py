def checksum_1(filename):
	with open(filename) as infile:

		count_2 = 0
		count_3 = 0

		for line in infile:
			dico = {}
			two = False
			three = False

			for char in line:
				if char not in dico:
					dico[char] = 1
				else:
					dico[char] += 1

			for char in dico:
				if dico[char] == 2 and two == False:
					count_2 += 1
					two = True
				if dico[char] == 3 and three == False:
					count_3 += 1
					three = True


	return count_2 * count_3

def checksum_2(filename):
	with open(filename) as infile:

		lines = infile.readlines()

		differ = []

		for id_1 in lines:
			id_1 = id_1.strip()
			for id_2 in lines:
				id_2 = id_2.strip()
				if id_1 == id_2:
					continue

				change = 0

				for c_1, c_2 in zip(id_1, id_2):
					if c_1 != c_2:
						change += 1

				if change == 1:
					differ.append((id_1, id_2))

	out = ""
	for c1, c2 in zip(differ[0][0], differ[0][1]):
		if c1 == c2:
			out += c1
	return out

print(checksum_2("input"))