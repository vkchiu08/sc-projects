"""
File: anagram.py
Name: Victoria
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# global
Python_list = {}              # 把所有的字丟進一個字典 key是每個單字 value=1


def main():
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        put = input('Find anagrams for: ')
        if put == EXIT:
            break
        # 開始
        start = time.time()
        find_anagrams(put)
        # 結束
        end = time.time()
        # 輸出結果
        print("執行時間：%f 秒" % (end - start))


def read_dictionary():
    global Python_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            Python_list[line] = 1


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    lst = []                                    # 把輸入的字的每個字母丟進一個字串,幫助排列組合
    for i in range(len(s)):
        lst.append(s[i])

    print('Searching...')
    counter = [0]                               # count anagrams 計算總共有找到幾個anagrams
    answer = []                                 # answer anagrams 把已經找到的anagrams丟進一個lst,避免有重複字出現的問題
    co = [0]                                    # 看HELPER被呼叫幾次
    helper('', lst, counter, answer, co)
    print(f'{sum(counter)} anagrams: {answer}')
    print(co)


def helper(s, lst, counter, answer, co):
    global Python_list
    co[0] += 1
    if lst == []:                                       # 當要查找的字母都被取出來後，lst==[]代表已經組合出一種字
        if s in Python_list and s not in answer:        # 測試組合出來的字，是不是出現在字典裡，且沒有被加入answer內再print
            print(f'Found: {s}')
            counter[0] += 1
            answer.append(s)
            print('Searching...')
        else:
            return
    else:
        for i in range(len(lst)):
            c = lst.pop(0)                              # 把要查找的字母c依照順序拿出來,串到字串's'上
            helper(s+c, lst, counter, answer, co)       # 用recursive製造出i!的單字組合
            lst.append(c)                       # 當recursive跑完跳出來(測試完其中一種組合是否存在字典後)再把pop的字母加回去lst中




if __name__ == '__main__':
    main()
