# Get words from "words.txt" and divide into 9 level word lists.

# --------- Read text file ---------- #
with open("words.txt") as file:
    contents = file.readlines()

# --------- Strip white space ---------- #
stripped_words = []
for word in contents:
    stripped_words.append(word.strip())
# print(stripped_words)

# --------- Sort words in order by length (Ascending) ---------- #
sorted_words = sorted(stripped_words, key=len)
# print(sorted_words)

# --------- Min, Max length ---------- #
min_len = len(sorted_words[0])
max_len = len(sorted_words[-1])
# print(min_len)  # 2
# print(max_len)  # 16

# --------- number of all words ---------- #
# print(len(sorted_words))  # 4319
# print(len(sorted_words) / 9)  # 479.8888888888889

# --------- divide words into 9 levels ---------- #
dividing_nums = []
num = 0
for _ in range(9):
    num += 480
    dividing_nums.append(num)
# print(dividing_nums)  # [480, 960, 1440, 1920, 2400, 2880, 3360, 3840, 4320]

level1 = sorted_words[:dividing_nums[0]]
level2 = sorted_words[dividing_nums[0]:dividing_nums[1]]
level3 = sorted_words[dividing_nums[1]:dividing_nums[2]]
level4 = sorted_words[dividing_nums[2]:dividing_nums[3]]
level5 = sorted_words[dividing_nums[3]:dividing_nums[4]]
level6 = sorted_words[dividing_nums[4]:dividing_nums[5]]
level7 = sorted_words[dividing_nums[5]:dividing_nums[6]]
level8 = sorted_words[dividing_nums[6]:dividing_nums[7]]
level9 = sorted_words[dividing_nums[7]:]

# print(len(words_level1))  # 480
# print(len(words_level2))  # 480
# print(len(words_level3))  # 480
# print(len(words_level4))  # 480
# print(len(words_level5))  # 480
# print(len(words_level6))  # 480
# print(len(words_level7))  # 480
# print(len(words_level8))  # 480
# print(len(words_level9))  # 479

# print(words_level1[-1])  # hurt
# print(words_level2[0])  # nine

ALL_LEVEL_WORDS_LIST = [level1, level2, level3, level4, level5, level6, level7, level8, level9]
# print(word_list)
# print(len(word_list))  # 9
