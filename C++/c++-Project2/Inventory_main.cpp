// Chapter 7 - Programming Challenge 7, Inventory class
// Files used for this project:
// ProgChallenge_7_07.cpp (this file, which tests the class functions)
//    Student test programs will likely be different.
// Inventory.h   -- contains Inventory class declaration
// Inventory.cpp -- contains Inventory class function definitions
#include <iostream>
#include <iomanip>
#include "Inventory.h"
using namespace std;

int main()
{
	cout << fixed << showpoint << setprecision(2);

	// Demonstrate the default constructor
	Inventory stockItem1;
	cout << "\nDemonstrating the default constructor...\n";
	cout << "Item number: " << stockItem1.getItemNumber() << endl;
	cout << "Quantity   : " << stockItem1.getQuantity() << endl;
	cout << "Cost       : " << stockItem1.getCost() << endl;
	cout << "Total Cost : " << stockItem1.getTotalCost() << endl;

	// Now demonstrate the overloaded constructor
	Inventory stockItem2(124, 12, 84.95f);
	cout << "\nDemonstrating the overloaded constructor...\n";
	cout << "Item number: " << stockItem2.getItemNumber() << endl;
	cout << "Quantity   : " << stockItem2.getQuantity() << endl;
	cout << "Cost       : " << stockItem2.getCost() << endl;
	cout << "Total Cost : " << stockItem2.getTotalCost() << endl;

	// Now demonstrate the member "set" functions
	stockItem2.setItemNumber(243);
	stockItem2.setQuantity(50);
	stockItem2.setCost(9.50);
	cout << "\nDemonstrating the \"set\" functions...\n";
	cout << "Item number: " << stockItem2.getItemNumber() << endl;
	cout << "Quantity   : " << stockItem2.getQuantity() << endl;
	cout << "Cost       : " << stockItem2.getCost() << endl;
	cout << "Total Cost : " << stockItem2.getTotalCost() << endl;

	// Now demonstrate the input validation functions
	cout << "\nDemonstrating the input validation functions...\n";
	stockItem2.setItemNumber(-1);
	stockItem2.setQuantity(-1);
	stockItem2.setCost(-1);
	cout << "\nItem number: " << stockItem2.getItemNumber() << endl;
	cout << "Quantity   : " << stockItem2.getQuantity() << endl;
	cout << "Cost       : " << stockItem2.getCost() << endl;
	cout << "Total Cost : " << stockItem2.getTotalCost() << endl;

	return 0;
}

/* RUN OUTPUT PRODUCED BY THIS TEST PROGRAM

Demonstrating the default constructor...
Item number: 0
Quantity   : 0
Cost       : 0.00
Total Cost : 0.00

Demonstrating the overloaded constructor...
Item number: 124
Quantity   : 12
Cost       : 84.95
Total Cost : 1019.40

Demonstrating the "set" functions...
Item number: 243
Quantity   : 50
Cost       : 9.50
Total Cost : 475.00

Demonstrating the input validation functions...
Item Number must be 0 or greater. Please re-enter: 100
Quantity must be 0 or greater. Please re-enter: 10
Cost must be 0 or greater. Please re-enter: 9.50

Item number: 100
Quantity   : 10
Cost       : 9.50
Total Cost : 95.00
*/
