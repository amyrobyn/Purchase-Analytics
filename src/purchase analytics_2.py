#path
path = "C:/Users/amykr/Documents/GitHub/Purchase-Analytics"#set your directory here.

PROD_ID=0
DEPT_ID=3
products = {}
dept_orders = {}

#import products.csv from folder
with open(path+'/input/products.csv','r') as f:
	next(f)  # skip the first line in the headers
	for line in f:
		words = line.strip().split(',')
		products[words[PROD_ID]] = words[DEPT_ID]
#	print products[1][0]

#import order_products.csv from folder
with open(path+'/input/order_products.csv','r') as f:
	next(f)   #skip the first line with the headers
	for line in f:
		words = line.strip().split(',')
		if products[words[1]] in dept_orders:
			dept_orders[products[words[1]]]["orders"] += 1;
			dept_orders[products[words[1]]]["reordered"] += int(words[3]);
		else:
			dept_orders[products[words[1]]] = {
				"orders": 1, 
				"reordered": int(words[3])
			}

		#order_products.append((words[1],words[3]))
#	print order_products[1][1][0]

for order in dept_orders:
	print ("Dept: %s   Orders: %d  first order: %d  perc: %f" 
		%(
			order,
			dept_orders[order]["orders"], 
			dept_orders[order]["orders"] - dept_orders[order]["reordered"],
			(dept_orders[order]["orders"] - dept_orders[order]["reordered"]) / (dept_orders[order]["orders"] * 1.0)

		)
	)

