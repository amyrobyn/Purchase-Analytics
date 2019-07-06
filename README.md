# Insight Data Engineering - Purchase-Analytics
 Coding Challenge: Summary of approach and run instructions

#approach
1) Map the products to their department in order to create a dictionary of products and department from products.csv.
2) Count the number of times a department was listed in orders_products.csv and number of times a product was reordered.
3) Write report to csv by subtracting reorders from orders and calculating ratio of first order to orders by department.
4) test with full dataset from https://www.instacart.com/datasets/grocery-shopping-2017

#notes to run
1. Replace the variable path for your local repository root path

2. to run test_2, data must be downloaded from #data: https://www.instacart.com/datasets/grocery-shopping-2017
#data dictionary: https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b . the data must be called directly from the source file. 
note, using sys import in python, the input for example and test data could be called automatically.

   	
#Questions, email Amy Krystosik at akrystos@stanford.edu
#Author: Amy R Krystosik
#last edited July 5, 2019
#instructions: https://github.com/InsightDataScience/Purchase-Analytics
#data: https://www.instacart.com/datasets/grocery-shopping-2017
#data dictionary: https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b