
"""
i = int(input("What number in this sequence would you like? "))

i = i-1


sequence = [2,1,]

for x, numbers in enumerate(sequence):
    if x != 0 and x != i:
        sequence.append(sequence[x]+sequence[x-1])
        print(f"{sequence}")
    elif x == i:
        break
    else:
        continue

a=""
b=""
n=""


n = int(input("What number in this sequence would you like? ")); #print(f"A. n={n}, a= {a}, b= {b}")

if n == 2:
    "\""print(1)"\""; #print(f"B. n={n}, a= {a}, b= {b}")
elif n==1:
    ""\"print (2)"\""; #print(f"C. n={n}, a= {a}, b= {b}")
else:
    #print(f"D. n={n}, a= {a}, b= {b}")
    a, b = 2, 1; #print(f"E. n={n}, a= {a}, b= {b}")
    for nothing in range(3, n + 1):
        #print(f"F. n={n}, a= {a}, b= {b}")
        a, b = b, a + b; #print(f"G. n={n}, a= {a}, b= {b}")
    "\""print(b);""\" ;#print(f"H. n={n}, a= {a}, b= {b}")



"""