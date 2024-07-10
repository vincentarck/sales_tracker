import datetime
import csv  
relation_of_products_name = {
    "P001": "Wireless Headphones",
    "P002": "Laptop Backpack" ,
    "P003": "Bluetooth Speaker" ,
    "P004": "USB Flash Drive", 
    "P005": "Mobile Phone Case",
    "P006": "Wireless Mouse" ,
    "P007": "Laptop Stand" ,
    "P008": "HDMI Cable" ,
    "P009": "Smartphone",
    "P010": "External Hard Drive"
}

relation_of_products_price = {
    "Wireless Headphones": 100,
    "Laptop Backpack": 60,
    "Bluetooth Speaker": 50,
    "USB Flash Drive": 20,
    "Mobile Phone Case": 15,
    "Wireless Mouse": 30,  
    "Laptop Stand": 40,  
    "HDMI Cable": 15,
    "Smartphone": 600,  
    "External Hard Drive": 100
}

sales_tracker_data = []

with open('product_sales.txt', 'r') as text_file:
    sale_id = 1
    for line in text_file:
        rmv_newline = line.strip()
        if relation_of_products_name.get(rmv_newline):
            # Programmatically convert data for each row in csv file
            current_date = datetime.date.today()
            product_id = rmv_newline
            product_name = relation_of_products_name.get(rmv_newline)
            product_price = relation_of_products_price.get(product_name)
            
            # Adding data for each row
            sales_tracker_data.append([current_date, sale_id, product_id, product_name, product_price])
            
            # Remove duplicates in key of product_sales
            del relation_of_products_name[rmv_newline]
            
            # Adding unique product id
            sale_id = sale_id + 1


with open("product_sales.csv", "w", newline="") as csv_file:
    headers = ["current_date", "sale_id", "product_id", "name", "price"]
    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    
    csv_writer.writerows(sales_tracker_data)