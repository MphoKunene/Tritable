
#the row will print from 1-9
for row in range(1, 10):
	#the column will range from 1 to row and also add the row by 1
	for col in range(1, row+1):
		#multiply the row by column and add spaces to the end
		print(row*col, end=" ")
	print("\n")