'''
Lab 9
Define Class
'''

#1
class my_stat:
    
    def calc_sigma(self,m,n):
        result=0
        for i in range(n, m+1):
            result= result + i
        return (result)
        
    def calc_pi(self,m,n):
        result=1
        for i in range (n, m+1):
            result=result*i
        return (result)
        
    def calc_factorial(self,m):
        if m==0:
            return 1
        else:
            return m*self.calc_factorial(m-1)
        
    def calc_permutation(self,m,n):
        return self.calc_factorial(m)/self.calc_factorial(m-n)