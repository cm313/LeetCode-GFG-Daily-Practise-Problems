/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let myMap = new Map();
    for(let i=0; i<nums.length; i++){
        let val =  target-nums[i];
        if(myMap.has(val))
        return [myMap.get(val),i];
     
            myMap.set(nums[i], i);
        
    }
    return [];
};