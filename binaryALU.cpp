#include <iostream>

// Half and full adder function
int halfAdd(int num1, int num2){
    //Initializes sum and carry variables
    int sum = 0, carry = 0;

    //Handles determining the sum for the two binary digits 
    //This is an xor gate along with an and gate for carry
    if(num1 == 1 || num2 == 1){
        sum = 1;
    }
    if(num1 == 1 && num2 == 1){
        sum = 0;
        carry = 1;
    }

    return sum, carry;
}

int fullAdd(int num1, int num2, int carry){
    int newCarry = 0;
    int insideSum, insideCarry = halfAdd(num1, num2);
    int newSum, secondInsideCarry = halfAdd(insideSum, carry);

    if(insideCarry == 1 || secondInsideCarry == 1){
        newCarry = 1;
    }
    return newSum, newCarry;
}

int halfSubtract(int num1, int num2){
    //This does num1 - num2
    int diff = 0, borrow = 0;
    if(num1 == 1 || num2 == 1){
        diff = 1;
    }
    if(num1 == 1 && num2 == 1){
        diff = 0;
    }

    //A not gate for num1
    if(num1 == 1){
        num1 = 0;
    }else {
        num1 = 1;
    }

    //Sets borrow to 1 if youre subtracting 1 from 0
    if(num1 == 1 && num2 == 1){
        borrow = 1;
    }
    return 0;
}

int main() {
    return 0;
}