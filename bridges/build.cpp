// build.cpp
// Rohan Weeden
// Created: September 29, 2017

// Implement build function
#include <vector>

using std::vector;
using Bridge = vector<int>;

int max(int a, int b) {
  if (a < b) return b;
  else return a;
}

bool isLegal(const Bridge & b, const vector<Bridge> & builtBridges) {
  for (auto const& e: builtBridges) {
    if ((b[0] <= e[0] && b[1] >= e[1]) ||
        (b[0] >= e[0] && b[1] <= e[1]))
      return false;
  }
  return true;
}

int build_recurse(int index, const vector<Bridge> & bridges, const vector<Bridge> & builtBridges) {
  if (index >= bridges.size())
    return 0;
  else {
    auto sum1 = -1;

    if (isLegal(bridges[index], builtBridges)) {
      auto bridgeVal = bridges[index][2];
      vector<Bridge> builtBridgesCopy(builtBridges);
      builtBridgesCopy.push_back(bridges[index]);

      sum1 = build_recurse(index + 1, bridges, builtBridgesCopy) + bridgeVal;
    }

    auto sum2 = build_recurse(index + 1, bridges, builtBridges);
    
    return max(sum1, sum2);
  }
}

int build(int w, int e, const vector<Bridge> & bridges) {
  vector<Bridge> builtBridges;
  return build_recurse(0, bridges, builtBridges);
}
