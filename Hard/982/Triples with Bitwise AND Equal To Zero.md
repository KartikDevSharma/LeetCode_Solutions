```Java []
class Solution {
    public int countTriplets(int[] nums) {
       
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        
       
        int bitRange = 1;
        while (bitRange <= maxVal) {
            bitRange <<= 1;  
        }
        
     
        int[] pairAndCounts = new int[bitRange];
        for (int x : nums) {
            for (int y : nums) {
                pairAndCounts[x & y]++;
            }
        }
        
        int totalTriplets = 0;
        
       
        for (int num : nums) {
            int complement = num ^ (bitRange - 1);
            totalTriplets += pairAndCounts[0];  

        
            int subset = complement;
            while (subset > 0) {
                totalTriplets += pairAndCounts[subset];
                subset = (subset - 1) & complement;
            }
        }
        
        return totalTriplets;
    }
}


//Kartikdevsharmaa
```
```C++ []
class Solution {
public:
    int countTriplets(vector<int>& nums) {
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }

        int bitRange = 1;
        while (bitRange <= maxVal) {
            bitRange <<= 1; 
        }

        vector<int> pairAndCounts(bitRange, 0);
        for (int x : nums) {
            for (int y : nums) {
                pairAndCounts[x & y]++;
            }
        }

        int totalTriplets = 0;

      
        for (int num : nums) {
            int complement = num ^ (bitRange - 1);
            totalTriplets += pairAndCounts[0];  
            int subset = complement;
            while (subset > 0) {
                totalTriplets += pairAndCounts[subset];
                subset = (subset - 1) & complement;
            }
        }

        return totalTriplets;
    }
};
//Kartikdevsharmaa
```
```Python []
class Solution:
    def countTriplets(self, nums):

        maxVal = max(nums)

        bitRange = 1
        while bitRange <= maxVal:
            bitRange <<= 1  

        pairAndCounts = [0] * bitRange
        for x in nums:
            for y in nums:
                pairAndCounts[x & y] += 1

        totalTriplets = 0

        for num in nums:
            complement = num ^ (bitRange - 1)
            totalTriplets += pairAndCounts[0] 
            subset = complement
            while subset > 0:
                totalTriplets += pairAndCounts[subset]
                subset = (subset - 1) & complement

        return totalTriplets

#Kartikdevsharmaa
```
