class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int i=0,j=0;
        while(i<n && j<n){
            if(nums[i]!=0 && nums[j]!=0){
                i++;
                j++;
            }
           else if(nums[i]==0 && nums[j]==0){
                j++;
            }
           else if(nums[i]==0 && nums[j]!=0){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
            }
        }
    }
}