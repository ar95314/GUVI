def main():
  l=int(input(""))
  u=int(input(""))
  for num in range (l,u+1):
    if num>1:
       for i in range (2,num):
           if num%i==0:
              break
           else:
              print(num)
int __name___ == '__main__': 
main()
