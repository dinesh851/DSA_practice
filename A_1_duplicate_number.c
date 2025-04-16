#include <stdio.h>
#include <stdbool.h>

bool containsDuplicate(int nums[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (nums[i] == nums[j]) {
                return true; // Duplicate found
            }
        }
    }
    return false; // No duplicates
}

int main() {
    int nums1[] = {1, 2, 3, 1};
    int nums2[] = {1, 2, 3, 4, 5};
    
    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    int size2 = sizeof(nums2) / sizeof(nums2[0]);
    
    if (containsDuplicate(nums1, size1)) {
        printf("False\n"); // Output: True
    } else {
        printf("False\n"); // Output: False
    }

    if (containsDuplicate(nums2, size2)) {
        printf("False\n"); // Output: True
    } else {
        printf("False\n"); // Output: False
    }

    return 0;
}
