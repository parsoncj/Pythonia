class Calc:

	# Convert Btus to Joules
	def btuToJ(btu):
		# If number is negative return zero
		if btu < 0:
			return 0
		else: 
 			 return btu * 1055.055853
	# Convert Joules to Btus
	def jtoBtu(j):
		# If number is negative return zero
		if j < 0:
			return 0
		else:
  			return j * 0.00094781712