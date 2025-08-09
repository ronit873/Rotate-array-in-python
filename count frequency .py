class Solution:
    def frequencyCount(self, arr):
        #  code here
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=[]
        for i in range(len(arr)):
            if i+1 in d:
                a.append(d[i+1])
            else:
                a.append(0)
        return a
        