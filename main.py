from test import test

def reverse(string):
  new_string = ""
  s_len = len(string)
  i = s_len - 1
  while len(new_string) < s_len:
    new_string += string[i - s_len]
    i -= 1
  return new_string

def mirror(string):
  return string + reverse(string)

def remove_letter(letter, string):
  n_string = ""
  for char in string:
    if char == letter:
      continue
    n_string += char
  return n_string

def is_palindrome(string):
  return string == reverse(string)


def count(sub, string):
  count = 0
  start = 0
  found = 0
  while found != -1:
    found = string.find(sub, start)
    if found >= 0:
      count += 1
      start = found + 1
      #print(found)

  return count

def remove(sub, string):
  n_string = ""
  start = string.find(sub)
  if start == -1:
    return string
  end = start + len(sub)
  n_string = string[0:start] + string[end:]
  return n_string

def remove_all(sub, string):
  #n_string = ""
  x = count(sub, string)
  n_string = string
  for i in range(x):
    n_string = remove(sub,n_string)
  #print(n_string) 
  return n_string

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
