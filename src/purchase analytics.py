#path
path = "C:/Users/amykr/Documents/GitHub/Purchase-Analytics"#set your directory here.

#import products.csv from folder
with open(path+'/input/products.csv','r') as f:
	products = []
	for line in f:
		words = line.split(',')
		products.append((words[0],words[1:]))
#	print products[1][0]

#import order_products.csv from folder
with open(path+'/input/order_products.csv','r') as f:
	order_products = []
	for line in f:
		words = line.split(',')
		order_products.append((words[0],words[1:]))
#	print order_products[1][1][0]

#merge datasets 1 and 2 by product_id
merge = []#create new object
for product in products:
	for order in order_products: 
		print order[1][0]
		if product[0] == order[1][0]:
			merge.append((product[1][2],order[1][2],order[1][0])) 

for line in merge:
	print line


#create the report by department
report = []#create new object

#count order
number_of_orders=0
number_of_first_orders=0
for row in merge:
	for col in merge:
#		if not row[0] in report[0][0]:
			if row[0]==col[0]:
				number_of_orders = number_of_orders +1
			print col[1]
			if col[1].rstrip()=="0":
				print "hola"
				number_of_first_orders = number_of_first_orders +1
	report.append((row[0],number_of_orders,number_of_first_orders)) 
	number_of_orders =0
	number_of_first_orders =0
	print row[0]
	merge.remove(row)
print report

