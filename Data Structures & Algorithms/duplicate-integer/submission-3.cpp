class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> vistos;
        for(int i = 0 ;i<nums.size();i++){
            if (vistos.find(nums[i]) != vistos.end()){
                return true;
            }else{
                vistos.insert(nums[i]);
            }
        }
        return false;
    }
};