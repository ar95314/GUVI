n = input()
if ((n>='a' and n<='z')or(n>='A' and n<='Z')):
    if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U' ):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
