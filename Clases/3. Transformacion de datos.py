import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

grp = df.groupby('genre')

agg_dict = {# escribe aquí tu diccionario con cuatro tuplas, una por cada variable
    "total_sales": "sum",
    "na_sales": "mean",
    "eu_sales": "mean",
    "jp_sales": "mean"
}

genre = grp.agg(agg_dict)# utiliza aquí la función agg

# muestra aquí los resultados
print(genre)



# ----------- -------------------- TABLAS DINAMICAS ----------------------------------

df = pd.read_csv('/datasets/vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df_pivot = df.pivot_table(index="genre",
                                columns="year_of_release",
                                values="jp_sales",
                                aggfunc="mean"
                                )

# escribe tu código aquí
print(df_pivot)

# ----------------------------------

df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()

num_pubs = df.groupby("platform")["publisher"].nunique()# escribe tu código aquí

# imprime aquí
print(num_pubs)

#---------------- EJEMPLO DEL DE ARRIBA

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Sumar por columnas (hacia abajo)
suma_columnas = df.sum(axis='index')  # Resultado: A=6, B=15, C=24

# Sumar por filas (hacia la derecha) 
suma_filas = df.sum(axis='columns')
suma_filas

# ------------- FIN DEL EJEMPLO


df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()
num_pubs = df.groupby('platform')['publisher'].nunique()

platforms = pd.concat([total_sales, num_pubs], axis="columns")

# cambia los nombres de las columnas aquí
platforms.columns = ["total_sales", "num_publishers"]
# muestra tu resultado
print(platforms)


# ------------------------------------

df_members = pd.read_csv('/datasets/new_members.csv')
df_orders  = pd.read_csv('/datasets/recent_orders.csv')

df_merged = df_members.merge(df_orders,
                             left_on="id",
                             right_on="user_id",
                             suffixes=("_member", "_order")
                            )

print(df_merged)


# ----------------------------

df_members = pd.read_csv('/datasets/new_members.csv')
df_orders  = pd.read_csv('/datasets/recent_orders.csv')

df_merged = df_members.merge(df_orders,
                             left_on='id',
                             right_on='user_id',
                             suffixes=('_member', '_order'))

# escribe tu código aquí
df_merged = df_merged.drop("user_id", axis="columns")
print(df_merged)