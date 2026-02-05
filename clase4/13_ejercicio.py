# Generaciones
# 1920 - 1940 "Generación Silenciosa"
# 1941 - 1960 "Baby Boomers"
# 1961 - 1980 "Generación X"
# 1981 - 1996 "Millennials"
# 1997 - 2012 "Generación Z"
# 2013 - presente "Generación Alpha"


año = int(input("Ingrese su año de nacimiento: "))

if año >= 1920 and año <= 1940:
	generacion = "Generación Silenciosa"

elif año >= 1941 and año <= 1960:
	generacion = "Baby Boomers"

elif año >= 1961 and año <= 1980:
	generacion = "Generación X"

elif año >= 1981 and año <= 1996:
	generacion = "Millennials"

elif año <= 1997 and año >= 2012:
	generacion = "Generación Z"

if generacion:
	print(f"El año {año} pertenece a la generación {generacion}")    

else:
	print(f"No existe una generación asociada al año {año}")