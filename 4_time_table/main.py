num = input("Enter a number you'd like to get the multiplication table for >> ")
rang = input("Enter the range from 1 - ")

if not num.isdigit():
	print("Invalid number Try 'Digits' instead")
else:
	num = int(num)
	if not rang.isdigit():
		pass
	else:
		rang = int(rang)
		for i in range(1,(rang+1),1):
			print(f"| --- {num} ❌ {i}  =  {num * i} ---- | ")

# Here is the First Format
num_2 = input("Enter a number you'd like to get the multiplication table for >> ")

if not num_2.isdigit():
	print("Enter a Number")
else:
	num_2 = int(num_2)
	table = f"""
#	{num_2}   ✖   1 =   {num_2 * 1}   	#
#	{num_2}   ✖   2 =   {num_2 * 2}   	#
#	{num_2}   ✖   3 =   {num_2 * 3}   	#
#	{num_2}   ✖   4 =   {num_2 * 4}   	#
#	{num_2}   ✖   5 =   {num_2 * 5}   	#
#	{num_2}   ✖   6 =   {num_2 * 6}   	#
#	{num_2}   ✖   7 =   {num_2 * 7}   	#
#	{num_2}   ✖   8 =   {num_2 * 8}   	#
#	{num_2}   ✖   9 =   {num_2 * 9}   	#
#	{num_2}   ✖   10 =  {num_2 * 10}   	#
#	{num_2}   ✖   11 =  {num_2 * 11}   	#
#	{num_2}   ✖   12 =  {num_2 * 12}   	#
	"""
	print(table)