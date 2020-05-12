FROM = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,.'"
TO = "I7AOwhLWeKvj8qNksRxEi UpfQm4BP9FXZy'aHr162TY5o3tnVuCG,lgbz0M.SDcJd"
REVERSE_SUBSTITUTION = ''.maketrans(TO, FROM)

def decrypt(message, substitution_table):
  """Decrypts the message once using the given translation table."""
  return message.translate(substitution_table)

# The answer to question 1 has been encrypted. 
message = ".KrsUIfRrcsQJsy8rfQMJIsdsMfsGW8WWMrfGN"

for i in range(0,100,1):

# This decrypts the message once, you'll need to do this 100 times in a loop to reveal the answer
  message = decrypt(message, REVERSE_SUBSTITUTION)
  i +=1
  continue

print(message)

