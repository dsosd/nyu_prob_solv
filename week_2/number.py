def main():
	'''
	Assignment: Write the game of 10 questions for a number between 1 and 1000 in python3.
	Is the number equal, greater than, or less than x?
	People have to answer something like "equal, less, greater"
	Initially, lower bound is 1 and upper bound is 1000.
	Each time you get an answer, you either raise the lower bound
	or lower the upper bound.
	If the respondent is inconsistent, tell them that they are lying.
	But be nice about it.
	'''
	bounds=[1, 1000 + 1]
	while (bounds[1]-bounds[0] > 1):
		slice_num=int(sum(bounds)/2)
		print("Is the number (e)qual, (g)reater than, or (l)ess than " + str(slice_num) + "?")
		response=input()
		if response in ["equal", "e"]:
			bounds[0]=slice_num
			bounds[1]=bounds[0]+1
			break
		elif response in ["greater", "g"]:
			bounds[0]=slice_num+1
		elif response in ["less", "l"]:
			bounds[1]=slice_num
	if (bounds[1]-bounds[0]==1):
		print("Your number is " + str(bounds[0]) + ". (Y/n)")
		response=input()
		if response=="n":
			print("A certain individual is mistaken in recalling a numerical constant.")
		elif response in ["", "y"]:
			print("This was expected.")
		else:
			print("invalid input")
	else:
		raise AssertionError()

if __name__=="__main__":
	main()
