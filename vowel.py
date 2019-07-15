num1 = input()
if ((num1>='a' and num1<='z')or(num1>='A' and num1<='Z')):
    if(num1 == 'a' or num1 == 'e' or num1 == 'i' or num1 == 'o' or num1 == 'u' or num1 == 'A' or num1 == 'E' or num1 == 'I' or num1 == 'O' or num1 == 'U' ):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
