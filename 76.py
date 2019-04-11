class checkcomposite:
  def notprime(self,n):
    for i in range(2,n):
      if n%i==0:
        print("yes")
        break
    else:
      print("no")
n=int(input())
c=checkcomposite()
c.notprime(n)
