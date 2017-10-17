

WRITE_CODE = False
# 1. 곱셈 함수(꼬리 재귀)
def mult1(m,n):
	def loop(n,ans):
		if (n>0):
			return loop(n-1,ans + m)
		else:
			return ans
	return loop(n,0)
  
# 2. 곱셈 함수(while문)
def mult2(m,n):
	ans = 0
	while (n != 0):
		n, ans = n-1, ans + m
	return ans

###################
#      수정 X      #
# 곱셈 함수 보조 함수 #
def double(n):    #
  return n * 2    #
                  #
def halve(n):     #
  return n // 2   #
###################

# 3. 빠른 곱셈 함수(재귀)
def fastmult1(m,n):
	if n > 0:
		if n % 2 == 0:
			return fastmult1(double(m),halve(n))
		else:
			return m + fastmult1(m,n-1)
	else:
		return 0

# 4. 빠른 곱셈 함수(꼬리 재귀)
def fastmult2(m,n):
	ans = 0
	def loop(m,n,ans):
		if (n > 0):
			if n % 2 == 0:
				return loop(double(m),halve(n),ans)
			else:
				return loop(m, n-1, ans + m)
		else:
			return ans
	return loop(m,n,0)

# 5. 빠른 곱셈 함수(while문)=
def fastmult3(m,n):
	ans = 0
	while(n > 0):
		if n % 2 == 0:
			m, n = double(m), halve(n)
		else:
			n, ans = n-1, ans + m
	return ans

# 6. 러시아 농부 곱셈 함수(재귀)
def russianmult1(m,n):
	def loop(m,n):
		if (n > 1):
			if n % 2 == 1:
				return m + loop(double(m),halve(n))
			else :
				return loop(double(m),halve(n))
		else:             # n == 1
			return m
	if (n > 0):
		return loop(m,n)
	else:
		return 0

# 7. 러시아 농부 곱셈 함수(꼬리 재귀)
def russianmult2(m,n):
	ans = 0
	def loop(m,n,ans):
		if (n > 1):
			if n % 2 == 1:
				return loop(double(m),halve(n),ans+m)
			else :
				return loop(double(m),halve(n),ans)
		else:
			return ans + m
	return loop(m,n,0)

# 8. 러시아 농부 곱셈 함수(while문)
def russianmult3(m,n):
	ans = 0
	while n > 0:
		if n > 1 :
			if n % 2 == 1:
				m, n, ans = double(m), halve(n), ans + m
			else : 
				m, n, ans = double(m), halve(n), ans
		else:	
			return m + ans


# 이 실행 부분은 이해하기 어려운 코드로 작성되어 있습니다.
# 입력에 따라 알맞은 함수를 부르게 되어있습니다.
# 채점을 위한 부분이니 그냥 넘어가세요
####################################
#              수정 X               #
#           실행 스크립트             #
funcMap = {                        #
  "mult1": mult1,                  #
  "mult2": mult2,                  #
  "fastmult1": fastmult1,          #
  "fastmult2": fastmult2,          #
  "fastmult3": fastmult3,          #
  "russianmult1": russianmult1,    #
  "russianmult2": russianmult2,    #
  "russianmult3": russianmult3,    #
}                                  #
function = input()                 #
m = int(input())                   #
n = int(input())                   #
                                   #
res = (funcMap.get(function))(m,n) #
if(type(res) == int):              #
  print(res)                       #
####################################