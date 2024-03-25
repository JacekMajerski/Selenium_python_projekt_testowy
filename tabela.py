import json
from openpyxl import Workbook

# Wczytaj dane JSON z pliku
with open('D:\data1.json') as f:
    data = f.readlines()

# Przetwórz dane JSON
rows = []
for line in data:
    row = json.loads(line)
    rows.append(row)

# Utwórz nowy arkusz Excela
wb = Workbook()
ws = wb.active

# Dodaj nagłówki
headers = ["_id", "product_price", "product_quantity", "product_name", "tags", "order_id", "order_userDevice", "order_shipping_price", "order_shipping_method", "order_payment_method", "commission"]
ws.append(headers)

# Dodaj dane do arkusza Excela
for row in rows:
    product = row['product']
    order = row['order']
    values = [
        row['_id'],
        product['price'],
        product['quantity'],
        product['name'],
        product['tags'],
        order['id'],
        order['userDevice'],
        order['shipping']['price'],
        order['shipping']['method'],
        order['payment']['status'],
        order['payment']['method'],
        row['commission']
    ]
    ws.append(values)

# Zapisz arkusz Excela
wb.save("dane.xlsx")
