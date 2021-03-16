letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  letter_list = list(letters)
  unique_letters = []
  for x in word:
    if x in letter_list and x not in unique_letters:
      unique_letters.append(x)
  return len(unique_letters)
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

