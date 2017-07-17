#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int spaces;
    int stairs;
    int nb;
    cin >> nb;
    spaces = nb -1;
    stairs = 1;
    for (int i = 0; i <nb; i++)
    { 
        for (int i = 0; i < spaces; i++)
            cout << " ";
        for (int i = 0; i < stairs; i++)
            cout << "#";
        cout << "" << endl;
        stairs++;
        spaces--;
    }
    return 0;
}
