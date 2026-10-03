#  2. Write a program to input any alphabet and check whether it is vowel or consonant.
char = input("Enter a character: ")
if(char =='a' or char =='A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O'or char == 'u' or char == 'U'): 
    print("It is vowel")
else:
    print("It is Consonant")


#  OR

if char in "aeiouAEIOU":
    print("It is vowel")
else:
    print("It is consonant")