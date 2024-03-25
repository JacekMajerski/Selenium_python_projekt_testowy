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
    product = row.get('product', {})
    order = row.get('order', {})
    values = [
        row.get('_id', ''),
        product.get('price', ''),
        product.get('quantity', ''),
        product.get('name', ''),
        ','.join(product.get('tags', [])),  # assuming tags is a list, convert it to a comma-separated string
        order.get('id', ''),
        order.get('userDevice', ''),
        order.get('shipping', {}).get('price', ''),
        order.get('shipping', {}).get('method', ''),
        order.get('payment', {}).get('status', ''),
        order.get('payment', {}).get('method', ''),
        row.get('commission', '')
    ]
    ws.append(values)

# Zapisz arkusz Excela
wb.save("dane2.xlsx")
