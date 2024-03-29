#Author: Amy R Krystosik, akrystos@stanford.edu
#last edited July 6, 2019
#instructions: https://github.com/InsightDataScience/Purchase-Analytics
#data: https://www.instacart.com/datasets/grocery-shopping-2017
#data dictionary: https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b

#define global variables
PROD_ID=0#product id is collumn 0 in products.csv
DEPT_ID= -1 #dept id is last collumn in products.csv #number of columns varies since commas in column 2 so column 3 is not always the dept id. csv reader has escape tactics to deal with this type of problem withour writing a csv reader with escape.
products = {}#create empty dictionary object for products
dept_orders = {}#create empty dictionary object for orders

order_file = './input/order_products.csv'#read from input folder. could specify in run.sh with import sys
product_file = './input/products.csv'#read from input folder. could specify in run.sh with import sys
report_file = './output/report.csv'#write to output folder. could specify in run.sh with import sys

test_order_file = './insight_testsuite/tests/test_2/input/order_products__prior.csv'#read from input folder. could specify in run.sh with import sys
test_product_file = './insight_testsuite/tests/test_2/input/products.csv'#read from input folder. could specify in run.sh with import sys
test_report_file = '/insight_testsuite/tests/test_2/output/report.csv'#write to output folder. could specify in run.sh with import sys

#read products file and create map products to department
#with open(test_product_file,'r') as f: #test with full data order_products.csv
with open(product_file,'r') as f:#import order_products.csv from folder
	next(f)  # skip the first line in the headers
	for line in f:#loop over rows in products
		column = line.strip().split(",")#comma delimited file. Return string without leading and trailing characters 
		products[column[PROD_ID]] = int(column[DEPT_ID])#look up product id to map to department id

#read order file and create map of orders to department and count of orders and reorders
#with open(test_order_file,'r') as f:#test with full data order_products.csv
with open(order_file,'r') as f:#import order_products.csv from folder
	next(f)   #skip the first line with the headers
	for line in f:#loop over rows in orders
		column = line.strip().split(',')#comma delimited file. Return string without leading and trailing characters
		if products[column[1]] in dept_orders:#if already in dept orders object, modify object
			dept_orders[products[column[1]]]["orders"] += 1;#increase value of orders by 1
			dept_orders[products[column[1]]]["reordered"] += int(column[3]);#increase value of reorder by 1
		else:#if not already in dept orders, set default value of order and reorders
			dept_orders[products[column[1]]] = {
				"orders": 1, #first order sets count to 1
				"reordered": int(column[3])#first order sets value of reorder to value of reorder
			}

#create report of number of product orders, number of first orders, and proportion of two.
#with open(test_report_file,'w') as f:#test report with full databases.
with open(report_file,'w') as f:#import order_products.csv from folder
	f.write("department_id,number_of_orders,number_of_first_orders,percentage\n")#add header to csv file.
	for dept in sorted(dept_orders):#sort ascending 
		f.write ("%d , %d , %d , %10.2f \n" 
			%(
				dept,
				dept_orders[dept]["orders"], 
				dept_orders[dept]["orders"] - dept_orders[dept]["reordered"],
				(dept_orders[dept]["orders"] - dept_orders[dept]["reordered"]) / (dept_orders[dept]["orders"] * 1.0)
			)
		)