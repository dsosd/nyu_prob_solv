def main():
	with open("test_data") as file_:
		for line in file_:
			print(line[:-1])
			print(sum(map(float, line.split())))

if __name__=="__main__":
	main()
