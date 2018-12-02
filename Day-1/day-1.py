def count_frequency(filename):
	with open(filename) as infile:
		count = 0
		for line in infile:
			count += int(line.strip())

	return count

def count_frequency_two(filename):
	
		count = 0
		seen = {}
		while True:
			with open(filename) as infile:
				for line in infile:
					count += int(line.strip())
					if count in seen:
						print("length: " + str(len(seen)))
						return count
					else:
						seen[count] = True
						

print(count_frequency_two("input"))