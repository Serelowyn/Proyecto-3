# --------------------------------- IMPORTACIONES ----------------------------------

import pandas as pd
import numpy as np

# ----------------------------- FIN DE LAS IMPORTACIONES ---------------------------

#-----------------------este codigo es para categorizar
df = pd.read_csv('/datasets/vg_sales.csv')

# escribe aquí la definición de tu función
def score_group(score):
    """La funcion devuelve la categoria por puntuacion obtenida:\n- Low (bajo) para calificaciones menores a 60.\n- Medium (medio) para calificaciones entre 60 y 79\n- High (alto) para calificaciones de 80 o mayor\n- No score para los que no tienen valor numerico en la lista (NaN).\n
    """
    if score < 60:
        return "Low"
    elif score > 60 and score < 80:
        return "Medium"
    elif score >= 80:
        return "High"
    else:
        return "No score"
# imprime los resultados de llamar a la función con estos inputs en orden: 10, 65, 99, np.nan
print(score_group(10))
print(score_group(65))
print(score_group(99))
print(score_group(np.nan))


# ------------------- tarea 2

df = pd.read_csv('/datasets/vg_sales.csv')

def score_group(score):
    if score < 60:
        return 'low'
    elif score < 80:
        return 'medium'
    elif score >= 80:
        return 'high'
    else:
        return 'no score'

df['score_categorized'] = df["critic_score"].apply(score_group)# escribe tu código aquí
print(df.head())

# ----------------------- tarea 3

df = pd.read_csv('/datasets/vg_sales.csv')

def score_group(score):
    if score < 60:
        return 'low'
    elif score < 80:
        return 'medium'
    elif score >= 80:
        return 'high'
    else:
        return 'no score'

df['score_categorized'] = df['critic_score'].apply(score_group)

df_grouped = df.groupby("score_categorized")# escribe tu código aquí
df_sum = df_grouped["na_sales"].sum() # escribe tu código aquí

print(df_sum)

# ------------------- tarea 1

df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row):# escribe tu función aquí
    critic_score = row["critic_score"]
    user_score = row["user_score"]
    
    avg_score =  (critic_score + user_score  * 10) / 2
    
    if avg_score < 60:
        return "low"
    elif avg_score > 60 and avg_score < 80:
        return "medium"
    elif avg_score > 80:
        return "high"


# parte de prueba a continuación, por favor no la cambies

col_names = ['critic_score', 'user_score']
test_low  = pd.Series([10, 1.0], index=col_names)
test_med  = pd.Series([65, 6.5], index=col_names)
test_high = pd.Series([99, 9.9], index=col_names)

rows = [test_low, test_med, test_high]

for row in rows:
    print(avg_score_group(row))
    
    
# -------------------------- tarea 2

df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row):
    critic_score = row['critic_score']
    user_score = row['user_score']
    
    avg_score = (critic_score + user_score * 10) / 2
    
    if avg_score < 60:
        return 'low'
    if avg_score < 80:
        return 'medium'
    if avg_score >= 80:
        return 'high'


# crea las filas de input de prueba aquí
row_1 = pd.Series([66, 3.6], index=["critic_score", "user_score"])
row_2 = pd.Series([72, 8.1], index=["critic_score", "user_score"])
row_3 = pd.Series([99, 9.4], index=["critic_score", "user_score"])
    
# imprime los resultados de llamar a la función con los input de prueba en orden
print(avg_score_group(row_1))
print(avg_score_group(row_2))
print(avg_score_group(row_3))


