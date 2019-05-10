"""Class MM prints the double M figure based on a number N. If we 
look at the examples we can clearly see that there are N+1 rows and 
each row has 10 * N characters which can be split into two identical 
repetitions of the same half row. This is why we can make a method to 
print half of a row and call it twice. We will count the number of 
executions of this method and on every second execution we will change
the values so that they match the figure. Moreover we can split the 
figure in two equal parts each (N + 1) / 2 rows based on the sequence 
of characters needed."""


class MM():

	#this is the number of executions that the method has had
	executionCount = 0

	#constructor that sets the values
	def __init__(self, N):

		#size of the logo MM
		self.N = N

		#this is the array for the print values
		self.printList = [N] * 5

	#method that prints half of a row                        
	def PrintRow(self):

		#We check if we are using the first sequence           
		if len(self.printList) == 5:

			#We print the line
			for index in range(len(self.printList)):

				#The * characters are always on the odd indexes
				if(index % 2 == 0):
					print('-' * self.printList[index], end = "")
				else:
					print('*' * self.printList[index], end = "")

				#On every second execution of the method decrease and
				#increase the list elements with the needed values
				if self.executionCount % 2 == 1:
					if index == 0 or index == len(self.printList) - 1:
						self.printList[index] -= 1
					elif index == 2:
						self.printList[index] -=2
					else:
						self.printList[index] += 2
		else:

			#We print the line for the second sequence
			for index in range(len(self.printList)):

				#The * characters are always on the odd indexes
				if(index % 2 == 0):
					print('-' * self.printList[index], end = "")
				else:
					print('*' * self.printList[index], end = "")

				#On every second execution of the method decrease and
				#increase the list elements with the needed values
				if self.executionCount % 2 == 1:
					if index == 0 or index == len(self.printList) - 1:
						self.printList[index] -= 1
					elif index == 2 or index == 4:
						self.printList[index] +=2
					elif index == 3:
						self.printList[index] -= 2

		#we increase the execution count with one
		self.executionCount += 1

		#check if there should be a transition from the first to the 
		#second sequence
		if self.printList[2] < 1:
			self.printList = [self.printList[0], self.N, 
				1, self.printList[1] - 2, 1, self.N, self.printList[4]]
        
	#for each column we call the method for printing the row twice
	def PrintFigure(self):
		print("N = " + str(self.N))
		for row in range(N + 1):
			[self.PrintRow() for i in range(2)]
			print()



#get the input from the user and check if it is a number
try:
	N = int(input("Please give the N:").strip())
except:
	print("Input must be an integer")
	
	#We must set the value because of the while
	N = 0
	
#check if it's even and between 3 and 9999
while N < 2 or N > 10000 or N % 2 == 0:
	print("Input must be an odd number between 3 and 9999")
	try:
		N = int(input("Please give the N:").strip())
	except:
		print("N must be an integer")

#create an object of our class
objectPrinter = MM(N)

#call the method that prints the figure
objectPrinter.PrintFigure()

