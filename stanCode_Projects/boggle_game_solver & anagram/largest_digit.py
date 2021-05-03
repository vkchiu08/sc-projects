"""
File: largest_digit.py
Name: Victoria
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = abs(n)
	if n % 10 == n:
		return n
	else:
		j = n % 10
		if n % 1000/100 < j and n % 100/10 < j:
			return j
		return find_largest_digit((n-j)//10)




if __name__ == '__main__':
	main()
