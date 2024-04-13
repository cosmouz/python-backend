//************************************************************************** 

//File: a9_LastName.cpp  
//Student: Shokirov Muhammadrasul  
//Assignment: Assignment #9 
//Course Name: Computer Programming II 
//Course Number: COSC 1560
//Due: Fri. April 12 (11.59 PM) 
//Statement of what the program does
//**************************************************************************

#include <iostream>

using namespace std;

class NumDays {
private:
    double hours;

public:
    NumDays(double h) : hours(h) {}

    void setHours(double h) {
        hours = h;
    }

    double getHours() {
        return hours;
    }

    double getDays() {
        return hours / 8.0;
    }

    NumDays operator+(const NumDays& other) {
        return NumDays(hours + other.hours);
    }

    NumDays operator-(const NumDays& other) {
        return NumDays(hours - other.hours);
    }
};

int main() {
    NumDays d1(8);
    NumDays d2(12);
    NumDays d3(18);

    cout << "8 hours = " << d1.getDays() << " days" << endl; 

    cout << "12 hours = " << d2.getDays() << " days" << endl;

    cout << "18 hours = " << d3.getDays() << " days" << endl;

    NumDays d4 = d1 + d2;
    cout << "8 + 12 hours = " << d4.getHours() << " hours" << endl;

    NumDays d5 = d3 - d2;
    cout << "18 - 12 hours = " << d5.getHours() << " hours" << endl;
    return 0;
}
