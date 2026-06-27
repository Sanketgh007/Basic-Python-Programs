class Solution:
    def threeSum(self, nums):
        ans =set()
        n=len(nums)
        for i in range(n):
            seen=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in seen:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    ans.add(tuple(temp))
                seen.add(nums[j])
        return [list(x) for x in ans]
        """
        triple_set=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        triple_set.add(tuple(temp))
        ans=[]
        for triplet in triple_set:
            ans.append(list(triplet))
        return ans
        """
       