#union
st1={1,2,3,4,5,6}
st2={5,5,6,7,8,9,10}
set3=st1.union(st2)#its combine the elements of both sets and avoid the dupication
print(set3)
#----------------------------------------

#intersection
set4=st1.intersection(st2)
print(set4)#it print the common values in both list, it avoid duplicates
#----------------------------------------

#difference
set5=st1.difference(st2)
set6=st2.difference(st1)
print(set5)
print(set6)

