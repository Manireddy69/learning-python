#using lambda funtion in map function
a = [9,8,6,7]
b = map(lambda x:x*2,a)
print (list(b)) 
#output :18, 16,
even = filter(lambda x:  x% 2 ==0 , a)
print(list(even))




