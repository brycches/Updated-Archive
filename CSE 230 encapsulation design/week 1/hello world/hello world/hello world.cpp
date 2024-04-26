// hello world.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <conio.h>
#include <string>
using namespace std;


/*************************
* pause the program
*************************/

void pause()
{
   char c;
   c = _getch();

}

/**********************************************
* get an integer from the user and return it
**********************************************/

int getint()
{
   int number;
   cout << "what is your favorite integer? ";
   cin  >> number;
   cin.ignore();
   return number;

}
/**********************************************
* get a string from the user and return it
**********************************************/
string getstring()
{
   string word;
   cout << "what is your favorite word? ";

   //cin >> word
   getline(cin, word);

   return word;

}
/**********************************************
* get a float from the user and return it
**********************************************/

float getfloat()
{
   float decimals;
   cout << "what is your favorite floating point number? ";
   cin  >> decimals;
   // Wrong>> getline(cin, decimals);

   return decimals;

}
/**********************************************
* display the given inputs
**********************************************/
void display(int number, string word, float number2)
{
   cout << "Your favorite number is: " << number  << "\n";
   cout << "Your favorite word is : "  << word    << "\n";
   cout << "Your favorite float is : " << number2 << "\n";

}

/**********************************************
* Display hello world, then run all functions.
**********************************************/
int main()
{
   std::cout << "Hello World!\n";

   pause();
   /*
   char data[256];
   cin >> data;

   char line[256];
   cin.getline(data, 256);

   char c;
   c = _getch();
   */

   //getchar();

   /*
   int integer;

   cout << "Give me an integer: ";
   cin >> integer;

   string words;

   cout << "give me a string: ";
   cin >> words;

   float decimals;

   cout << "give me a float: ";
   cin >> decimals;

   cout << "your answers were: " << integer << words << decimals << endl;
   */

   int    number  = getint   ();
   string word    = getstring();
   float  number2 = getfloat ();

   display(number, word, number2);


}