#define global variables
path = "C:/Users/amykr/Documents/GitHub/Purchase-Analytics"#set your directory here.
PROD_ID=0#product id is collumn 0 in products.csv
DEPT_ID=3#dept id isc collumn 3 in products.csv
products = {}#create empty dictionary object for products
dept_orders = {}#create empty dictionary object for orders
report=	[]
i = 0#set counter to 0

#read products file and create map products to department
with open(path+'/input/products.csv','r') as f:#import products.csv from folder
	next(f)  # skip the first line in the headers
	for line in f:#loop over rows in products
		words = line.strip().split(',')#comma delimited file. Return string without leading and trailing characters 
		products[words[PROD_ID]] = words[DEPT_ID]#look up product id to map to department id

#read order file and create map of orders to department and count of orders and reorders
with open(path+'/input/order_products__prior.csv','r') as f:#import order_products.csv from folder
	next(f)   #skip the first line with the headers
	for line in f:#loop over rows in orders
		words = line.strip().split(',')#comma delimited file. Return string without leading and trailing characters
		if products[words[0]] in dept_orders:#if at least one order of product in department ## not working
			if products[words[1]] in dept_orders:#if already in dept orders object, modify object
				dept_orders[products[words[1]]]["orders"] += 1;#increase value of orders by 1
				dept_orders[products[words[1]]]["reordered"] += int(words[3]);#increase value of reorder by 1
			else:#if not already in dept orders, set default value of order and reorders
				dept_orders[products[words[1]]] = {
					"orders": 1, #first order sets count to 1
					"reordered": int(words[3])#first order sets value of reorder to value of reorder
				}
#create report of number of product orders, number of first orders, and proportion of two.
for dept in dept_orders:#loop over department
		report.append(int(dept))
		report.append(',')
		report.append(dept_orders[dept]["orders"]) 
		report.append(',')
		report.append(dept_orders[dept]["orders"] - dept_orders[dept]["reordered"])
		report.append(',')
		report.append(float((dept_orders[dept]["orders"] - dept_orders[dept]["reordered"]) / (dept_orders[dept]["orders"] * 1.0)),2)
		report.append('\n')

report=sorted(report, key=dept)

#write report to csv in output folder
f = open(path+'/output/report.csv','w')#open file
f.write('department_id'+','+'number_of_orders'+','+'number_of_first_orders'+','+'percentage'+'\n')#add header to file
while (i<len(report)):#loop over rows in report   
    f.write(str(report[i]))#write lines to csv
    i = i + 1#add to counter to length of report
f.close()#close file