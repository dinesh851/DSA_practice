public class A_1_duplicate_number {
    public boolean bruteforce (int[] nums){
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if (nums[i] == nums[j])
                    return true;
            }
        }
        
        
        return false;
    }
    public static void main (String[] args){
        A_1_duplicate_number solution = new A_1_duplicate_number();
        int[] nums1 = {1, 2, 3, 1};
        int[] nums2 = {1, 2, 3, 4};
        System.out.println(solution.bruteforce(nums1));
        System.out.println(solution.bruteforce(nums2));
    }
}