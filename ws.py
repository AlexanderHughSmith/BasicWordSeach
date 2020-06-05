def horizontal(ans,puzzle):
	for x in range (0,len(puzzle)):
		temp = "".join(map(str,puzzle[x]))
		if temp.find(ans) > -1:
			print("Right to Left: ("+str(temp.find(ans)+1)+","+str(x+1)+")")
			return True
		if temp.find(ans[::-1]) > -1:
			print("Left to Right (Backwards): ("+str(temp.find(ans[::-1])+1)+","+str(x+1)+")")
			return True
	return False


def vertical(ans, puzzle):
	for x in range(0, len(puzzle[0])):
		temp = []
		for j in range(0, len(puzzle)):
			temp.append(puzzle[j][x])
		temp = "".join(map(str,temp))
		if temp.find(ans) > -1:
			print("Top to Bottom: ("+str(x+1)+","+str(temp.find(ans)+1)+")")
			return True
		if temp.find(ans[::-1]) > -1:
			print("Bottom to Top: ("+str(x+1)+","+str(temp.find(ans[::-1])+len(ans))+")")
			return True
	return False
	
def solve(ans,puzzle):
	Found = False
	while not Found:
		if horizontal(ans,puzzle):
			break
		if vertical(ans,puzzle):
			break
		else:
			print("Not found in puzzle")
			break

l1 = "csmfsnow"
l2 = "ocbrcsmh"
l3 = "aaqoobvk"
l4 = "treslfei"
l5 = "wfotdqsz"
l6 = "lwkyqice"
l7 = "vqwigloo"
l8 = "hwintern"
puzzle = [1,2,3,4,5,6,7,8]
puzzle[0] = list(l1)
puzzle[1] = list(l2)
puzzle[2] = list(l3)
puzzle[3] = list(l4)
puzzle[4] = list(l5)
puzzle[5] = list(l6)
puzzle[6] = list(l7)
puzzle[7] = list(l8)

def print_puzzle(puz):
	for x in range (0,len(puz)):
		print(puz[x])
print_puzzle(puzzle)

while True:
	word = input("What word are you looking for: ")
	solve(word,puzzle)
