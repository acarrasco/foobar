def in_base_3(n):
	digits = []
	while n:
		digits.append(n%3)
		n /= 3
	return digits

def balance(weights):
	balanced = []
	carry = 0
	for w in weights:
		x = w + carry
		if x < 2:
			balanced.append(x)
			carry = 0
		elif x == 2:
			balanced.append(-1)
			carry = 1
		elif x == 3:
			balanced.append(0)
			carry = 1
	if carry:
		balanced.append(carry)
	return balanced

rebase = {
	-1 : 'L',
	 0 : '-',
	 1 : 'R'
}

def answer(x):
	digits = in_base_3(x)
	return [rebase[w] for w in balance(digits)]
