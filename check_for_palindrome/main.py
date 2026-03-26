def is_palindrome(word:str):
  cleaned = ""
  for char in word:
    if char.isalnum():
      cleaned += char.lower() 
  return cleaned == cleaned[::-1]
  

print(is_palindrome('hello'))
print(is_palindrome('racecaR'))