def check(num):
  dividor = 1
  index = 1
  while dividor % num != 0:
    dividor += 10**index
    index += 1
  return len(str(dividor))

while True:
  try:
    n = int(input())
    _len = check(n)
    print(_len)
  except:
    break