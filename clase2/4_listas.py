proyectos_django = [
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
]

proyectos_django.insert(0, "App para gestión de eventos")
print(proyectos_django)

proyectos_django_ia = [
    "Chatbot integrado en un sitio web usando un modelo de lenguaje",
    "Sistema de recomendación (productos, cursos o contenido) basado en machine learning",
    "Clasificador automático de imágenes o textos (subes un archivo y la IA lo analiza)",
]

proyectos_django.extend(proyectos_django_ia)

proyectos_django.remove("Foro con categorías y moderación")
print(proyectos_django)