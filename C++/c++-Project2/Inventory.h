// This is the inventory.h file.
// It contains the Inventory class declaration.

#ifndef INVENTORY_H
#define INVENTORY_H

class Inventory
{
private:
	int itemNumber;
	int quantity;
	double cost;

public:
	// Default constructor
	Inventory();

	// Overloaded constructor
	Inventory(int, int, double);	// Defined in Inventory.cpp

	// Mutators (i.e., "set" functions) defined in Inventory.cpp
	void setItemNumber(int);
	void setQuantity(int);
	void setCost(double);

	// Accessors (i.e., "get" functions) defined in Inventory.cpp
	int getItemNumber();
	int getQuantity();
	double getCost();
	double getTotalCost();

	// Input validation functions defined in Inventory.cpp
	// You may use separate functions as below
	// or provide code in your other functions
	bool validInt(int);
	bool validFloat(double);
};

#endif
