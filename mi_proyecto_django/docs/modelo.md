# Modelo de datos - Sistema de Tareas

## Entidades principales

### 1. Usuario
- **id** (PK)
- **nombre**
- **correo**
- **fecha_registro**

### 2. Proyecto
- **id** (PK)
- **nombre**
- **descripcion**
- **fecha_inicio**
- **fecha_fin**
- **usuario** (FK → Usuario)
  - Relación **1:N** → Un usuario puede tener varios proyectos.

### 3. Tarea
- **id** (PK)
- **titulo**
- **descripcion**
- **estado** (pendiente, en progreso, completada)
- **fecha_creacion**
- **proyecto** (FK → Proyecto)
  - Relación **1:N** → Un proyecto puede tener varias tareas.

### 4. Etiqueta
- **id** (PK)
- **nombre**
- **color**
- **tareas** (ManyToMany con Tarea)
  - Relación **N:N** → Una tarea puede tener varias etiquetas y viceversa.

---

## Relaciones resumidas

| Relación | Tipo  | Descripción |
|-----------|--------|-------------|
| Usuario → Proyecto | 1:N | Un usuario tiene muchos proyectos |
| Proyecto → Tarea | 1:N | Un proyecto tiene muchas tareas |
| Tarea ↔ Etiqueta | N:N | Una tarea puede tener muchas etiquetas |

---

## Ejemplo visual
```text
Usuario (1) ───< Proyecto (1) ───< Tarea >───< Etiqueta
