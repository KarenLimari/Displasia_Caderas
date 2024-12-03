# Evaluación de Displasia de Caderas

Este proyecto está diseñado para asistir a los Tecnólogos Médicos en Imagenología (TMS) en la evaluación rápida y oportuna de la displasia de cadera en niños. A través de mediciones realizadas en radiografías de pelvis pediátricas, este código ayuda a generar alertas que priorizan casos y facilitan la elaboración de informes radiológicos.

## Descripción

La displasia de cadera es una condición que, si no se detecta a tiempo, puede tener consecuencias graves en la salud del paciente. Este proyecto utiliza la clasificación del **International Hip Dysplasia Institute** y aplica técnicas clínicas estándar como el trazado de:

- Líneas de **Hilgenreiner** y **Perkins**
- Línea de **Shenton**
- **Ángulo acetabular**
- Posición de la cabeza femoral

El sistema permite que los TMS ingresen las mediciones obtenidas con las herramientas digitales de radiología y evalúa automáticamente los resultados, generando alertas para priorizar la atención médica.

## Funcionalidades

### 1. Clase `Radiografía`

- Encapsula la información y métodos necesarios para ingresar y evaluar las mediciones.
- Permite ingresar datos como el ángulo acetabular, la posición de la cabeza femoral y signos clínicos.

### 2. Evaluación Automática

- Verifica si las mediciones cumplen con los rangos normales:
  - Línea de **Shenton**
  - **Ángulo acetabular**
  - Posición de la cabeza femoral
- Genera alertas en caso de resultados anormales.

### 3. Resultados Claros

- Proporciona un resumen con las mediciones ingresadas y las alertas generadas, facilitando la interpretación.

## Utilidad Clínica

Este proyecto optimiza el proceso de diagnóstico al permitir evaluaciones preliminares realizadas por TMS antes de la revisión médica formal. Aunque no sustituye la labor del médico radiólogo, **proporciona un apoyo importante en la detección temprana de displasia de cadera pediátrica**.

### Beneficios:

- Priorización de casos críticos.
- Mayor eficiencia en la generación de informes.
- Promueve la detección temprana en niños desde los 3 meses de edad (según indicación médica).

## Contexto del Proyecto

Después de años de experiencia como Tecnóloga Médica en Imagenología, he comprendido cómo la implementación de herramientas tecnológicas puede mejorar significativamente la práctica clínica. A través de este proyecto, exploro cómo el uso de programación puede complementar y optimizar el diagnóstico en casos pediátricos.

Si bien el código actual es sencillo, estoy convencida de que con más desarrollo y refinamiento, podría convertirse en una herramienta integral para el diagnóstico temprano y oportuno de displasia de cadera.

## Requisitos

Para ejecutar este proyecto, se requiere tener instalado:

Sistema Operativo: Windows, Linux, MacOS
Lenguaje de programación: Python 3.12

## Instalación y Uso

1. **Clonar el repositorio**:

```bash
git clone https://github.com/KarenLimari/Displasia_Caderas.git
cd main,py
```

- Ingresa las mediciones de la radiografía según las instrucciones proporcionadas.
  Recibe un resumen de las mediciones y las alertas generadas.

## Autor

[Karen Limari](https://github.com/KarenLimari)

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE.md para más detalles.
