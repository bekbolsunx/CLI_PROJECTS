### 15.10.2023
 
import csv

print(1)
x=list (csv.reader(open("car_dealership.txt")))
dealership=[[pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost] for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x] 

def who_bought_mostexcar(arr):
    full_name=0
    a=float("-inf")
    for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
       car_cost=int(car_cost.replace("$",""))
       if car_cost>a:
           a=car_cost
           full_name=f"{f_n} {l_n}"
    return full_name
print(f"{who_bought_mostexcar(dealership)} bought the most expensive car")
print(2)


def median(arr):
    s=[]
    for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
        s.append(int(car_cost.replace("$","")))
        s=sorted(s)
        mid=len(s)//2
        if mid*2==len(s):
            mid=sum(s[mid-1:mid+1])/2
        else:
            mid=s[mid]
    return mid
print(f"${median(dealership)}  Median car cost")
print(3)


colors=list(set([car_color for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x]))
def popular_car_color(arr):
    counter = [0 for color in colors]
    for color in colors:
     for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
       if color==car_color:
          counter[colors.index(color)]+=888
    return colors[counter.index(max(counter))]
print(f"{popular_car_color(dealership)} is the most popular color")

print(4)
cars=list(set([car_model for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x]))
def least_sold_car(dealership):
 counter = [0 for car in cars]
 least_sold_cars=[]
 for car in cars:
     for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in dealership:
       if car==car_model:
          counter[cars.index(car)]+=1
 least_sold_cars.append([val for i,val in enumerate(cars) for j,val2 in enumerate(counter) if val2==min(counter) and i==j])
 return least_sold_cars
print(f"{least_sold_car(dealership)} Last sold  ")

print(5)
def avg_car_year(arr):
   sum=0  
   for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
     sum+=int(model_year)
   return sum//len(arr)
print(f"{avg_car_year(dealership)} The average car model year" )

print(6)  
def median_customer(arr):
    ages=[]
    s=[]
    for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
        ages.append(date_birth.split("."))
    for i in ages:
        s.append(2023-int(i[2]))
        s=sorted(s)
        mid=len(s)//2
        if mid*2==len(s):
            mid=sum(s[mid-1:mid+1])/2
        else:
            mid=s[mid]
    return mid
print(f"{median_customer(dealership)}  Median customer age" )

print(7)
def was_sold(dealership):
   x='Colorado Denver'
   count=0
   m=0
   for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in dealership:
     place=f"{state} {city}"
     if place==x:
        count+=1
        return True,count
print(was_sold(dealership))

