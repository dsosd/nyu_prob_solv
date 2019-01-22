import sys

def read_and_repeat():
	i=0
	with open("test_data") as file_:
		for line in file_:
			for j in range(2):
				print(str(i+j) + " " + line[:-1])
			i+=2

def map_word_to_line():
	word_to_lines={}
	with open("test_data") as file_:
		i=1#1-indexed lines
		for line in file_:
			for word in line.split():
				if word_to_lines.get(word) is None:
					word_to_lines[word]=[i]
				else:
					word_to_lines.get(word).append(i)
			i+=1
	print(word_to_lines)

def main():
	if len(sys.argv)!=2:
		print("bad args")
		return
	if sys.argv[1]=="0":
		read_and_repeat()
	elif sys.argv[1]=="1":
		map_word_to_line()

if __name__=="__main__":
	main()
