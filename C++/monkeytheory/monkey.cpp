// pre-processor directives
#include <iostream>
using namespace std;

// function to generate a new string
string gen(int length)
{
    string alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
    string res = "";

    for (int i = 0; i < length; i++)
    {
        int randomNum = rand() % 52;
        res += alpha[randomNum];
    }

    return res;
}

float score(string goal, string attempt)
{
    float same = 0;

    for (int i = 0; i < goal.length(); i++)
    {
        if (goal[i] == attempt[i])
        {
            same += 1;
        }
    }

    return same / goal.length();
}

int main()
{
    string goal;
    cout << "Enter Goal: " << endl;
    cin >> goal;

    string attempt = gen(goal.length());

    float best = 0.00;

    float curr = score(goal, attempt);

    int index = 0;

    int tot = 0;

    while (curr < 1.0)
    {
        if (curr > best)
        {
            cout << "\nBest: " << attempt << "\nTime: " << tot << endl;
            best = curr;
        }

        if (index == 1000000)
        {
            cout << ".";
            cout.flush();

            index = 0;
        }

        attempt = gen(goal.length());
        curr = score(goal, attempt);
        index += 1;
        tot += 1;
    }

    cout << "\nWord Found!\nTime: " << tot << endl;
}
