#1.Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary,
#save it in binary_dict.

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
z=zip(integer,binary)
binary_dict={integer:binary for integer,binary in z}
print("binary_dict:",binary_dict)

#2.Create a List which contains additive inverse of a given integer list. 

integer=[1, -1, 2, 3, 5, 0, -7]
additive_inverse=[-1*i for i in integer]
print("additive_inverse:",additive_inverse)

#3.Create a set which only contains unique sqaures from a given a integer list.

integer = [1, -1, 2, -2, 3, -3]
unique_squares={i*i for i in integer}
print("unique square:",unique_squares)