# Write your x_length_words function here:
def x_length_words(sentence,x):
  word_list = sentence.strip().split()
  for word in word_list:
    if len(word) >= x:
      pass
    else:
      return False
  return True  

    
    
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True