# import data from source folder to R -------------------------------------------------------------
setwd("C:/Users/amykr/Documents/GitHub/Purchase-Analytics")#this is your source folder
products<-read.csv(file = "input/products.csv")#import 1st data base
order_products<-read.csv(file = "input/order_products.csv")# import 2nd data base
merge<-merge(products,order_products,by="product_id")#merge database 1 and 2

# create report with number_of_orders, number_of_first_orders, and ratio of firth to total orders-------------------------------------------------------------
library(dplyr)#import dplyr library
report<-merge %>%
  group_by(department_id) %>%
  summarise(number_of_orders=length((department_id)),number_of_first_orders=sum(reordered==0),percentage=number_of_first_orders/number_of_orders)

# write report to csv in output folder-------------------------------------------------------------
write.csv(report,file="output/report.csv")#write to output folder