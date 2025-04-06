/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let i=1, j=1;
    let val1 = nums1[0];
    let val2 = nums2[0];
    let mergedArray = [];
    let median = 0;
    while(val1 !== undefined || val2 !== undefined ){
        if(val2===undefined || val1 !== undefined && val1<val2){
            mergedArray.push(val1);
            val1 = nums1[i];
            i++;
        }
        else{
            mergedArray.push(val2);
            val2 = nums2[j];
            j++;
        }
    }
    let n = mergedArray.length;
    if(n%2 === 0){
      median = (mergedArray[n/2 - 1]+mergedArray[n/2])/2;
    }
    else{
        median = mergedArray[(n-1)/2];
    }

    return median;
};