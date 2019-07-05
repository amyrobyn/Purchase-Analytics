#Author: Amy R Krystosik, akrystos@stanford.edu
#last edited July 5, 2019
#instructions: https://github.com/InsightDataScience/Purchase-Analytics
#data: https://www.instacart.com/datasets/grocery-shopping-2017
#data dictionary: https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b

#define global variables
path = "C:/Users/amykr/Documents/GitHub/Purchase-Analytics"#set your directory here.
PROD_ID=0#product id is collumn 0 in products.csv
DEPT_ID=-1#dept id is last collumn in products.csv #number of columns varies since commas in column 2 so column 3 is not always the dept id. csv reader has escape tactics to deal with this type of problem withour writing a csv reader with escape.
products = {}#create empty dictionary object for products
dept_orders = {}#create empty dictionary object for orders

#read products file and create map products to department
with open(path+'/input/products.csv','rU') as f:#import products.csv from folder
	next(f)  # skip the first line in the headers
	for line in f:#loop over rows in products
		column = line.strip().split(",")#comma delimited file. Return string without leading and trailing characters 
		products[column[PROD_ID]] = int(column[DEPT_ID])#look up product id to map to department id

#read order file and create map of orders to department and count of orders and reorders
with open(path+'/input/order_products__prior.csv','r') as f:#import order_products.csv from folder
	next(f)   #skip the first line with the headers
	for line in f:#loop over rows in orders
		column = line.strip().split(',')#comma delimited file. Return string without leading and trailing characters
#		if dept_orders[0] in products[column[3]]:#if at least one order of product in department ## not working
		if products[column[1]] in dept_orders:#if already in dept orders object, modify object
			dept_orders[products[column[1]]]["orders"] += 1;#increase value of orders by 1
			dept_orders[products[column[1]]]["reordered"] += int(column[3]);#increase value of reorder by 1
		else:#if not already in dept orders, set default value of order and reorders
			dept_orders[products[column[1]]] = {
				"orders": 1, #first order sets count to 1
				"reordered": int(column[3])#first order sets value of reorder to value of reorder
			}

#create report of number of product orders, number of first orders, and proportion of two.
with open(path+'/output/report.csv','w') as f:#import order_products.csv from folder
	f.write("department_id, number_of_orders, number_of_first_orders, percentage \n")
	for order in sorted(dept_orders):#sort ascending 
		f.write ("%s , %d , %d , %10.2f \n" 
			%(
				order,
				dept_orders[order]["orders"], 
				dept_orders[order]["orders"] - dept_orders[order]["reordered"],
				(dept_orders[order]["orders"] - dept_orders[order]["reordered"]) / (dept_orders[order]["orders"] * 1.0)

			)
		)