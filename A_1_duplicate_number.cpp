#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

bool containsDuplicate(const vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.find(num) != seen.end()) {
            return true; // Duplicate found
        }
        seen.insert(num);
    }
    return false; // No duplicates
}

int main() {
    vector<int> nums1 = {1, 2, 3, 1};
    vector<int> nums2 = {1, 2, 3, 4, 5};

    cout << (containsDuplicate(nums1) ? "True" : "False") << endl; // Output: True
    cout << (containsDuplicate(nums2) ? "True" : "False") << endl; // Output: False

    return 0;
}
