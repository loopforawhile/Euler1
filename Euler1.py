            # Question 1 // Soru 1
            
            # If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .
            # Find the sum of all the multiples of  or  below .
            
            # 1000'in altındaki 3'e veya 5'e bölünen sayıların toplamını istiyor.
a = 0
list1 = list()
while a < 1000:
    
    if a %3 == 0 or a %5 == 0:
        list1.append(a)
    a += 1

b = sum(list1)

print(b)