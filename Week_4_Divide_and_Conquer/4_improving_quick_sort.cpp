#include <iostream>
#include <vector>
#include <cstdlib>
#include <time.h>

using std::vector;
using std::swap;
int mid[2];

int *partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  mid[0] = l;
  mid[1] = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      mid[1]++;
      swap(a[i], a[mid[1]]);
    }
  }
  for (int i=l+1; i<= mid[1]; i++){
    if(a[i]!=r){
      mid[0]++;
      swap(a[mid[0]],a[i]);
    }
  }
  swap(a[l], a[mid[0]]);
  return mid;
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }
  srand(time(0));
  int k = l + rand() % (r - l + 1);
  // srand(5);
  swap(a[l], a[k]);
  // std::cout << "k:" << k << std::endl;
  // for (size_t i = 0; i < a.size(); ++i) {
  //   std::cout << a[i] << ' ';
  // }
  // int m[2];
  while(l<r){
    // int m[];
    int *m = partition2(a, l, r);

    if((m[0]-l)<(r-m[1])){
      randomized_quick_sort(a, l, m[0] - 1);
      l = m[1]+1;
    }
    else{
      randomized_quick_sort(a, m[1] + 1, r);
      r = m[0]-1;
    }
  }
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
}
