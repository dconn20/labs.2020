# A program	that reads in a	students percentage	
# mark and prints out the corresponding	grade

#  Under	40%	=>	Fail
#  Between	40%	and	49%	 =>	Pass
#  Between	50%	and	59% =>	Merit	2
#  Between	60%	and	69%	 =>	Merit	1
#  Over	70%	 =>	Distinction

p = float(input ("Enter percentage  "))

if p < 40:
    print ("Fail")
elif p < 50:
    print ("Pass")
elif p < 60:
    print ("Merit 2")
elif p < 70:
    print ("Merit 1")
elif p > 70:
    print ("Distinction")