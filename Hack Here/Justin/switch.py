class Solution:

    def solve(self,coins,i,sum,DP):

       

            

        if sum==0:

            return 1

            

        if sum<0:

            return 0

        

        if i>len(coins)-1:

            return 0

            

        if DP[i][sum]!=-1:

            #print(DP[i][sum])

            return DP[i][sum]

            

        DP[i][sum]=self.solve(coins,i,sum-coins[i],DP)+self.solve(coins,i+1,sum,DP)

        return DP[i][sum]

    

        

    def count(self, coin, N, sum):

        # code here 

        ans=0

        i=0

        #print(N,sum)

        DP=[[-1 for j in range(N+sum)] for j in range(N+sum)]

        ans=self.solve(coins,i,sum,DP)

        #print(ans)

 

        return ans