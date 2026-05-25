# SkillHub - Sistema de Intercambio de Habilidades

Proyecto academico desarrollado para la asignatura Arquitectura de Software II del ITM.
SkillHub es una plataforma web que permite registrar usuarios, publicar habilidades y
consultar conocimientos disponibles dentro de una comunidad de aprendizaje colaborativo.

## Tecnologias utilizadas

- Django 4.2
- MySQL
- Auth0 para autenticacion
- Apache Kafka para auditoria de eventos
- Azure DevOps para gestion del proyecto y flujo de integracion

## Modulos principales

- Usuarios: permite crear, consultar, editar y desactivar usuarios registrados.
- Habilidades: permite publicar, consultar, filtrar, editar y eliminar habilidades.
- Auditoria: registra eventos importantes del aplicativo mediante Kafka y los almacena
  en la base de datos.

## Flujo DevOps

El proyecto utiliza un flujo de trabajo basado en ramas para controlar la integracion
del codigo fuente:

- develop: rama utilizada para la carga inicial y el desarrollo de nuevas funcionalidades.
- integration: rama utilizada para integrar y validar los cambios provenientes de develop.
- master: rama estable que contiene la version final integrada del proyecto.

Los cambios se promueven entre ramas mediante Pull Requests en Azure DevOps, relacionando
cada integracion con las Historias de Usuario y Tareas correspondientes.

## Objetivo del proyecto

El objetivo de SkillHub es aplicar conceptos de arquitectura de software, gestion de
repositorios, organizacion de trabajo con Azure Boards e integracion de cambios mediante
Pull Requests, manteniendo trazabilidad entre la planeacion y el codigo desarrollado.
