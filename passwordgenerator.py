import random
import string

def pwd_length(num_length):
  return random.sample(string.ascii_letters, num_length)

def pwd_digits(digits_length):
  digits = []
  for i in range(digits_length):
    digits.append(str(random.randint(1, 10)))
  return digits

def pwd_symbols(symbol_length):
  symbols = []
  for j in range(symbol_length):
    symbols.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))
  return symbols

print("how many characters would you like to use ? (DO NOT USE LESS THAN 8)")
str_cnt = input()
print("how many digits would you like to use ? (DO NOT USE LESS THAN 1)")
num_cnt = input()
print("how many special characters would you like to use ? (DO NOT USE LESS THAN 1)")
s_chars_cnt = input()

pwd = pwd_length(int(str_cnt)) + pwd_digits(int(num_cnt)) + pwd_symbols(int(s_chars_cnt))

random.shuffle(pwd)

print('Generated Password is :')
print(''.join(pwd))
