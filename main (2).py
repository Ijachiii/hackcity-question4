def runningsum(x):
  x = list(x)
    
  lst = []
  for n in x:
    if n == x[0]:
      lst.append(n)
    else:
      n = n + lst[-1]
      lst.append(n)
  print(lst)
      
runningsum([1,2,3,4])