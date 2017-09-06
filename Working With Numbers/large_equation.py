#Challenge: solve the equation:
#  (a + (b - c) * d - e) * f = [22, 38, 46, 57, 75, 78, 80, 81, 88, 92, 100, 102, 104, 105]
#where a, b, c, d, e, and f are unique integers in the range [1, 6].

values = [22, 38, 46, 57, 75, 78, 80, 81, 88, 92, 100, 102, 104, 105]

for value in values:

	a = 1

	while a <= 6:
		
		b = 1
		while b <= 6:

			c = 1
			while c <= 6:
				
				d = 1
				while d <= 6:
					
					e = 1
					while e <= 6:
						
						f = 1
						while f <= 6:
								
							if (a + (b - c) * d - e) * f == value:
								
								if a != b and a != c and a != d and a != e and a != f:
									if b != c and b != d and b != e and b != f:
										if c != d and c != e and c != f:
											if d != e and d != f:
												if e != f:
											
													a_final = a
													b_final = b
													c_final = c
													d_final = d
													e_final = e
													f_final = f			
							f += 1

						e += 1
					
					d += 1
				
				c += 1
			
			b += 1
		
		a += 1

	print ("When we use the equation (a + (b-c) * d - e) * f = " + str(value))
	print ("The value of a is " + str(a_final))
	print ("The value of b is " + str(b_final))
	print ("The value of c is " + str(c_final))
	print ("The value of d is " + str(d_final))
	print ("The value of e is " + str(e_final))
	print ("The value of f is " + str(f_final))
	print ("")