# ---------------------------------------- IMPORTACIONES -------------------------------------

import pandas as pd
from matplotlib import pyplot as plt

# ------------------------------------- FIN DE LAS IMPORTACIONES -----------------------------

df_orders = pd.read_csv("instacart_orders.csv", sep=";")
df_products = pd.read_csv("products.csv", sep=";")
df_aisles = pd.read_csv("aisles.csv", sep=";")
df_departments = pd.read_csv("departments.csv", sep=";")
df_orderproducts = pd.read_csv("order_products.csv", sep=";")

# mostrar información del DataFrame
print(df_orders)
print(df_products)
print(df_aisles)
print(df_departments)
print(df_orderproducts)

# ----------------------------- verificar duplicados en el primer data frame, df_orders

df_orders = df_orders.drop_duplicates()
print(df_orders)

# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.
#### ---- Dias de la semana 0 domingo, horas 2 para am, formato 24H

miercoles_2am = df_orders[(df_orders["order_dow"] == 3) & (df_orders["order_hour_of_day"] == 2)]
miercoles_2am.drop_duplicates()
miercoles_2am.duplicated() #para verificar si hay duplicados

# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
pedidos_duplicados = df_orders["order_id"]
pedidos_duplicados.drop_duplicates(inplace=True)
pedidos_duplicados

# ----------------------------- verificar duplicados en el 2do data frame, df_products

df_products.drop_duplicates(inplace=True)
df_products

# Revisa únicamente si hay ID de productos duplicados
prod_duplicados = df_products["product_id"]
prod_duplicados.drop_duplicates(inplace=True)
prod_duplicados

# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
df_products["product_name"] = df_products["product_name"].str.upper()
df_products[df_products["product_name"].duplicated()]


# Revisa si hay nombres duplicados de productos no faltantes
df_products[df_products["product_name"].notna() & df_products["product_name"].duplicated()]


### `departments` data frame ------------------------------------

# ------------------- revisar si hay filas duplicadas
df_departments[df_departments.duplicated()]

# ----------------- revisa únicamente si hay IDs duplicadas de departamentos
df_departments[df_departments["department_id"].duplicated()]