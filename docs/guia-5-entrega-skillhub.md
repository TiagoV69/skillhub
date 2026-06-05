# Guia 5 - Taller evaluativo

## Informacion del estudiante

- Estudiante: [Nombre del estudiante]
- Integrantes del grupo: [Nombres]
- Programa: [Programa academico]
- Asignatura: Arquitectura de Software II
- Proyecto: SkillHub - Sistema de Intercambio de Habilidades
- Fecha: 4 de junio de 2026

## 1. Test Plan en Azure

El plan de pruebas se realizo sobre el sitio web SkillHub, una aplicacion Django para registrar usuarios, publicar habilidades y consultar conocimientos disponibles dentro de una comunidad de aprendizaje colaborativo.

### Prueba 1: Inicio de sesion con Auth0

- Objetivo: Validar que un usuario pueda autenticarse correctamente mediante Auth0.
- Pasos:
  1. Ingresar a la pagina principal de SkillHub.
  2. Hacer clic en "Iniciar sesion".
  3. Completar el flujo de autenticacion en Auth0.
  4. Verificar que la aplicacion muestre la sesion activa.
- Resultado esperado: El usuario autenticado puede acceder a las opciones de habilidades y usuarios.
- Evidencia: [Insertar captura del caso de prueba en Azure Test Plans y captura del resultado en la aplicacion].

### Prueba 2: Creacion de usuario

- Objetivo: Validar el registro de un usuario activo dentro de la plataforma.
- Pasos:
  1. Iniciar sesion.
  2. Ir al modulo "Usuarios".
  3. Seleccionar "Nuevo usuario".
  4. Completar nombre, email, contrasena, confirmacion de contrasena, descripcion y estado.
  5. Guardar el formulario.
- Resultado esperado: El sistema muestra un mensaje de exito y el usuario aparece en la lista.
- Evidencia: [Insertar captura del formulario, mensaje de exito y registro en la lista].

### Prueba 3: Validacion de contrasenas diferentes

- Objetivo: Verificar que el formulario de usuarios controle errores de validacion.
- Pasos:
  1. Ir a "Nuevo usuario".
  2. Ingresar una contrasena y una confirmacion diferente.
  3. Enviar el formulario.
- Resultado esperado: El sistema no crea el usuario y muestra el mensaje "Las contrasenas no coinciden.".
- Evidencia: [Insertar captura del error en el formulario].

### Prueba 4: Publicacion de habilidad

- Objetivo: Validar que se pueda publicar una habilidad asociada a un usuario activo.
- Pasos:
  1. Iniciar sesion.
  2. Ir al modulo "Habilidades".
  3. Seleccionar "Publicar habilidad".
  4. Seleccionar un usuario propietario.
  5. Completar titulo, descripcion, categoria, nivel y disponibilidad.
  6. Guardar la habilidad.
- Resultado esperado: El sistema muestra un mensaje de exito y la habilidad queda visible en el listado.
- Evidencia: [Insertar captura del formulario, mensaje de exito y tarjeta de habilidad].

### Prueba 5: Busqueda y filtrado de habilidades

- Objetivo: Verificar que el listado de habilidades permita consultar informacion por texto, categoria y nivel.
- Pasos:
  1. Ir al modulo "Habilidades".
  2. Ingresar una palabra clave en el campo de busqueda.
  3. Seleccionar categoria y nivel.
  4. Hacer clic en "Filtrar".
- Resultado esperado: El sistema muestra solo las habilidades que cumplen los filtros seleccionados.
- Evidencia: [Insertar captura de los filtros y resultados].

### Bugs o hallazgos identificados

- Hallazgo 1: En algunas plantillas aparecen caracteres especiales corruptos, por ejemplo textos como "EstÃ¡s", "SÃ­" o "Â¿". Esto indica un problema de codificacion en archivos HTML.
- Hallazgo 2: Antes de la correccion, Django detectaba una migracion pendiente en el modulo de habilidades para los campos `descripcion`, `categoria` y `disponibilidad`.

## 2. Archivo YAML

Se creo el archivo `.github/workflows/ci.yml` para evidenciar el flujo de CI/CD del proyecto SkillHub.

El archivo realiza las siguientes acciones:

- Se ejecuta automaticamente cuando hay commits en la rama `master`.
- Tambien se ejecuta cuando se abre o actualiza un Pull Request hacia `master`.
- Permite ejecucion manual mediante `workflow_dispatch`.
- Levanta un servicio MySQL 8.0 para que Django pueda usar una base de datos real durante el pipeline.
- Instala Python 3.11 y las dependencias definidas en `requirements.txt`.
- Ejecuta `python manage.py check` para validar la configuracion de Django.
- Ejecuta `python manage.py makemigrations --check --dry-run` para garantizar que no existan migraciones pendientes.
- Ejecuta `python manage.py migrate --noinput` para aplicar migraciones.
- Ejecuta `python manage.py test --verbosity 2` para correr las pruebas automatizadas.
- Ejecuta `python manage.py collectstatic --noinput` y publica los archivos estaticos como artefacto de entrega.

Evidencia sugerida:

- Captura del archivo `.github/workflows/ci.yml` en el repositorio.
- Captura de la ejecucion del workflow en GitHub Actions.
- Captura de los pasos completados correctamente.

## 3. Disparador del proceso CI/CD

El disparador se configuro en la seccion `on` del archivo YAML:

```yaml
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
  workflow_dispatch:
```

Esto garantiza que cada commit enviado directamente a `master`, o cada Pull Request dirigido a `master`, ejecute automaticamente el proceso de CI/CD.

Para evidenciar los dos commits requeridos se recomienda:

1. Commit 1: agregar el workflow y la migracion pendiente.
   - Mensaje sugerido: `Add CI workflow for SkillHub`
2. Commit 2: agregar o actualizar el documento de evidencias.
   - Mensaje sugerido: `Add guide 5 delivery draft`

Evidencia sugerida:

- Captura del historial de commits mostrando los dos commits.
- Captura de GitHub Actions mostrando dos ejecuciones del workflow.
- Captura del detalle de una ejecucion exitosa.

## 4. Feedback y retrospectiva individual

### Que hice bien

Durante el desarrollo se mantuvo el proyecto SkillHub como caso de estudio del curso, integrando modulos funcionales de usuarios, habilidades, autenticacion y auditoria. Tambien se avanzo en la automatizacion del flujo de integracion mediante un archivo YAML que valida la configuracion del proyecto y prepara una entrega reproducible.

### Que hice mal

Se identifico que algunas plantillas tenian problemas de codificacion en caracteres especiales. Tambien se encontro una migracion pendiente que podia afectar la ejecucion correcta del pipeline si no se corregia antes de integrar los cambios.

### Como equipo, que debemos seguir haciendo

Como equipo debemos seguir usando ramas, Pull Requests y validaciones automaticas para integrar cambios con mayor seguridad. Tambien debemos documentar mejor las evidencias, mantener las migraciones actualizadas y agregar pruebas automatizadas para los casos principales del sistema.
