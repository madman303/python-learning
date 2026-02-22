def romanToInt(self,s:str) -> int:
    roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    n = len(s)#字符串s的长度
    for i in range(n):
        #特殊减法规则（两种情况）
        #如果当前值小于下一个值，说明是特殊情况，需要减去当前值
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
            result -= roman_map[s[i]]
        else:
            #否则，直接加上当前值
            result += roman_map[s[i]]
    return result