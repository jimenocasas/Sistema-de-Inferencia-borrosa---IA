# Sistema de Inferencia Borrosa para Concesión de Préstamos  

## Descripción
Este proyecto desarrolla un sistema de inferencia borrosa (MFIS – Mamdani Fuzzy Inference System) aplicado al ámbito bancario.  
El objetivo es apoyar al Banco Pichin en la evaluación del riesgo de solicitudes de préstamos personales a partir de variables socioeconómicas.  

El sistema recibe como entrada datos de cada solicitante (edad, ingresos, bienes, historial crediticio, tipo de contrato, entre otros) y devuelve un nivel de riesgo (bajo, medio o alto), facilitando la decisión sobre la concesión del préstamo.  

## Funcionalidades implementadas
### Definición de variables de entrada
- Edad, ingresos, bienes, estabilidad laboral, historial crediticio y relación préstamo/ingresos.  
- Conjuntos borrosos definidos mediante funciones trapezoidales y triangulares.  

### Definición de reglas de inferencia
- Basadas en conocimiento experto (formato `var=label`).  
- Operador lógico AND implícito en los antecedentes.  

### Implementación del MFIS
- Fuzzificación de variables de entrada.  
- Evaluación de reglas con operadores lógicos difusos.  
- Agregación de resultados parciales.  
- Defuzzificación para obtener un valor de riesgo final.  

### Procesamiento de solicitudes reales
- Entrada: `Applications.txt` con datos de solicitantes.  
- Salida: `Results.txt` con nivel de riesgo calculado para cada solicitud.  

### Automatización y modularidad
- Lectura de variables, conjuntos y reglas desde ficheros externos (`InputVarSets.txt`, `Rules.txt`, `Risks.txt`).

## Tecnologías y herramientas utilizadas
- Python para el desarrollo del motor de inferencia.  
- NumPy para cálculos numéricos.  
- scikit-fuzzy (skfuzzy) para funciones de pertenencia y lógica difusa (sin usar el módulo control).  
- Clases y funciones propias para representar variables, reglas y resultados.  
- Procesamiento de ficheros externos (.txt) para definir variables, conjuntos borrosos, reglas y aplicaciones.  

