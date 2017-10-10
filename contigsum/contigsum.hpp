// contigsum.hpp
// Rohan Weeden
// Created: October 10, 2017

#ifndef __con_ti_g_SUM__h_PP___
#define __con_ti_g_SUM__h_PP___

#include <tuple>

template<typename RAIter>
std::tuple<int, int, int, int> contigSumRec(RAIter first, RAIter last) {
  int length = std::distance(first, last);

  if (length == 1) {
    int gcs = std::max(0, *first);
    return std::make_tuple(gcs, gcs, gcs, *first);
  }

  return std::make_tuple(0, 0, 0, 0);
}

template<typename RAIter>
int contigSum(RAIter first, RAIter last) {
  return std::get<0>(contigSumRec(first, last));
}

#endif
