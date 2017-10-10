// contigsum.hpp
// Rohan Weeden
// Created: October 10, 2017

#ifndef __con_ti_g_SUM__h_PP___
#define __con_ti_g_SUM__h_PP___

#include <tuple>
#include <algorithm>

template<typename RAIter>
std::tuple<int, int, int, int> contigSumRec(RAIter first, RAIter last) {
  auto length = std::distance(first, last);

  if (length == 1) {
    auto gcs = std::max(0, *first);
    return std::make_tuple(gcs, gcs, gcs, *first);
  }

  auto mid = first;
  std::advance(mid, length / 2);

  auto first_half = contigSumRec(first, mid);
  auto second_half = contigSumRec(mid, last);

  auto start_gcs = 0;
  auto end_gcs = 0;

  if (std::get<1>(first_half) == std::get<3>(first_half))
      start_gcs = std::get<1>(first_half) + std::get<1>(second_half);
  else
      start_gcs = std::max(std::get<1>(first_half), std::get<3>(first_half) + std::get<1>(second_half));

  if (std::get<2>(second_half) == std::get<3>(second_half))
      end_gcs = std::get<2>(first_half) + std::get<2>(second_half);
  else:
      end_gcs = std::max(std::get<2>(second_half), std::get<3>(second_half) + std::get<2>(first_half));

  return std::make_tuple(std::max(std::get<0>(first_half), std::get<2>(second_half), std::get<2>(first_half) + std::get<1>(second_half)), start_gcs, end_gcs, std::get<3>(first_half) + std::get<3>(second_half));
}

template<typename RAIter>
int contigSum(RAIter first, RAIter last) {
  return std::get<0>(contigSumRec(first, last));
}

#endif
