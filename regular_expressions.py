import re



#def main():
    #print(parse(input("HTML: ")))


def parse(s):
  # <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe
  #output : https://youtu.be/xvFZjo5PgG0
  if shorten := re.search(r'(www\.)?youtube.com/embed/(\w+)', s):
    return 'https://youtu.be/' + shorten.group(2)
    




#if __name__ == "__main__":
    #main()
print (parse("<iframe src='http://www.youtube.com/embed/xvFZjo5PgG0'></iframe"))