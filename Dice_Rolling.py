import random
import time
U_Num = input ("Enter your Number (1-6): ")
print("Wait a second")
for i in range(2):
	print ("Wait...")
	time.sleep(1)
for num in range(1):
	print ("My number is: " + str(random.randint(1,6)))
if U_Num == num:
	print(" AND YOU WIN")
else:
	print ("AND YOU LOST")
