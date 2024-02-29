// class implementation file for Inventory objects
#include "Inventory.h"
#include <string>
#include <iostream>

// default constructor which sets all inventory object member variables to 0
Inventory::Inventory()
{
    itemNumber = 0;
    quantity = 0;
    cost = 0;
}

// constructor that takes in an item's number, gauntity, and cost and sets it to it's respective member variable
Inventory::Inventory(int itemNumberIn, int quantityIn, double costIn)
{
    setItemNumber(itemNumberIn); // iN is the item number
    setQuantity(quantityIn);     // q is the quantity
    setCost(costIn);             // c is the cost
}

// takes in an item's number and sets it to its member variable
void Inventory::setItemNumber(int itemNumberIn)
{
    // validates the item's number
    while (!validInt(itemNumberIn))
    {
        std::cout << "Item Number must be 0 or greater. Please re-enter: ";
        std::cin >> itemNumberIn;
    }
    itemNumber = itemNumberIn;
}

// takes in an item's quantity and sets it to its member variable
void Inventory::setQuantity(int quantityIn)
{
    // validates the item's quantity
    while (!validInt(quantityIn))
    {
        std::cout << "Quantity must be 0 or greater. Please re-enter: ";
        std::cin >> quantityIn;
    }
    quantity = quantityIn;
}

// takes in an item's cost and sets it to its member variable
void Inventory::setCost(double costIn)
{
    // validates the item's cost
    while (!validFloat(costIn))
    {
        std::cout << "Cost must be 0 or greater. Please re-enter: ";
        std::cin >> costIn;
    }
    cost = costIn;
}

// returns the item's number
int Inventory::getItemNumber()
{
    return itemNumber;
}

// returns the item's quantity
int Inventory::getQuantity()
{
    return quantity;
}

// returns the item's cost
double Inventory::getCost()
{
    return cost;
}

// returns the total cost of the item's inventory, quantity * cost
double Inventory::getTotalCost()
{
    return quantity * cost;
}

// returns whether an integer is greater than 0 or not
bool Inventory::validInt(int integerIn)
{
    if (integerIn < 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}

// returns whether a double is greater than 0 or not
bool Inventory::validFloat(double doubleIn)
{
    if (doubleIn < 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}