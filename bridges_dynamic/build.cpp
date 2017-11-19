// build.cpp
// Rohan Weeden
// Created: November 19, 2017

// Implement build function
#include <vector>
#include <cstddef>
#include <algorithm>

using std::vector;
using std::max;
using Bridge = vector<int>;

// A wrapper around vector for storing data in a 2 dimensional matrix
template <typename T>
class Matrix {
private:
  vector<T> _data;
  size_t _rows;
  size_t _cols;

public:
  Matrix (size_t rows, size_t cols) : _rows(rows), _cols(cols) {
      _data = vector<T>(rows * cols);
  }

  T get(size_t row, size_t col) {
    auto index = _rows * row + col;
    if (row < 0 || col < 0 || row > _rows || col > _cols) {
      return T(0);
    }
    return _data[index];
  }

  void set(size_t row, size_t col, T val) {
    _data[_rows * row + col] = val;
  }
};

int build(int w, int e, const vector<Bridge> & bridges) {
  Matrix<int> tolls(w, e);
  int totalMax = 0;

  for (auto b : bridges) {
    if (b[2] > tolls.get(b[0], b[1])) {
      tolls.set(b[0], b[1], b[2]);
    }
  }

  for (auto i = 0; i < w; i++) {
    for (auto j = 0; j < e; j++) {
      auto currMax = max(tolls.get(i, j) + tolls.get(i - 1, j - 1), max(tolls.get(i - 1, j), tolls.get(i, j - 1)));

      if (totalMax < currMax) {
        totalMax = currMax;
      }
      tolls.set(i, j, currMax);
    }
  }

  return totalMax;
}
