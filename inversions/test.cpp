#include "inversions.hpp"
#include <vector>
#include <deque>
#include <iostream>

int main() {

    std::vector<int> v;
    const int N = 100;
    for (int i = 0; i < N; ++i)
    {
        std::cout << i << ", " << N-i << ", ";
        v.push_back(i);
        v.push_back(N-i);
    }
    size_t ans = size_t(N*(N-1));      // Correct result
    std::cout << "Calculalting... " << std::endl;
    int i = inversions(v.begin(), v.end());
    std::cout << "Got: " << i << std::endl << "Wanted: " << ans << std::endl;
    for(auto i = v.begin(); i != v.end(); ++i) {
        std::cout << *i << ", ";
    }
}