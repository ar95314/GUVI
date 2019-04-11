class checkcomposite:
  def notprime(self,w):
    for i in range(2,w):
      if w%i==0:
        print("yes")
        break
    else:
      print("no")
w=int(input())
d=checkcomposite()
d.notprime(n)
