import math

def prompt_bool(prompt):
	while True:
		response=input(prompt)
		if response in ["yes", "y", "Y", "1"]:
			return 1
		elif response in ["no", "n", "N", "0"]:
			return 0
		else:
			print("bad input")

def num_suffix(num):
	if num%100>=11 and num%100<=19:
		return "th"
	if num%10==1:
		return "st"
	elif num%10==2:
		return "nd"
	elif num%10==3:
		return "rd"
	else:
		return "th"

def power_of_2(num):
	while not num%2 and num>1:
		num>>=1
	return num==1

def c_to_p(num):#codeword bit to parity bit
	return int(math.log(num+1, 2)) if power_of_2(num+1) else -1

def c_to_d(num):#codeword bit to data bit
	return num-1-math.floor(math.log(num, 2)) if not power_of_2(num+1) else -1

def calc_hamming(data):
	codeword=[]
	codeword_size=len(data)+math.ceil(math.log(len(data), 2))
	parity=[]
	for i in range(codeword_size):
		p_val=c_to_p(i)
		d_val=c_to_d(i)
		if p_val!=-1:
			codeword.append(0)#should not be used in this function. just filler data
		else:
			codeword.append(data[d_val])

	for i in range(math.ceil(math.log(len(codeword), 2))):
		curr_bit=0
		for j in range(len(codeword)):
			d_val=c_to_d(j)
			if ((j+1) >> i)%2 and codeword[j]:#((j+1) >> i)%2 identifies the data bits that the i-th parity bit covers
				curr_bit^=1#NOTE alternatively: x=~x BUT tricky pit
		parity.append(curr_bit)
	return parity

def main():
	#Hamming code [14, 10, 3]2
	hamming_n=14
	hamming_k=10

	data=[]
	parity=[]
	parity_prime=[]
	truth=[]
	print("1st bit is the MSB")

	for i in range(hamming_k):
		data.append(prompt_bool("Is the " + str(i+1) + num_suffix(i+1) + " bit in your number 1? "))
	for i in range(hamming_n-hamming_k):
		query="Did you lie on any of the following questions?"
		for j in range(hamming_n):
			d_val=c_to_d(j)
			if d_val!=-1 and ((j+1) >> i)%2:#((j+1) >> i)%2 identifies the data bits that the i-th parity bit covers
				query+= " " + str(d_val+1) + num_suffix(d_val+1) + ","
		if query[-1]==",":
			query=query[:-1]
		query+=" "
		truth.append(1^prompt_bool(query))

	parity_prime=calc_hamming(data)
	assert(len(parity_prime)==len(truth))
	parity=[(parity_prime[i] if truth[i] else 1^parity_prime[i]) for i in range(len(parity_prime))]

	error_sum=sum( [( parity[i]^parity_prime[i] )*pow(2, i) for i in range(len(parity))] )
	if error_sum:
		d_val=c_to_d(error_sum-1)#1-index vs 0-index
		if d_val!=-1:
			data[d_val]^=1
		else:
			parity[c_to_p(error_sum)]^=1
	print(sum( [data[i]*pow(2, len(data)-i-1) for i in range(len(data))] ))
	return

if __name__=="__main__":
	main()
