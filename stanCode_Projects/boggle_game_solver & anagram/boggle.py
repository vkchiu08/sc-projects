"""
File: boggle.py
Name: Victoria
----------------------------------------
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
NUMBER = 4
import time

# global
Python_dict = {}			 # 把所有的字丟進一個字典，key是每個單字，value=1
Prefix_dict = {}			 # 把Python_dict裡面所有的字，拆成Prefix丟進另一個字典，key是每個單字的Prefix，value=1
Found_dict = {}				 # 把已經找到過的字丟到字典，避免有重複的字印出來
lst = []					 # 用來裝input的字母
valid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]		# 為4*4矩陣的16個字母製造一個開關，避免重複選取
Count = 0					 # 計算找到幾個字


def main():
	"""
	TODO:
	把輸入的4行字母,加入到lst裡面，製造出4*4的二維矩陣
	用兩個 for loop,讓找相連單字的起點會分別從16個不同點開始
	"""
	global lst
	read_dictionary()
	prefix_dictionary()
	for i in range(NUMBER):
		put = input(f'{i+1} row of letters: ')
		put.lower()						# Case insensitive
		if len(put) != 7:				# 假設字母跟字母中間會輸入空格，且最後的字母後面不會輸入空格是直接enter
			print('Illegal input')
			break
		ele = put.split()
		lst.append(ele)
	# 開始
	start = time.time()

	for i in range(NUMBER):
		for j in range(NUMBER):
			valid[i][j] = 1
			dfs(lst[i][j], i, j)
			valid[i][j] = 0
	print(f'There are {Count} words in total.')

	# 結束
	end = time.time()
	# 輸出結果
	print("執行時間：%f 秒" % (end - start))


def dfs(prefix, i, j):
	"""
	:param prefix: 已經串上去的字串
	:param i: 矩陣的橫軸(透過編碼，輔助判斷字母位置)
	:param j: 矩陣的縱軸(透過編碼，輔助判斷字母位置)
	"""
	global Python_dict, Prefix_dict, lst, valid, Count, Found_dict
	# 如果Prefix開頭不在字典內就不再往下找
	if prefix not in Prefix_dict:
		return
	# 印出找到的單字
	if prefix in Python_dict and len(prefix) >= 4 and prefix not in Found_dict:
		Found_dict[prefix] = 1
		print(f'Found "{prefix}"')
		Count += 1
	# 用recursive概念和8個if，判斷周圍的字母是否串上去
	# 左上
	if i-1 >= 0 and j-1 >= 0 and valid[i-1][j-1] == 0:
		valid[i-1][j-1] = 1
		dfs(prefix+lst[i-1][j-1], i-1, j-1)
		valid[i-1][j-1] = 0
	# 上
	if j-1 >= 0 and valid[i][j-1] == 0:
		valid[i][j-1] = 1
		dfs(prefix+lst[i][j-1], i, j-1)
		valid[i][j-1] = 0
	# 右上
	if i+1 < NUMBER and j-1 >= 0 and valid[i+1][j-1] == 0:
		valid[i+1][j-1] = 1
		dfs(prefix+lst[i+1][j-1], i+1, j-1)
		valid[i+1][j-1] = 0
	# 左
	if i-1 >= 0 and valid[i-1][j] == 0:
		valid[i-1][j] = 1
		dfs(prefix+lst[i-1][j], i-1, j)
		valid[i-1][j] = 0
	# 右
	if i+1 < NUMBER and valid[i+1][j] == 0:
		valid[i+1][j] = 1
		dfs(prefix+lst[i+1][j], i+1, j)
		valid[i+1][j] = 0
	# 左下
	if i-1 >= 0 and j+1 < NUMBER and valid[i-1][j+1] == 0:
		valid[i-1][j+1] = 1
		dfs(prefix+lst[i-1][j+1], i-1, j+1)
		valid[i-1][j+1] = 0
	# 下
	if j+1 < NUMBER and valid[i][j+1] == 0:
		valid[i][j+1] = 1
		dfs(prefix+lst[i][j+1], i, j+1)
		valid[i][j+1] = 0
	# 右下
	if i+1 < NUMBER and j+1 < NUMBER and valid[i+1][j+1] == 0:
		valid[i+1][j+1] = 1
		dfs(prefix+lst[i+1][j+1], i+1, j+1)
		valid[i+1][j+1] = 0


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global Python_dict
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip('\n')
			Python_dict[line] = 1


def prefix_dictionary():
	global Prefix_dict, Python_dict
	for s in Python_dict:
		for i in range(len(s)):
			Prefix_dict[s[0:i+1]] = 1


if __name__ == '__main__':
	main()
