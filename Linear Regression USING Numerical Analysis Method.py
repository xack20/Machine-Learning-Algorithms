

'''                  Linear Regression USING Numerical Analysis Method                  '''



list_x = list(map(int,input().split()))
list_y = list(map(int,input().split()))

list_size = len(list_x)
avg_of_list_x = sum(list_x)/list_size
avg_of_list_y = sum(list_y)/list_size




#       ( (avg(list_x)*avg(list_y)) - avg(list_x*list_y) ) 
#   m =  --------------------------------------------------
#              avg(list_x)**2 - avg(list_x**2)



sum_of_xy = sum_of_xSQR = 0

for i in range( list_size ):
  sum_of_xy += list_x[i]*list_y[i]
  sum_of_xSQR += list_x[i]*list_x[i]

m = (( avg_of_list_x * avg_of_list_y) - (sum_of_xy/list_size) ) / ( avg_of_list_x**2  - (sum_of_xSQR/list_size) )

c = avg_of_list_y - m * avg_of_list_x 


#print(m,c)


#               Accuracy of this Predicting Method
 
#                      sum_of  ( (new_yi - avg_of_all_y)^2 )
#   R_squared_value = ---------------------------------------
#                      sum_of  ( (old_yi - avg_of_all_y)^2 )


sm1 = sm2 = 0

for i in range(list_size):
  new_y = m* list_x[i] + c
  old_y = list_y[i]

  sm1 += ( new_y - avg_of_list_y )**2
  sm2 += ( old_y - avg_of_list_y )**2

R_squared_value = sm1/sm2

print("Approximate Accuracy of this method :",int(R_squared_value*100),"%")



# Start Predicting

#  y = int(input()) * m + c
# print("Approximate Y is" : , y)



