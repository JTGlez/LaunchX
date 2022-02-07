#Activa el entorno virtual con python3 -m venv env, ubícate en la carpeta del proyecto 
# y ejecuta en consola env\Scripts\activate (Windows). Desactiva con "deactivate".

#pip freeze obtiene las bibliotecas instaladas en el entorno o siste, y con pip install
#puedes instalar una biblioteca de múltiples modos.


#Importa de las bibliotecas datetime y de dateutil.relativedelta todas sus funciones.
from datetime import *
from dateutil.relativedelta import *

#A la variable date implícita now le asigna la fecha y hora actual y la imprime.
now = datetime.now()
print("La fecha y hora del día de hoy es:", now)

#A now ahora se le suma una delta de tiempo (es decir, un cambio) de 1 mes, 1 semana y 10 horas.
now = now + relativedelta(months=1, weeks=1, hour=10)

print("La fecha y hora anterior con la suma de 1 mes, 1 semana y 1 año es", now)