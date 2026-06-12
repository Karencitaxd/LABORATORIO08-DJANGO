# 🌎 LABORATORIO 08 - DESTINOS TURÍSTICOS CON DJANGO

## 📌 Descripción

Este proyecto consiste en el desarrollo de una aplicación web utilizando el framework Django para la gestión de destinos turísticos del Perú.

La aplicación permite visualizar destinos turísticos almacenados en una base de datos mediante vistas dinámicas utilizando los tags `{% for %}` y `{% if %}` de Django. Además, implementa operaciones CRUD completas para administrar la información de los destinos.

---

## 🎯 Objetivos

* Implementar una aplicación web utilizando Django.
* Utilizar una base de datos para almacenar destinos turísticos.
* Mostrar información mediante plantillas dinámicas.
* Aplicar los tags `for` e `if` en las vistas HTML.
* Implementar formularios para agregar, editar y eliminar registros.
* Utilizar Git y GitHub para el control de versiones.

---

## 🛠 Tecnologías Utilizadas

* Python 3
* Django 4.2
* SQLite3
* Bootstrap 5
* HTML5
* CSS3
* Git
* GitHub
* Pillow

---

## 📂 Modelo Utilizado

### DestinoTuristico

Campos implementados:

* nombreCiudad
* descripcionCiudad
* imagenCiudad
* precioTour
* ofertaTour

---

## ⚙️ Funcionalidades Implementadas

### CRUD Completo

* ✅ Listar destinos turísticos
* ✅ Agregar destinos turísticos
* ✅ Editar destinos turísticos
* ✅ Eliminar destinos turísticos

### Plantillas Dinámicas

* ✅ Uso de `{% for %}`
* ✅ Uso de `{% if %}`

### Interfaz

* ✅ Navbar profesional
* ✅ Banner principal
* ✅ Tarjetas Bootstrap
* ✅ Efecto Hover
* ✅ Footer informativo
* ✅ Visualización de imágenes

---

## 🌎 Destinos Registrados

* Arequipa
* Lago Titicaca
* Cusco
* Machu Picchu
* Ica - Huacachina
* Tarapoto
* Valle del Colca

---

## 🚀 Ejecución del Proyecto

### Clonar repositorio

```bash
git clone https://github.com/Karencitaxd/LABORATORIO08-DJANGO.git
```

### Ingresar al proyecto

```bash
cd LABORATORIO08-DJANGO
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar migraciones

```bash
python manage.py migrate
```

### Ejecutar servidor

```bash
python manage.py runserver
```

---

## 👩‍💻 Autor

Karen Alexandra Álvarez Molina

Curso: Desarrollo de Aplicaciones Web

Laboratorio 08 - Django Destinos Turísticos
