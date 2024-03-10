'''always split into tokens by using x = line.split(), here x is a list
with open("data.txt", "r") as file:
  lines = file.readlines()  # lines is a list of strings

for eachline in lines:
  words = eachline.split()  # words is a list of words (tokens) from the given line, stored as eachline
  # Process the words in the list
