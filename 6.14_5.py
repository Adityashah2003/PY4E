str = "X-DSPAM-Confidence: 0.8475"
new_str_1 = str.find(':')
new_str_2 = str[new_str_1 +1:]
new_word = float(new_str_2)
print(new_word)
