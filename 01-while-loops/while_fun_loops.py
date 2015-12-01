#1.
#i = 1
#while(i <= 20):
#	print i
#	i = i + 1

#2.
#i = 1
#while(i <= 20):
#	if (i == 13):
#		print "hello"
#	else:
#		print i
#	i = i + 1

#3.
#i = 0
#while(i <= 101):
#	if(i%10 == 0):
#		print i
#	i = i + 1

#4.
#i = 0
#while(i <= 10):
#	if(i%2 != 0):
#		print i
#	i = i + 1

#5.
#i = 10
#while(i >= 0):
#	if(i == 0):
#		print "Blastoff!"
#	else:
#		print i
#	i = i - 1

#6. 
#fruits = ["apples", "oranges", "bananas"]

#i = 0
#while(i < len(fruits)):
#	print fruits[i]
#	i = i + 1

#7.
def sum_nums(num):
	i = 0
	sum = 0

	while(i < num):
		sum = sum + i
		i = i + 1
	return sum

print sum_nums(3)

#7i.
def sum_nums(num):
	i = 0
	sum = 0

	while(i <= num):
		sum = sum + i
		i = i + 1
	return sum

print sum_nums(3)
