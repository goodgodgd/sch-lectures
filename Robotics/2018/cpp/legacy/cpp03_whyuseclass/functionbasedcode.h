#ifndef FUNCTIONBASEDCODE_H
#define FUNCTIONBASEDCODE_H

#include <iostream>
#include <string>
using namespace std;


float ripenApple(float sweetness)
{
    const float sweetIncr = 0.3f;
    sweetness += sweetIncr;
    cout << "apple's current sweetness=" << sweetness << endl;
    return sweetness;
}

float ripenOrange(float sweetness)
{
    const float sweetIncr = 0.5f;
    sweetness += sweetIncr;
    cout << "orange's current sweetness=" << sweetness << endl;
    return sweetness;
}


bool isEatable(const string name, float sweetness)
{
    cout << name << " is eatable? " << ((sweetness > 2.f) ? "yes" : "no") << endl;
    return (sweetness > 2.f);
}

#endif // FUNCTIONBASEDCODE_H
