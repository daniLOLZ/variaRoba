def fib(n):
	
	a, b = 0, 1
	for i in range(0, n):
		print(b, sep=' ')
		a, b = b, a+b

fib(int(input("Inserisci quanti numeri di Fibonacci vuoi\n")))