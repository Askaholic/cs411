// inversions.hpp
// Rohan Weeden
// Created: October 11, 2017

// Count the number of inversions in a range

#ifndef __INVERSIONS_HPP__
#define __INVERSIONS_HPP__

#include <algorithm>
#include <iterator>
#include <iostream>
#include <vector>

template<typename RAIter>
size_t mergesort(RAIter start, RAIter end) {
    using remove_reference_t = typename std::remove_reference<decltype(*start)>::type;
    std::vector<remove_reference_t> temp;

    auto size = std::distance(start, end);

    size_t inversions = 0;

    if (size <= 1) {
        return inversions;
    }

    auto split = size / 2;
    auto mid = start;
    std::advance(mid, split);

    // Sort Left
    inversions += mergesort(start, mid);
    // Sort Right
    inversions += mergesort(mid, end);

    auto left = start;
    auto right = mid;

    while (temp.size() < size && left < right) {
        if (!(right < end)) {
            temp.push_back(*left++);
        }
        else if (!(left < mid) || *right < *left) {
            temp.push_back(*right++);
            inversions += std::distance(left, mid);
        }
        else {
            temp.push_back(*left++);
        }
    }
    auto j = temp.begin();
    
    for(auto i = start; j < temp.end();) {
        *i++ = *j++;
    }
    return inversions;
}

template<typename RAIter>
size_t inversions(RAIter first, RAIter last) 
{
    return mergesort(first, last);
}

#endif // __INVERSIONS_HPP__