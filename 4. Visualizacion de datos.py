# ---------------------------------- IMPORTACIONES ---------------------------------

import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

#en cuestion de matplotlib import pyplot... es una de las cosas que se pueden hacer, igual existe "ANIMATION" para animaciones, "MPLOT3D" para graficos 3d y "WIDGETS" PARA ELEMENTOS INTERACTIVOS.

# ------------------------------ FIN DE LAS IMPORTACIONES --------------------------



cases = [33, 61, 86, 112, 116, 129, 192, 174, 344, 304, 327, 246, 320, 339, 376]

dates = ['March<br>'] * len(cases)
day = 18
for i in range(len(dates)):
    dates[i] = dates[i] + str(day)
    day = day + 1
dates[-1] = 'April<br>1'

labels = dict(date="Date", cases="Number of cases")
markers = dict(size=30, line=dict(width=2, color='black'), color='white')
title = dict(text='New Cases Per Day', font=dict(color='white', size=30))
yaxis = dict(tickmode='linear', tick0=30, dtick=30)

df = pd.DataFrame({'cases': cases, 'date': dates})

fig = px.line(df, y='cases', x='date', text='cases', markers=True, labels=labels, title="New Cases Per Day")

fig.update_xaxes(showgrid=False, color='white', tickangle=0)
fig.update_yaxes(color='white', gridcolor='#5c5a5c', gridwidth=2, range=[15, 400])
fig.update_traces(marker=markers, line_color='white', line_width=6)
fig.update_layout(title=title,
                  title_x=0.5,
                  paper_bgcolor='#070230',
                  plot_bgcolor='#070230',
                  yaxis=yaxis,
                  xaxis_type='category')
fig.add_annotation(text='TOTAL CASES', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=12),
                    xref='paper',
                    yref='paper',
                    x=1.08,
                    y=1.25)
fig.add_annotation(text='3,342', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=23),
                    xref='paper',
                    yref='paper',
                    x=1.071,
                    y=1.2)

fig.show()


# --------------------------------------

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
print(df)

df.plot()
plt.show()

#lo mismo pero en menos lineas de codigo
df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df['b'].plot()
plt.show()

# para guardar imagen

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df['b'].plot()
plt.savefig('myplot.png')

# para poner titulos

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B')
plt.show()

# para el estilo de las letras

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='o')
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='x')
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='o-')
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o')
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b',
        y='a',
        title='A vs B',
        style='o',
        xlabel="Hola, soy B",
        ylabel="Hola, soy A")

plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b',
        y='a',
        title='A vs B',
        style='o',
        legend=False)

plt.xlabel("Hola, soy B") # configurando la leyenda x
plt.ylabel("Hola, so A") # configurando la leyenda y
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], ylim=0)
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o', grid=True)
plt.show()

#

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

# construir una gráfica pequeña
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[2, 2])

# construir una gráfica grande
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[10, 4])

plt.show()

# 

# ------------------------------ EJERCICIOS -----------------------------------------

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})

df.plot(x="c",
        y="a",
        title= "A vs C",
        style="*",
        color="hotpink",
        figsize=[5, 5],
        xlim=[0, 12],
        ylim=[1, 6],
        xlabel="C",
        ylabel="A"
        )
plt.show()

# -----------------------------------------

df = pd.read_csv('/datasets/height_weight.csv')

df.plot(x="height",
        y="weight",
        title="Adult heights",
        alpha=0.36,
        figsize=[8, 6],
        xlabel="Age / years",
        ylabel="Height / inches",
        kind="scatter"
        )

plt.show()

# -------------------------------------

df = pd.read_csv('/datasets/height_weight.csv')
# Obtén los coeficientes de correlación para la columna 'male' con cada una de las otras tres columnas. Pero en lugar de llamar corr() en la columna 'male' tres veces por separado, crea una matriz de correlación y extrae los tres coeficientes que deseas. El resultado debería ser un objeto Series con tres elementos, uno para cada coeficiente.

# Asigna la matriz de correlación a una variable llamada corr_mat y asigna el Series de coeficientes a una variable llamada male_corr. Luego, muestra male_corr.

# Usa loc[] con 'male' como el primer argumento, y una lista de los otros datos como el segundo argumento para extraer aquellos valores para la variable male_corr.

corr_mat = df.corr()
male_corr = corr_mat.loc['male', 'height':'age']
print(male_corr)

# --------------- GRAFICOS DE LINEAS

# --------------------------- Ejercicio 1

df = pd.read_csv('/datasets/sbux.csv')

df.plot(title="Historic SBUX volume",
        x="date",
        y="volume",
        rot=50,
        legend=False,
        ylim=[1e6, 7e7]
        )

plt.show()

# --------------------------- Ejercicio 2

df = pd.read_csv('/datasets/sbux.csv')
cols = ['open', 'close']

df.plot(title="Historic SBUX price",
        x="date",
        y=cols,
        xlabel="date",
        ylabel="Share price / USD",
        rot=50
        )

plt.show()

# --------------------------- Ejercicio 1

df = pd.read_csv('/datasets/west_coast_pop.csv')

df = pd.read_csv('/datasets/west_coast_pop.csv')

df.plot(x='year',
        y=['or_pop', 'wa_pop'],#se especifica cuales estados, hay 3, ocupamos solo 2
        kind='bar',
        title='Pacific Northwest population growth',
        xlabel='Year',
        ylabel='Population (millions)')

plt.legend(['OR', 'WA'])
plt.show()

# --------------------------- Ejercicio 2

df = pd.read_csv('/datasets/height_weight.csv')

# separa df en dataframes separados según la edad
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# print out the results
print("La suma de las longitudes del dataframe:", len(df_20s) + len(df_30s) + len(df_40s))
print("Edad mínima y máxima para df_20s:", df_20s["age"].min(), df_20s["age"].max())
print("Edad mínima y máxima para df_30s:", df_30s["age"].min(), df_30s["age"].max())
print("Edad mínima y máxima para df_40s:", df_40s["age"].min(), df_40s["age"].max())

# --------------------------- Ejercicio 3

df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

df_20s['weight'].plot(bins=20,
                      title="Weight / lbs",
                      ylabel="Frequency",
                      kind="hist")

df_30s['weight'].plot(bins=20,
                      alpha=0.6,
                      kind="hist")
df_40s['weight'].plot(bins=20,
                      alpha=0.3,
                      kind="hist")

plt.legend(["20s", "30s", "40s"])

plt.show()