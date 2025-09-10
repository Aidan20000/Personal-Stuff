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

int main() {
    return 0;
}