import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  #print(quotes)
  #print(quotes[0])
  #print(quotes[13])
  print(quotes[rnd])

if __name__== "__main__":
  primary()