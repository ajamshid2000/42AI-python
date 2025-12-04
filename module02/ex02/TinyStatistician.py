class TinyStatistician:
    def mean(self, x):
        res = 0
        if(isinstance(x, list) and len(x) > 0):
            for i in x:
                res += i
            res = res/len(x)
            return float(res)
        else: return None
    def median(self, x):
        res = 0
        if(isinstance(x, list) and len(x) > 0):
            x.sort()
            if(len(x)%2 == 0):
                res = self.mean([x[(len(x) // 2) -1] + x[(len(x) // 2)]])
            else: res = x[((len(x) // 2))]
            return float(res)
        else: return None
    def quartile(self, x):
        res = 0
        if(isinstance(x, list) and len(x) > 0):
            x.sort()
            if(len(x)%2 == 0):
                return([self.median(x[:len(x)//2]), self.median(x[len(x)//2:])])
            else: return([self.median(x[:len(x)//2+1]), self.median(x[len(x)//2:])])
    def var(self, x):
        if not x:
            return None
        mean = self.mean(x)
        return sum((val - mean) ** 2 for val in x) / len(x)
    def std(self, x):
        return self.var(x) **(1/2)


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.81263465868862