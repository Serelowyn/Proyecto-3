# --------------------------------- IMPORTACIONES ---------------------------------

import pandas as pd

# --------------------------- FIN DE LAS IMPORTACIONES ----------------------------

# ------------------------- METODOS PARA LAS FECHAS :

#       D - DAY
#       H - HOUR
#       min or T - Minute (15min) por ejemplo, para que redonde a los cuartos de minutos mas cercanos
#       S - second


### dt.round("") para redondear a la hora mas cercana
### df.floor()
### dt.ceil()

string_date = '5/13/13 12:04:00'
fecha = pd.to_datetime(string_date, format='%m/%d/%y %H:%M:%S')
print(fecha)


raw_date = '20-12-2002Z04:31:00'
clean_date = pd.to_datetime(raw_date, format="%d-%m-%YZ%H:%M:%S")#escribe el formato aqui)
print(clean_date)


# --------------- Extraer información útil de fechas con .dt en pandas --------------


# ¿Por qué querríamos extraer partes de una fecha?
# Imagina que te han pedido preparar un reporte par saber cuáles son los días más activos en ventas cada mes, por ejemplo a principios de mes e.g el 2 de cada mes o despues de pagar quincenas e.g. el 16. Para descubrirlo, necesitas descomponer las fechas completas en partes como el día, el mes, o incluso la hora.

# Pandas nos permite hacerlo fácilmente... si sabemos cómo.


# El problema: no podemos acceder directamente a los atributos de fecha
# El dataset OnlineRetail.csv registra información de cada transacción, incluyendo la fecha y hora exacta en que ocurrió (InvoiceDate). Vamos a leer el archivo y convertir esta columna a un tipo de dato datetime:

df = pd.read_csv('/datasets/OnlineRetail.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%dT%H:%M:%SZ')

print(df['InvoiceDate'][0].day) #para saber que dia se hizo la primera compra

# Pero, ¿qué pasa si queremos el día de todas las fechas de la columna InvoiceDate?

df['day'] = df['InvoiceDate'].day

# ⛔ Esto da error:

# AttributeError: 'Series' object has no attribute 'day'



# La solución: usa .dt para acceder a los componentes de una columna datetime
# Cuando trabajas con una columna completa de fechas (un objeto Series), necesitas usar el accesor .dt para extraer partes como el día, mes, año, hora, etc.

# Así es como puedes obtener el día de cada factura:


df['Day'] = df['InvoiceDate'].dt.day
print(df[['InvoiceDate', 'Day']].head(5))

# --------------------- ¿Qué más puedes extraer con .dt? -----------------------------

# Pandas te permite acceder a muchos otros atributos de las fechas usando .dt, como:

# .dt.year → año
# .dt.month → mes
# .dt.day → día
# .dt.hour → hora
# .dt.minute → minuto
# .dt.weekday → día de la semana (0 = lunes, 6 = domingo)
# .dt.date → solo la fecha, sin la hora
# Puedes ver más opciones en la documentación oficial.


# 1. Leer datos
df = pd.read_csv('/datasets/OnlineRetail.csv')

# 2. Convertir columna a datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%dT%H:%M:%SZ')

# 3. Extraer el día del mes
#escribe tu codigo aqui
df["Day"] = df["InvoiceDate"].dt.day

# 4. Verifica el resultado
#escribe tu codigo aqui
print(df[['InvoiceDate', 'Day']].head(10))




# ¿Qué es UTC?

# UTC significa Tiempo Universal Coordinado. Es el estándar mundial de tiempo que no cambia con las estaciones. A diferencia de horarios locales (como el de Ciudad de México o Nueva York), UTC no tiene horario de verano.

# Muchas bases de datos y sistemas registran fechas en UTC para mantener consistencia sin importar en qué parte del mundo se recolectaron los datos. Luego, puedes convertir esos valores a la hora local que necesites.

# Ejemplo:

# Si una transacción ocurrió a las 2023-11-01 15:00:00 UTC, en Ciudad de México (horario de invierno, UTC-6) habría ocurrido a las 2023-11-01 09:00:00.

# Usar UTC evita confusiones cuando tus datos vienen de distintos países o cuando hay cambios de horario de verano.



# ------------------------------------------------------------------------------------

# Para convertir datos de un huso horario a otro, pandas ofrece dos herramientas poderosas:

# .dt.tz_localize() — asigna una zona horaria a una columna de tipo datetime.
# .dt.tz_convert() — convierte una columna con zona horaria a otra zona horaria diferente.
# Es decir  .dt.tz_localize()  te permite asignar una zona horaria a una columna datetime para que tus datos "tengan conocimiento" de su zona horaria. .dt.tz_convert() te permite convertir una columna "con conocimiento de su zona horaria" en una zona horaria distinta.


df = pd.read_csv('/datasets/OnlineRetail.csv') #leer datos
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%dT%H:%M:%SZ')#formatear los datos de la fecha

df['InvoiceDate'] = df['InvoiceDate'].dt.tz_localize('UTC')#especificar que los datos de la fecha estan en UTC

print(df['InvoiceDate'].head()) #esto deberia indicar que los datos estan en UTC


# Paso 2: Convertir a otra zona horaria
# Ahora imagina que tu equipo en Nueva York quiere ver los reportes en su hora local. Usamos .tz_convert() para hacerlo:

df['InvoiceDate_NYC'] = df['InvoiceDate'].dt.tz_convert('America/New_York')

print(df['InvoiceDate_NYC'].head())

# 🎯 ¿Qué cambió?

# El dtype de la nueva columna ahora dice America/New_York.
# Las horas han cambiado: ahora están ajustadas a la zona horaria de Nueva York (UTC-5).



position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

dt_months = position["timestamp"].dt.month# escribe tu código aquí
print(dt_months.head(5))




# Localiza correctamente las marcas de tiempo asignándoles la zona horaria 'America/Toronto', y guarda el resultado en una nueva variable llamada dt_toronto. Muestra las primeras cinco filas.

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

dt_toronto = position["timestamp"].dt.tz_localize("America/Toronto")
# escribe tu código aquí

print(dt_toronto.head())

