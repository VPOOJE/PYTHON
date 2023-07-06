'''Assume that the below dictionary 
Digit_word = { 1 : “One”, 2 : “Two” , 3 : “Three” , 4 : “Four” , 5 : “Five” , 6 : “Six” , 7 : “Seven” , 8 : “Eight” , 9 : “Nine”}
Read the integer from the user and display it in words by considering the above dictionary.
Sample Input 
324
Sample Output
Three Two Four'''

Digit_word = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}
number = input("Enter an integer: ")
for digit in number:
    print(Digit_word[int(digit)], end=" ")
