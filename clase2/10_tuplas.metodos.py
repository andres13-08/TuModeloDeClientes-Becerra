proyectos_django = (
    "Blog con sistema de comentarios",
    "E-commerce con carrito de compras y pagos",
    "Red social básica con perfiles y publicaciones",
    "Gestor de tareas (To-Do App) con usuarios",
    "Plataforma de cursos online",
    "Foro con categorías y moderación",
    "Sistema de reservas (turnos, citas, etc.)",
    "Dashboard administrativo con gráficos",
    "Aplicación de encuestas con resultados en tiempo real",
    "API REST para una app móvil usando Django REST Framework",
    "Sistema de reservas (turnos, citas, etc.)",
)

indice = proyectos_django.index("E-commerce con carrito de compras y pagos")
print(indice)

#Número de veces que aparece un elemento.
cuenta = proyectos_django.count("Sistema de reservas (turnos, citas, etc.)")
print(cuenta)