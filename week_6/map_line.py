def extend(data):
	return "_".join(data)

def main():
	n=3

	with open("test_data") as file_:
		for line in file_:
			line=line[:-1]
			print(len(line), line)
			data=line.split()
			if len(data)-n>=0:
				#processes each consecutive n elements in the list in order
				extended_data=map(extend, [data[i:i+n] for i in range(len(data)-n +1)])
				for it in extended_data:
					print(it)
			else:
				print(line)
			print()

if __name__=="__main__":
	main()
