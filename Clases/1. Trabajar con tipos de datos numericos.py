# Trabajar con tipos de datos numéricos y de string


# ----------- IMPORTACIONES -----------

import pandas as pd
import numpy as np

# --------- FIN DE LAS IMPORTACIONES -----------

# ¿Qué es un tipo de datos object?
# Cuando trabajas con un conjunto de datos en Python (usando pandas), cada columna tiene un tipo de dato. Eso le dice a Python qué tipo de valores hay en esa columna: números, texto, fechas, etc.

# El tipo object es como un cajón donde pandas pone todo lo que no puede clasificar claramente como número o fecha. Por lo general, eso significa que la columna contiene texto, pero también podría haber mezcla de cosas raras, como números escritos como texto, espacios vacíos, símbolos, o incluso una mezcla de números y letras.

# Reflexión breve y siguientes pasos
# Qué aprendiste:

# Al leer datos, no debemos asumir que Python asigna los tipos de datos que esperamos.
# Siempre es buena idea llamar a info() en tu DataFrame antes de lanzarte a hacer cálculos y modificaciones. Haz de esto una rutina.
# En la próxima lección, aprenderemos a cambiar los datos de una columna de un tipo a otro e identificar por qué pandas no logró detectar el tipo de datos correcto para la columna 'UnitPrice'.

# ¿Qué haremos en esta clase?
# En la lección anterior descubrimos que algunas columnas de nuestro dataset no tienen el tipo de datos correcto. En esta clase, vamos a corregir esos errores usando astype() y to_numeric().

# Recordatorio: columnas con tipos incorrectos
# Al revisar el dataset con df.info(), identificamos lo siguiente:

# 'StockCode': aparece como tipo object, pero contiene números → debería ser int.
# 'UnitPrice': también aparece como object, pero debería ser un número decimal (float).
# 'Quantity': está como float64, pero representa cantidades enteras → debería ser int.
# Vamos a corregir un par de estos casos.

# Convertir a un tipo de datos específico con astype()
# El método astype() de pandas te permite convertir tipos de datos.

# Al igual que con otros métodos de pandas, existe para DataFrames y Series.

# Al usarlo, debes especificar entre paréntesis el tipo de datos al cual deseas convertirlo. Por ejemplo, df['column'] = df['column'].astype('int') convertiría la columna 'column' al tipo de datos entero.

data = {
    'StockCode': ['10001', '10002', '10003', '10004', '10005', '10006'],
    'Description': ['Mug', 'T-shirt', 'Notebook', 'Invalid Code', 'Float code', 'Pen'],
    'Quantity': [10, 5, 8, 1, 3, 6],
    'UnitPrice': [2.5, 15.0, 4.2, 1.0, 6.75, 1.5]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

#1. Convert 'StockCode' to integer type 'int'
df['StockCode'] = df['StockCode'].astype('int')

#2. Validate the change by executing the info() method on the dataframe
df.info()



# Convertir strings a valores numéricos
# En los casos sencillos como el anterior, el método astype() funciona de maravilla. Pero astype() puede convertir strings a números, solo si el formato del string coincide exactamente con el tipo de datos al que estás convirtiendo. 

# Por ejemplo, 
# - convertir el string '1.0' -> flotante si se puede.
# - convertir el string '1' -> entero si se puede. 
# - convertir el string '1.0' (en formato de flotante) -> entero no se puede.

# Ejecuta el código y observa el error cuando intentamos convertir strings de la col1 que representan valores flotantes en enteros:


# crear un dataframe con 2 columnas
d = {'col1': ['1.0', '2.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

# convertir la segunda columna 'col2' a int
df['col1'] = df['col1'].astype('int')

#verificar el data type de las columnas utilizando el metodo '.dtypes'
print(df.dtypes)



# Como puedes ver. El resultado arroja un error. 

# Para solventar este problema, usaremos un método más flexible llamado to_numeric()

# Convertir Strings a entero con el metodo "to_numeric"
# Cuando intentas convertir strings a números, el método astype() solo funciona si todos los valores son válidos y perfectamente formateados. 

# Aquí es donde to_numeric() se vuelve útil. A diferencia de astype(), el método to_numeric() si hace dichas conversiones:

# Ejecuta el código y observa el resultado.

d = {'col1': ['1.0', '2.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

df['col1'] = pd.to_numeric(df['col1'])
print(df.dtypes)


# Funciona muy bien si tienes strings similares a números como '72' o '1.394'.

# No obstante, de forma predeterminada, to_numeric() no puede convertir strings con caracteres no numéricos o decimales en números. Pero para eso esta el parametro errors=.

# El parámetro errors= te permite decidir qué hacer si pandas encuentra un valor que no puede convertir:

# errors='raise' (por defecto): se detiene y lanza un error (igual que astype()).
# errors='coerce': reemplaza los valores no numéricos con NaN (muy útil para limpieza de datos).
# errors='ignore': deja los valores originales sin intentar convertirlos.
# Ahora probemos convertir una columna con un valor no numerico, por ejemplo B.0, a entero.

# Para eso, vamos a añadir el parametro errors='coerce' el cual remplazará el valor no valido  por NaN. 

# Así es como se ve:


d = {'col1': ['1.0', 'B.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

df['col2'] = df['col2'].astype('int')
df['col1'] = pd.to_numeric(df['col1'], errors='coerce')

print(df.dtypes)
print(df)





# Ahora, utiliza  la funcion to_numeric() para los datos de la columna 'UnitPrice' 

# Convierte la columna 'UnitPrice' de object a float
#  a. Usa la función to_numeric().
#  b. Usa el parámetro errors= que remplaza valores inválidos con NaN.
# Verifica los resultados llamando al método info() en el DataFrame.

df = pd.read_csv('/datasets/OnlineRetail.csv')

#1. Convierte la columna `'UnitPrice'` de `object` a `float`
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

#2. Verifica los resultados llamando al método `info()` en el DataFrame.
df.info()



# ¿Convertimos Quantity a float?
# Siguamos con la siguiente columna, Quantity la cual debemos convertir de flotante a entero  

# Pero antes de convertirla a enteros (int), es importante verificar si existen valores con decimales. Aunque en la mayoría mayoría de los casos, esperas cantidades enteras, como 2 camisetas o 12 tazas. talvez existan valores como 0.5 kilos o 0.25 metros de listón. Si hay alguno de estos, podrías perder información importante al convertir.

# ¿Pero cómo saber si todos los valores de esta columna son enteros, aunque el tipo de datos sea float?

# Aquí es donde entra np.array_equal()

# ¿Qué hace np.array_equal()?
# Imagina que tienes dos listas de números y quieres saber si son exactamente iguales, posición por posición. Eso es justo lo que hace np.array_equal(array1, array2).

# Sintaxis

# np.array_equal(array1, array2)

# Esta funcion hace parte de NumPy, una librería de Python que hace que trabajar con números sea mucho más fácil y rápido. Pandas usa NumPy “por debajo del capó” para manejar datos, especialmente cuando queremos hacer operaciones matemáticas con muchos valores a la vez.

# ¿Qué es un array?
# Un array (o arreglo) en NumPy es como una lista de Python

# ¿Qué resultado arroja?
# Devuelve True si todos los elementos de ambos arrays son iguales y en el mismo orden. Si hay al menos un número diferente, devuelve False.

# Para ilustrar esto, mira el siguiente ejemplo donde revisamos si al convertir los valores de la primera columna a enteros resultan los mismos valores:

d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)

# comprueba si es seguro convertir 'col1' con np.array_equal
print(np.array_equal(df['col1'], df['col1'].astype('int')))



#¡Excelente! No hubo ningún problema. Ahora prueba con 'col2':

d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)

# comprueba si es seguro convertir 'col1' con np.array_equal
print(np.array_equal(df['col2'], df['col2'].astype('int')))

#Ahora sabemos que no podemos convertir 'col2' de float a int sin perder algunos de los datos.





# Ahora, probemos con los datos de la columna 'Quantity' 

# En el primer paso usa numpy para comprobar si no hay problema con convertir la columna 'Quantity' de float a int sin modificar los valores. Muestra la expresión que evalúa si es True o False.

df = pd.read_csv('/datasets/OnlineRetail.csv')

resultado = np.array_equal(df['Quantity'], df['Quantity'].astype('int'))

print(resultado)





# 2. Ahora realiza la operación de conversión utilizando el método astype(). Convierte la columna 'Quantity' de float a int, después verifica los resultados llamando el método info() en el DataFrame.


#convierte los valores de la columna a enteros
df = pd.read_csv('/datasets/OnlineRetail.csv')

#Valida el resultado con el metodod info() 
df['Quantity'] = df['Quantity'].astype('int')
df.info()


# Resumen
# Usa astype() para convertir un tipo de datos en otro.
# No todos los tipos de datos se pueden convertir entre sí usando astype(); algunas conversiones (como strings tipo float a enteros) podrían arrojar un error.
# Ten cuidado cuando hagas conversiones que pudieran alterar significativamente los datos originales.
# Al convertir los strings en números, el método to_numeric() podría ser mejor opción gracias a la flexibilidad que le brinda el parámetro errors