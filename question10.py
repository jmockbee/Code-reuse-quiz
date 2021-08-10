def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 

    x = numerator 
    y = denominator
    if (y==0):
            return 0
    z = (x % y) / y

    if (z == 0):
            return 0
    else :
            return z 


# keep just the fractional part of the quotient
	

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0