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

# ------------------ verificar duplicados en el 2do data frame, df_products

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


### ------------------- `departments` data frame ------------------------------------

# ------------------- revisar si hay filas duplicadas
df_departments[df_departments.duplicated()]

# ----------------- revisa únicamente si hay IDs duplicadas de departamentos
df_departments[df_departments["department_id"].duplicated()]


### ------------------- `aisles` data frame-----------------------

# Revisa si hay filas totalmente duplicadas
df_aisles[df_aisles.duplicated()]

# Revisa únicamente si hay IDs duplicadas de pasillos
df_aisles[df_aisles["aisle_id"].duplicated()]


### ----------------------- `order_products` data frame --------------------

# Revisa si hay filas totalmente duplicadas
duplicates_order = df_orderproducts[df_orderproducts.duplicated()]
print(duplicates_order)

# Vuelve a verificar si hay cualquier otro duplicado engañoso
duplicado_enganioso = df_orderproducts[df_orderproducts.duplicated(subset=["order_id", "product_id"])]
print(duplicado_enganioso)


### --------------- products DATAFRAME --------------------

# Encuentra los valores ausentes en la columna 'product_name'
val_aus_prod = df_products[df_products["product_name"].isna()]
val_aus_prod


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21
id100 = df_aisles[df_aisles["aisle_id"] == 100]
id21 = df_departments[df_departments["department_id"] == 21]
id100
id21

# Completa los nombres de productos ausentes con 'Unknown'
df_products["product_name"].fillna("Unknown", inplace=True)

### ---------------------- `orders` data frame -----------------------------------

# Encuentra los valores ausentes
print(df_orders.isna().sum())


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
nan_orders = df_orders[df_orders["days_since_prior_order"].isna()]
print("Pedidos con valores ausentes en days_since_prior_order:")
print(nan_orders.head())

# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
# Primero identificamos el primer pedido de cada usuario
primer_pedido_orders = df_orders.sort_values(by=["user_id","order_number"]).groupby("user_id").first()

# Comparamos los pedidos con NaN contra los primeros pedidos de cada usuario
nan_orders_check = nan_orders.merge(
    primer_pedido_orders[["order_id"]],
    on="order_id",
    how="left",
    indicator=True)

# Revisamos si todos los NaN coinciden con el primer pedido
print(nan_orders_check["_merge"].value_counts())

##### opcional 2
na_orders_not_first = df_orders[
    df_orders["days_since_prior_order"].isna() & (df_orders["order_number"] > 1)
]
print(na_orders_not_first)
#####


# ------------------------------ Order_Products DataFram ----------------------------------

# Encuentra los valores ausentes en la columna 'add_to_cart_order'
print(df_orderproducts)
print(df_orderproducts.isna().sum())

# ¿Cuáles son los valores mínimos y máximos en esta columna?
print("Valor mínimo:", df_orderproducts["add_to_cart_order"].min())
print("Valor máximo:", df_orderproducts["add_to_cart_order"].max())

# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
nan_cart = df_orderproducts[df_orderproducts["add_to_cart_order"].isna()]
nan_order_ids = nan_cart["order_id"].unique()
print(nan_order_ids)


# Filtrar solo los pedidos con valores ausentes en add_to_cart_order
pedidos_nulos = df_orderproducts[df_orderproducts["add_to_cart_order"].isna()]
# Agrupar esos pedidos por order_id y contar cuántos productos tiene cada uno
nulos_agrupados_productid = pedidos_nulos.groupby("order_id")["product_id"].count()
print(nulos_agrupados_productid)
# Revisar el valor mínimo del conteo
print("Valor minimo:", nulos_agrupados_productid.min())
print("Valor maximo:", nulos_agrupados_productid.max())


# Reemplazar los valores ausentes en la columna 'add_to_cart_order' con 999
df_orderproducts["add_to_cart_order"] = df_orderproducts["add_to_cart_order"].fillna(999)

# Convertir la columna al tipo entero
df_orderproducts["add_to_cart_order"] = df_orderproducts["add_to_cart_order"].astype(int)

# Verificar que ya no haya valores ausentes
print(df_orderproducts["add_to_cart_order"].isna().sum())

# Revisar los primeros registros para confirmar el cambio
print(df_orderproducts.head())