# ---------------------------------------- IMPORTACIONES ------------------------------------------

import pandas as pd
from matplotlib import pyplot as plt

# ------------------------------------- FIN DE LAS IMPORTACIONES -----------------------------------

df_orders = pd.read_csv("/datasets/instacart_orders.csv")
df_products = pd.read_csv("/datasets/products.csv")
df_aisles = pd.read_csv("/datasets/aisles.csv")
df_departments = pd.read_csv("/datasets/departments.csv")
df_orderproducts = pd.read_csv("/datasets/order_products.csv")

# mostrar información del DataFrame
print(df_orders)
print(df_products)
print(df_aisles)
print(df_departments)
print(df_orderproducts)