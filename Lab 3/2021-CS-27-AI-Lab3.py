#EDIT DISTANCE
def editDistance(s1,s2):
    length1 = len(s1)
    length2 = len(s2)
    m = [[0 for i in range(length2 +1)] for i in range(length1+1)]
    for x in range(length1 + 1):
        for y in range(length2 + 1):
            if x == 0:
                m[x][y] = y 
            elif y == 0:
                m[x][y] = x
            elif s1[x-1] == s2[y-1]:
                m[x][y] = m[x-1][y-1]
            else:
                m[x][y] = min(m[x-1][y]+1,m[x][y-1]+1,m[x-1][y-1]+1) 
    return m[length1][length2]
string1 = input('Enter a string: ')
string2 = input('Enter another string: ')
result = editDistance(string1,string2)
print(result)

#Unbalanced Sequence
def balance_brackets(s):
    balance = 0
    result = []
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            if balance > 0:
                balance -= 1
            else:
                result.insert(0, '(')
    result.extend([')'] * balance)
    result = ''.join(result) + s
    return result

s1= "(a+b(c)"
result1 = balance_brackets(s1)
print(result1) 

#Minimum Coins
def min_coins(coins, k): 
	n = len(coins) 
	dp = [[0 for i in range(k + 1)] for j in range(n + 1)] 
	for i in range(n + 1): 
		for j in range(k + 1): 
			if (i == 0): 
				dp[i][j] = float('inf') 
			elif (j == 0): 
				dp[i][j] = 0
			elif (coins[i - 1] <= j): 
				dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j]) 
			else: 
				dp[i][j] = dp[i - 1][j] 
	return dp[n][k] 

coins = [25, 10, 5] 
k = 30
result2 = min_coins(coins,k)
print(result2)