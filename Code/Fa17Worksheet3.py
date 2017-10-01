#runs in n^2 time
def fun(n):
	count = n
	while(n > 0):
	     n-=1
	return fun(count-1)

#Naive Fibonacci, takes polynomial time
def fib(n):
	if(n <= 2):
	     return n
	return fib(n-1)+fib(n-2)

#Better fibonacci, with caching. Takes linear time
cache = {}
def fib(n):
    if(n <2):
         return n
    if(n-1 not in cache):
    	 cache[n-1] = fib(n-1)
    if(n-2 not in cache):
        cache[n-2] = fib(n-2)
    return cache[n-1]+ cache[n-2]