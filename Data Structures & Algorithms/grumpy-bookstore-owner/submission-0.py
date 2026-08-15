class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        sum_ = 0
        grumpsum = 0
        grumpsummax = 0
        l = 0 
        for r in range(len(customers)):

            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    grumpsum -= customers[l]
                l += 1
            if grumpy[r] == 0:
                sum_ += customers[r]
            else:
                grumpsum += customers[r]

            grumpsummax = max(grumpsummax, grumpsum)


        return sum_ + grumpsummax


