// Demo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
/**************************
* main
* There can only be one!
**************************/
int main()
{
   //place a user friendly message on the screen
   cout << "Hello World!" << endl; /* this is equal to: cout << "Hello World!\n"; */
   cout << "my address is:\n11732 W Fenchurch St.\nBoise, ID, 83709\n";



   //Puts $931.12 on the screen.
   double dollars = 931.12322;
   cout.setf(ios::fixed);
   cout.precision(2);
   cout << "$"
      << dollars
      << endl;

   //puts 3.9 on the screen
   double gpa = 3.871;
   cout.precision(1);
   cout << gpa << endl;

   // prompt user for a gpa ugpa == userGradePointAverage
   double ugpa;
   cout << "What is your GPA: ";
   cin  >> ugpa;

   //get thier letter grade
   char letterGrade;
   cout << "What is your letter grade: ";
   cin >> letterGrade;

   //round gpa
   cout.precision(1);
   cout << "Your GPA is : " << ugpa << endl;
   cout << "and your letter grade is: " << letterGrade << endl;










   //report we were successful
   return 42;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
