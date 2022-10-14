#include <iostream>
#include <string>
#include <vector>

using namespace std;

int time(int h, int m);

void main()
{
    int inputa, inputb;
    printf("%d",time(inputa, inputb));

}

int time(int h, int m)
{
    if(m>=45)
    {
        m = m-45;
    }
    else
    {
        h = h - 1;
        m = m % 60;
    }
}