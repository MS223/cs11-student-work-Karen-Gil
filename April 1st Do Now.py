# For each example below, predict what will be printed. Then, run the code and confirm your prediction.

a = 0
while a< 100:
	print a
"""
Prediction: This will be an infint loop because 
Observation: it didnt STOP!!!!
 """

a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: it will add 1 to 0 until it reaches to 100
Observation:It went through 1-100 unril it got to 100
 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction:even if you say yes iy will always ask you the same thing
Observation: IT did until you put y
 """
