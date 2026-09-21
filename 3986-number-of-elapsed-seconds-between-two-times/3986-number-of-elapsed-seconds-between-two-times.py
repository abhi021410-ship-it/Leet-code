class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h,m,s=map(int,startTime.split(":"))
        h1,m1,s1=map(int,endTime.split(":"))
        start=h*3600+m*60+s
        end=h1*3600+m1*60+s1
        return end -start