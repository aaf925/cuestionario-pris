import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Diccionario que contendrá todas las preguntas por tema
# Las preguntas se añaden directamente aquí en el código.
# Cada tema es una clave, y su valor es una lista de diccionarios de preguntas.

ALL_QUESTIONS = {
    "Tema 1: Metodologías de Desarrollo de Software": [
        {"question": "¿Qué modelo de desarrollo se caracteriza por tener fases bien definidas y no permitir retrocesos?", "options": ["Modelo en V", "Modelo Espiral", "Modelo en Cascada", "Modelo Iterativo"], "answer": "Modelo en Cascada", "type": "multiple_choice"},
        {"question": "En el modelo en V, ¿qué fase acompaña cada etapa de desarrollo?", "options": ["Implementación", "Pruebas", "Análisis de requisitos", "Mantenimiento"], "answer": "Pruebas", "type": "multiple_choice"},
        {"question": "¿Cuál es una característica fundamental de las metodologías ágiles?", "options": ["Documentación extensa", "Desarrollo incremental e iterativo", "Planificación rígida y detallada", "Uso exclusivo de diagramas UML"], "answer": "Desarrollo incremental e iterativo", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes NO es una metodología ágil?", "options": ["Scrum", "XP (Extreme Programming)", "Modelo en Cascada", "Kanban"], "answer": "Modelo en Cascada", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un principio clave de Scrum?", "options": ["Sprints iterativos", "Entregas solo al final del proyecto", "Desarrollo sin reuniones", "Se exige una práctica de desarrollo específica"], "answer": "Sprints iterativos", "type": "multiple_choice"},
        {"question": "¿Qué rol en Scrum es responsable de eliminar obstáculos y facilitar el proceso?", "options": ["Product Owner", "Scrum Master", "Jefe de Proyecto", "Desarrollador"], "answer": "Scrum Master", "type": "multiple_choice"},
        {"question": "¿Qué metodología ágil promueve la programación en pareja y pruebas automatizadas?", "options": ["Kanban", "Scrum", "XP (Extreme Programming)", "Modelo en V"], "answer": "XP (Extreme Programming)", "type": "multiple_choice"},
        {"question": "¿Cuál es una característica clave de los métodos híbridos como Scrumban?", "options": ["No permiten iteraciones", "Mezclan elementos de metodologías tradicionales y ágiles", "Solo se usan en proyectos pequeños", "No requieren planificación"], "answer": "Mezclan elementos de metodologías tradicionales y ágiles", "type": "multiple_choice"},
        {"question": "¿Qué marco de trabajo ágil es más utilizado en grandes organizaciones para escalar Agile?", "options": ["XP", "Scrum", "SAFe (Scaled Agile Framework)", "Kanban"], "answer": "SAFe (Scaled Agile Framework)", "type": "multiple_choice"},
        {"question": "En el ciclo de vida del software, ¿qué fase implica la verificación y validación del código?", "options": ["Diseño", "Implementación", "Pruebas", "Análisis de requisitos"], "answer": "Pruebas", "type": "multiple_choice"},
        {"question": "¿Cuál es la principal ventaja de utilizar metodologías ágiles?", "options": ["Reduce la necesidad de planificación", "Flexibilidad y adaptación a cambios", "Menos interacción con el cliente", "Desarrollo más lento pero más seguro"], "answer": "Flexibilidad y adaptación a cambios", "type": "multiple_choice"},
        {"question": "¿Qué enfoque de desarrollo mejora el producto en ciclos incrementales, adaptando el alcance en cada iteración?", "options": ["Predictivo", "Adaptativo", "Modelo en V", "Modelo en Cascada"], "answer": "Adaptativo", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un objetivo clave de las metodologías de desarrollo de software?", "options": ["Reducir la necesidad de pruebas", "Estandarizar el proceso de desarrollo y reducir errores", "Eliminar la fase de mantenimiento", "Desarrollar software sin documentación"], "answer": "Estandarizar el proceso de desarrollo y reducir errores", "type": "multiple_choice"},
        {"question": "¿Qué tipo de ciclo de vida se caracteriza por dividir el desarrollo en pequeñas partes funcionales entregables?", "options": ["Predictivo", "Cascada", "Incremental", "Modelo en V"], "answer": "Incremental", "type": "multiple_choice"},
        {"question": "¿Qué ventaja tiene el modelo en espiral respecto al modelo en cascada?", "options": ["Permite evaluar riesgos en cada iteración", "Es más rápido", "No necesita planificación", "No requiere pruebas"], "answer": "Permite evaluar riesgos en cada iteración", "type": "multiple_choice"},
        {"question": "¿Cuál es una de las funciones principales del Product Owner en Scrum?", "options": ["Escribir código", "Priorizar los requisitos del producto", "Gestionar el equipo de desarrollo", "Diseñar la interfaz de usuario"], "answer": "Priorizar los requisitos del producto", "type": "multiple_choice"},
        {"question": "¿Cómo se denomina la reunión diaria en Scrum donde el equipo sincroniza el trabajo?", "options": ["Daily Scrum", "Sprint Planning", "Sprint Retrospective", "Revisión del Sprint"], "answer": "Daily Scrum", "type": "multiple_choice"},
        {"question": "¿Qué ventaja tiene Kanban sobre Scrum?", "options": ["Utiliza reuniones diarias obligatorias", "No permite cambios en el flujo de trabajo", "No usa iteraciones fijas y permite flujo continuo", "Depende de la documentación extensa"], "answer": "No usa iteraciones fijas y permite flujo continuo", "type": "multiple_choice"},
        {"question": "¿Qué significa la retrospectiva en Scrum?", "options": ["Reunión para evaluar y mejorar el proceso", "Presentación del software al cliente", "Revisión del código fuente", "Análisis de riesgos"], "answer": "Reunión para evaluar y mejorar el proceso", "type": "multiple_choice"},
        {"question": "¿En qué metodología se utilizan tarjetas visuales para gestionar tareas y su progreso?", "options": ["Scrum", "XP", "Kanban", "Modelo en V"], "answer": "Kanban", "type": "multiple_choice"}
    ],
    "Tema 2: Calidad y Estándares de Software": [
        {"question": "¿Cuál de los siguientes NO es un factor clave en la calidad del software?", "options": ["Correctitud", "Mantenibilidad", "Inseguridad", "Eficiencia"], "answer": "Inseguridad", "type": "multiple_choice"},
        {"question": "Los estándares,", "options": ["Sólo se enfocan en aspectos técnicos.", "Se enfocan en aspectos técnicos y en ética profesional y responsabilidad social.", "Se enfocan en ética profesional y responsabilidad social pero no en aspectos técnicos.", "Se enfocan en aspectos técnicos y en ética profesional solamente."], "answer": "Se enfocan en aspectos técnicos y en ética profesional y responsabilidad social.", "type": "multiple_choice"},
        {"question": "Documentar errores y fallos de manera honesta es un principio de la ética en el software:", "options": ["Verdadero", "Falso"], "answer": "Verdadero", "type": "multiple_choice"},
        {"question": "El ISO 9000,", "options": ["Establece los principios fundamentales para la gestión de la calidad en las organizaciones.", "Establece un marco para gestionar y controlar la calidad en el ciclo de vida del desarrollo.", "Es una norma diseñada para ayudar a las organizaciones a mejorar su eficiencia y sostenibilidad a largo plazo.", "Estándar internacional para la evaluación de la calidad del software."], "answer": "Establece los principios fundamentales para la gestión de la calidad en las organizaciones.", "type": "multiple_choice"},
        {"question": "Las características de la ISO 25000 son", "options": ["Funcionalidad, usabilidad, fiabilidad, eficiencia, mantenibilidad, seguridad, portabilidad y compatibilidad .", "Funcionalidad, fiabilidad, seguridad y mantenibilidad.", "Funcionalidad, usabilidad, fiabilidad, eficiencia, mantenibilidad, seguridad, portabilidad, compatibilidad y liderazgo.", "Enfoque del cliente, liderazgo, compromiso del personal, enfoque por procesos, mejora continua y toma de decisiones basada en evidencias."], "answer": "Funcionalidad, usabilidad, fiabilidad, eficiencia, mantenibilidad, seguridad, portabilidad y compatibilidad .", "type": "multiple_choice"},
        {"question": "¿Qué es un estándar de calidad de software?", "options": ["Un conjunto de reglas para evaluar y mejorar la calidad del software.", "Un tipo de software de código abierto.", "Un modelo de negocio para la industria del software.", "Un programa de seguridad informática."], "answer": "Un conjunto de reglas para evaluar y mejorar la calidad del software.", "type": "multiple_choice"},
        {"question": "¿Qué tipo de prueba se realiza sin ejecutar el código?", "options": ["Pruebas estáticas", "Pruebas dinámicas", "Pruebas de carga", "Pruebas de estrés"], "answer": "Pruebas estáticas", "type": "multiple_choice"},
        {"question": "¿Cuál es el propósito principal de un SQA (Software Quality Assurance)?", "options": ["Crear bases de datos seguras.", "Escribir código sin errores.", "Garantizar el cumplimiento de metodologías de calidad.", "Reemplazar a los testers manuales."], "answer": "Garantizar el cumplimiento de metodologías de calidad.", "type": "multiple_choice"},
        {"question": "¿Cuáles son los fundamentos de SQC (Software Quality Control)?", "options": ["Detecta problemas en los productos de trabajo.", "Verifica que los productos de trabajo cumplan con los estándares de calidad especificados.", "Revisa el contenido del producto.", "Todas las anteriores son correctas."], "answer": "Todas las anteriores son correctas.", "type": "multiple_choice"},
        {"question": "Sobre la mejora continua de la calidad, señala la afirmación INCORRECTA.", "options": ["Estrategia iterativa para optimizar procesos y productos.", "Se basa en el ciclo PDCA (Plan-Do-Check-Act) y la gestión de calidad total (TQM).", "La retroalimentación constante de usuarios y desarrolladores ayuda a perfeccionar el software.", "Reduce el tiempo y los costos de mantenimiento"], "answer": "Reduce el tiempo y los costos de mantenimiento", "type": "multiple_choice"},
        {"question": "¿Qué es un proceso de auditoría en el desarrollo de software?", "options": ["Evaluación para verificar el cumplimiento de estándares.", "Escribir código más rápido.", "Reducir costos de desarrollo.", "Desarrollar software sin documentación."], "answer": "Evaluación para verificar el cumplimiento de estándares.", "type": "multiple_choice"},
        {"question": "La evaluación y verificación de la calidad del software garantizan que el producto cumple con los estándares establecidos y satisface las necesidades del usuario.", "options": ["Verdadero", "Falso"], "answer": "Verdadero", "type": "multiple_choice"},
        {"question": "Sobre la seguridad en software crítico, señala la afirmación CORRECTA.", "options": ["Se aplican pruebas de estrés y carga", "Un software seguro protege la integridad de los datos y la privacidad del usuario.", "El análisis de fallos permite mitigar errores y prevenir problemas futuros.", "Ninguna es correcta."], "answer": "Un software seguro protege la integridad de los datos y la privacidad del usuario.", "type": "multiple_choice"},
        {"question": "¿Cuál es la principal diferencia entre los métodos de evaluación de calidad estáticos y dinámicos?", "options": ["Los métodos estáticos requieren la ejecución del software, mientras que los dinámicos no.", "Los métodos dinámicos se aplican antes del desarrollo del software y los estáticos después.", "Los métodos estáticos no requieren la ejecución del software, mientras que los dinámicos sí.", "Ambos métodos requieren la ejecución del software, pero en diferentes entornos."], "answer": "Los métodos estáticos no requieren la ejecución del software, mientras que los dinámicos sí.", "type": "multiple_choice"},
        {"question": "¿Cuál de estas métricas NO se utiliza en estándares de calidad?", "options": ["Densidad de defectos", "Tiempo entre fallos", "Complejidad ciclomática", "Densidad ciclomática"], "answer": "Densidad ciclomática", "type": "multiple_choice"},
        {"question": "El análisis estático,", "options": ["Es fundamental para detectar errores en etapas tardías.", "Es fundamental para detectar errores en etapas tempranas.", "No permite identificar código ejecutable o redundante.", "Evalúa el comportamiento real del sistema bajo diferentes condiciones."], "answer": "Es fundamental para detectar errores en etapas tempranas.", "type": "multiple_choice"},
        {"question": "¿Cual de estas herramientas pertenece al análisis dinámico?", "options": ["Sonarqube", "ESLint", "Selenium", "Infer"], "answer": "Selenium", "type": "multiple_choice"},
        {"question": "¿Cual de estas no es una técnica de reducción de riesgos?", "options": ["Evitación de fallos.", "Análisis de rendimiento.", "Uso de modelos de aseguramiento.", "Limitación del daño causado por fallos."], "answer": "Análisis de rendimiento.", "type": "multiple_choice"},
        {"question": "La ISO 9001 permite a las empresas que desarrollan software conocer la calidad de sus productos.", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "multiple_choice"},
        {"question": "¿Cual de estas afirmaciones es correcta?", "options": ["La verificacion garantiza que el software cumple con los requisitos del usuario.", "Las verificación previene problemas de usabilidad y funcionalidad", "La verificación confirma que el desarrollo sigue las especificaciones técnicas.", "La verificación no detecta problemas antes de la entrega del producto."], "answer": "La verificación confirma que el desarrollo sigue las especificaciones técnicas.", "type": "multiple_choice"}
    ],
    "Tema 3: Métricas de calidad de proyectos software": [
        {"question": "¿Para qué sirven las métricas de calidad a lo largo del desarrollo de un proyecto?", "options": ["Únicamente para la fase final de pruebas.", "Solo para la comunicación con los usuarios finales.", "Para identificar áreas de mejora, establecer objetivos realistas y tomar decisiones informadas.", "Principalmente para la gestión de la infraestructura del servidor."], "answer": "Para identificar áreas de mejora, establecer objetivos realistas y tomar decisiones informadas.", "type": "multiple_choice"},
        {"question": "¿Qué se busca conseguir al analizar el problema antes de iniciar un proyecto de software?", "options": ["Definir el lenguaje de programación a utilizar.", "Entender qué se quiere hacer y qué se quiere conseguir para no afectar la calidad.", "Establecer el cronograma detallado de tareas.", "Asignar los roles y responsabilidades del equipo."], "answer": "Entender qué se quiere hacer y qué se quiere conseguir para no afectar la calidad.", "type": "multiple_choice"},
        {"question": "¿Desde qué perspectiva principal miden el software las métricas de función?", "options": ["La cantidad de líneas de código.", "La eficiencia del algoritmo.", "El rendimiento del servidor.", "La del usuario, en términos de tamaño, complejidad y funcionalidad."], "answer": "La del usuario, en términos de tamaño, complejidad y funcionalidad.", "type": "multiple_choice"},
        {"question": "¿Cuál es el propósito del factor de ajuste de complejidad en el cálculo de Puntos de Función?", "options": ["Simplificar el proceso de conteo de elementos funcionales.", "Reflejar mejor las características técnicas y operativas del software en el cálculo final.", "Asegurar que todos los proyectos tengan el mismo número de Puntos de Función.", "Eliminar la necesidad de contar los elementos funcionales individualmente."], "answer": "Reflejar mejor las características técnicas y operativas del software en el cálculo final.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un tipo de elemento funcional que se considera al calcular los Puntos de Función?", "options": ["Entradas Externas (EI).", "Líneas de código comentadas.", "Número de pruebas unitarias.", "Cantidad de diagramas UML."], "answer": "Entradas Externas (EI).", "type": "multiple_choice"},
        {"question": "¿Qué representan los Archivos Lógicos Internos (ILF) en el modelo de Puntos de Función?", "options": ["Datos que ingresan al sistema desde el exterior.", "Datos generados por el sistema y enviados al usuario.", "Conjuntos de datos almacenados dentro de la aplicación y mantenidos por el sistema.", "Archivos referenciados por la aplicación pero no mantenidos por ella."], "answer": "Conjuntos de datos almacenados dentro de la aplicación y mantenidos por el sistema.", "type": "multiple_choice"},
        {"question": "¿Qué indica un valor alto en la métrica \"Falta de Cohesión en Métodos (LCOM)\"?", "options": ["Que los métodos de la clase están bien relacionados.", "Que la clase realiza demasiadas tareas no relacionadas.", "Que la clase tiene una interfaz bien definida.", "Que la clase es altamente reutilizable."], "answer": "Que la clase realiza demasiadas tareas no relacionadas.", "type": "multiple_choice"},
        {"question": "¿A qué se refiere el concepto de \"acoplamiento\" en el diseño de clases?", "options": ["Qué tan bien los elementos dentro de una clase trabajan juntos.", "La cantidad de elementos y relaciones dentro del sistema.", "El contexto donde una clase puede operar.", "El grado de interdependencia entre dos sistemas o clases."], "answer": "El grado de interdependencia entre dos sistemas o clases.", "type": "multiple_choice"},
        {"question": "¿Qué evalúan las métricas de diseño de clases en el desarrollo de software orientado a objetos?", "options": ["La calidad de la estructura y las relaciones de las clases dentro de un sistema.", "El rendimiento de los métodos de las clases.", "La cantidad de documentación generada para cada clase.", "El número de pruebas unitarias escritas para cada clase."], "answer": "La calidad de la estructura y las relaciones de las clases dentro de un sistema.", "type": "multiple_choice"},
        {"question": "¿Qué mide la \"Complejidad Ciclomática del Caso de Uso (CC)\"?", "options": ["La cantidad total de actores involucrados en el caso de uso.", "La cantidad de caminos alternativos dentro del caso de uso.", "El porcentaje de acciones realizadas por el sistema.", "El número de casos de uso incluidos en el caso de uso principal."], "answer": "La cantidad de caminos alternativos dentro del caso de uso.", "type": "multiple_choice"},
        {"question": "¿Qué evalúan las métricas de casos de uso?", "options": ["La eficiencia del código generado a partir de los casos de uso.", "La calidad de la especificación de requisitos en un sistema orientado a objetos, centrada en la interacción usuario-sistema.", "El número de diagramas de secuencia creados para cada caso de uso.", "La complejidad técnica de la implementación de cada caso de uso."], "answer": "La calidad de la especificación de requisitos en un sistema orientado a objetos, centrada en la interacción usuario-sistema.", "type": "multiple_choice"},
        {"question": "¿Qué mide la métrica de \"trazabilidad\" en los requisitos de software?", "options": ["La longitud promedio de las frases en los requisitos.", "La frecuencia con la que se actualizan los requisitos.", "La capacidad de seguir un requisito a lo largo del ciclo de vida del software.", "El nivel de detalle técnico incluido en cada requisito."], "answer": "La capacidad de seguir un requisito a lo largo del ciclo de vida del software.", "type": "multiple_choice"},
        {"question": "¿Cuál es un beneficio esperado de mantener un bajo acoplamiento entre las clases en un sistema orientado a objetos?", "options": ["Mejora la modularidad y facilita la reutilización del código.", "Mayor dificultad para realizar cambios en el código.", "Menor modularidad y dificultad para la reutilización del código.", "Aumento de la complejidad en las pruebas unitarias"], "answer": "Mejora la modularidad y facilita la reutilización del código.", "type": "multiple_choice"},
        {"question": "¿Qué mide la métrica de diseño de clases \"Weighted Methods per Class (WMC)\"?", "options": ["La profundidad de la jerarquía de herencia.", "El número de subclases de una clase.", "El número de clases con las que una clase está acoplada.", "La complejidad de una clase sumando la complejidad de cada uno de sus métodos."], "answer": "La complejidad de una clase sumando la complejidad de cada uno de sus métodos.", "type": "multiple_choice"},
        {"question": "¿Qué distingue a una Salida Externa (EO) de una Consulta Externa (EQ) en el contexto de los Puntos de Función?", "options": ["La EO no involucra datos almacenados, mientras que la EQ sí.", "La EQ siempre modifica archivos internos, mientras que la EO no.", "La EO incluye cálculos, transformaciones o datos derivados, a diferencia de la EQ que solo muestra información sin procesamiento adicional.", "La EO es iniciada por un sistema externo, mientras que la EQ por el usuario."], "answer": "La EO incluye cálculos, transformaciones o datos derivados, a diferencia de la EQ que solo muestra información sin procesamiento adicional.", "type": "multiple_choice"},
        {"question": "¿Qué métrica de requisitos se centra en asegurar que cada requisito tenga una única interpretación técnica?", "options": ["Completitud.", "Consistencia.", "Corrección.", "Trazabilidad."], "answer": "Corrección.", "type": "multiple_choice"},
        {"question": "¿Qué indica un valor alto en la métrica de diseño de clases \"Coupling Between Object Classes (CBO)\"?", "options": ["Una alta dependencia entre clases, lo que dificulta la modificación y reutilización del código.", "Una alta cohesión entre los métodos de la clase.", "Una baja dependencia de la jerarquía de herencia.", "Una buena encapsulación de los atributos de la clase."], "answer": "Una alta dependencia entre clases, lo que dificulta la modificación y reutilización del código.", "type": "multiple_choice"},
        {"question": "¿Qué herramienta basada en PLN se menciona en el texto para medir la calidad de los requisitos, basándose en problemas comunes de redacción?", "options": ["ARM Tool de la NASA.", "Visure Quality Analyzer.", "IBM DOORS.", "Enterprise Architect."], "answer": "Visure Quality Analyzer.", "type": "multiple_choice"},
        {"question": "¿Cuál es el objetivo principal de las métricas de requisitos?", "options": ["Medir la velocidad de codificación de los programadores.", "Evaluar el rendimiento del software una vez implementado.", "Gestionar el presupuesto y el cronograma del proyecto", "Asegurar que los requisitos sean claros, completos, consistentes y trazables."], "answer": "Asegurar que los requisitos sean claros, completos, consistentes y trazables.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes factores se considera para ajustar la complejidad en el cálculo de Puntos de Función?", "options": ["La experiencia del analista de requisitos.", "El lenguaje de programación utilizado.", "Comunicación de Datos.", "El tamaño del equipo de pruebas."], "answer": "Comunicación de Datos.", "type": "multiple_choice"}
    ],
    "Tema 4: Refactorización": [
        {"question": "La refactorización consiste en modificar el código fuente para mejorar su estructura interna sin alterar su comportamiento externo.", "options": ["Verdadero", "Falso"], "answer": "Verdadero", "type": "true_false"},
        {"question": "El objetivo principal de la refactorización es corregir errores de funcionalidad en el código.", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "La refactorización es una práctica recomendada solo para proyectos grandes.", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "La refactorización mejora el rendimiento del código en todos los casos.", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "\"Feature Envy\" es un code smell qué ocurre cuando un método de una clase accede con demasiada frecuencia a los datos de otra clase.", "options": ["Verdadero", "Falso"], "answer": "Verdadero", "type": "true_false"},
        {"question": "¿Cuándo se debe realizar la refactorización en el desarrollo de software?", "options": ["Solo al final del ciclo de desarrollo.", "Únicamente cuando aparecen errores en producción", "De manera continua durante el desarrollo para mejorar la calidad del código.", "Solo cuando el equipo decida reescribir todo el código desde cero."], "answer": "De manera continua durante el desarrollo para mejorar la calidad del código.", "type": "multiple_choice"},
        {"question": "¿Qué son los bloaters en el contexto de la refactorización de código?", "options": ["Patrones de diseño que mejoran la eficiencia del código.", "Secciones de código que han crecido demasiado y afectan la mantenibilidad.", "Técnicas para aumentar el rendimiento de un programa.", "Herramientas automatizadas para detectar errores en el código."], "answer": "Secciones de código que han crecido demasiado y afectan la mantenibilidad.", "type": "multiple_choice"},
        {"question": "¿Por qué es importante acompañar la refactorización con pruebas?", "options": ["Porque ayuda a garantizar que la funcionalidad no se vea afectada.", "Porque reduce el tiempo de desarrollo sin importar los errores.", "Porque la refactorización siempre introduce nuevos errores.", "Porque evita la necesidad de documentar los cambios."], "answer": "Porque ayuda a garantizar que la funcionalidad no se vea afectada.", "type": "multiple_choice"},
        {"question": "¿Qué es un \"Code smell\" en el contexto de la refactorización?", "options": ["Un error de sintaxis en el código que puede resolverse con una técnica de refactorización.", "Una indicación de que el código puede tener problemas de diseño que requieren refactorización.", "Una característica nueva añadida al código que resulta contradictoria con los principios de la refactorización.", "Una herramienta para depurar el código en busca de casos para la aplicación de refactorización."], "answer": "Una indicación de que el código puede tener problemas de diseño que requieren refactorización.", "type": "multiple_choice"},
        {"question": "¿Qué técnica de refactorización se utiliza para mover una funcionalidad de una clase a otra más apropiada?", "options": ["Extract Class", "Move Method", "Inline Method", "Pull Up Method"], "answer": "Move Method", "type": "multiple_choice"},
        {"question": "¿Qué problema aborda la técnica \"Replace Magic Number with Symbolic Constant\"?", "options": ["El uso de números literales en el código que carecen de significado claro.", "La presencia de números complejos en el código.", "La utilización de constantes simbólicas en lugar de variables.", "El uso de números en comentarios del código."], "answer": "El uso de números literales en el código que carecen de significado claro.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes no es un code smell?", "options": ["Long Method", "Magic Numbers", "Single Parameter", "Feature Envy"], "answer": "Single Parameter", "type": "multiple_choice"},
        {"question": "¿Cuál es una ventaja de \"Inline Class\"?", "options": ["Simplifica el código al eliminar clases innecesarias.", "Hace que el código sea más modular.", "Duplica la lógica del programa en diferentes clases.", "Aumenta la dependencia entre clases."], "answer": "Simplifica el código al eliminar clases innecesarias.", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes afirmaciones sobre la refactorización es falsa?", "options": ["Mejora la legibilidad del código.", "Siempre aumenta el rendimiento del software.", "Puede hacer que el código sea menos flexible.", "Facilita el mantenimiento del código."], "answer": "Siempre aumenta el rendimiento del software.", "type": "multiple_choice"},
        {"question": "¿Cuál es un beneficio clave de la técnica \"Separate Query from Modifier\"?", "options": ["Evita efectos secundarios en consultas de datos.", "Permite cambiar el estado de los objetos más rápidamente.", "Reduce el número de clases en el código.", "Convierte todos los métodos en estáticos."], "answer": "Evita efectos secundarios en consultas de datos.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes NO es un motivo para refactorizar código?", "options": ["Mejorar la mantenibilidad del código.", "Facilitar la incorporación de nuevas funcionalidades.", "Asegurar que el código compile sin errores.", "Reducir la complejidad del código."], "answer": "Asegurar que el código compile sin errores.", "type": "multiple_choice"},
        {"question": "¿Qué técnica ayuda a eliminar código repetitivo en múltiples clases?", "options": ["Extract Interface", "Push Down Method", "Pull Up Method", "Replace Conditional with Polymorphism"], "answer": "Pull Up Method", "type": "multiple_choice"},
        {"question": "¿Cuál es el riesgo de \"Cambiar Valor a Referencia\" si no se maneja bien?", "options": ["Puede provocar efectos colaterales si los objetos referenciados se modifican inesperadamente.", "Genera más copias de datos en memoria, lo que puede hacer que el programa sea más lento.", "Hace que cada objeto sea completamente independiente, lo que puede causar redundancia de datos.", "Obliga a usar estructuras de datos ineficientes para representar objetos."], "answer": "Puede provocar efectos colaterales si los objetos referenciados se modifican inesperadamente.", "type": "multiple_choice"}
    ],
    "Tema 5: Patrones de Diseño": [
        {"question": "¿Qué es un patrón de diseño en software?", "options": ["Un lenguaje de programación", "Un conjunto de reglas de sintaxis", "Una herramienta de depuración", "Una solución estandarizada a problemas comunes en desarrollo de software"], "answer": "Una solución estandarizada a problemas comunes en desarrollo de software", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes NO es un beneficio de los patrones de diseño?", "options": ["Reutilización de soluciones", "Establecimiento de un vocabulario común", "Dependencia estricta de una tecnología específica", "Código más mantenible"], "answer": "Dependencia estricta de una tecnología específica", "type": "multiple_choice"},
        {"question": "¿Quiénes popularizaron los patrones de diseño en informática con el libro Design Patterns?", "options": ["Alan Turing", "Linus Torvalds", "Gang of Four (GoF)", "Donald Knuth"], "answer": "Gang of Four (GoF)", "type": "multiple_choice"},
        {"question": "¿Qué patrón de diseño se usa para garantizar que solo haya una única instancia de una clase?", "options": ["Factory Method", "Singleton", "Builder", "Prototype"], "answer": "Singleton", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes patrones se usa para construir objetos paso a paso?", "options": ["Singleton", "Factory Method", "Prototype", "Builder"], "answer": "Builder", "type": "multiple_choice"},
        {"question": "¿El patrón Abstract Factory permite...?", "options": ["Crear una única instancia de una clase", "Construir objetos paso a paso", "Producir familias de objetos relacionados sin especificar clases concretas", "Clonar objetos existentes"], "answer": "Producir familias de objetos relacionados sin especificar clases concretas", "type": "multiple_choice"},
        {"question": "¿Qué patrón permite a objetos con interfaces incompatibles trabajar juntos?", "options": ["Composite", "Adapter", "Proxy", "Facade"], "answer": "Adapter", "type": "multiple_choice"},
        {"question": "¿Cuál es la principal ventaja del patrón Facade?", "options": ["Proporciona una interfaz simplificada a un sistema complejo", "Minimiza el uso de memoria compartiendo objetos", "Controla el acceso a un objeto", "Desacopla una abstracción de su implementación"], "answer": "Proporciona una interfaz simplificada a un sistema complejo", "type": "multiple_choice"},
        {"question": "¿Cuál es el propósito principal del patrón Decorator?", "options": ["Separar el comportamiento de la lógica de negocio", "Mejorar la estructura de clases en jerarquías", "Añadir responsabilidades a un objeto en tiempo de ejecución sin modificar su código fuente", "Evitar la creación de instancias innecesarias"], "answer": "Añadir responsabilidades a un objeto en tiempo de ejecución sin modificar su código fuente", "type": "multiple_choice"},
        {"question": "¿Qué patrón se usa para estructurar objetos en jerarquías tipo árbol?", "options": ["Composite", "Proxy", "Decorator", "Flyweight"], "answer": "Composite", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes patrones se usa para encapsular una solicitud como un objeto?", "options": ["Command", "Observer", "State", "Mediator"], "answer": "Command", "type": "multiple_choice"},
        {"question": "¿Qué patrón define una dependencia uno-a-muchos entre objetos, notificando cambios automáticamente?", "options": ["Strategy", "Memento", "Observer", "Chain of Responsibility"], "answer": "Observer", "type": "multiple_choice"},
        {"question": "¿Cuál es el propósito del patrón State?", "options": ["Controlar el acceso a un objeto", "Permitir que un objeto cambie su comportamiento cuando cambia su estado interno", "Separar la creación de objetos en pasos", "Coordinar la comunicación entre múltiples objetos"], "answer": "Permitir que un objeto cambie su comportamiento cuando cambia su estado interno", "type": "multiple_choice"},
        {"question": "¿Cuál es la principal función del patrón Strategy?", "options": ["Controlar el ciclo de vida de un objeto", "Crear objetos a partir de prototipos", "Definir una familia de algoritmos intercambiables", "Administrar la memoria en objetos reutilizados"], "answer": "Definir una familia de algoritmos intercambiables", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes patrones se usa para permitir que varios objetos manejen una solicitud sin que el emisor conozca cuál la procesará?", "options": ["Chain of Responsibility", "Mediator", "Command", "Memento"], "answer": "Chain of Responsibility", "type": "multiple_choice"},
        {"question": "¿Qué patrón permite guardar y restaurar el estado de un objeto sin afectar su encapsulación?", "options": ["Proxy", "Observer", "Strategy", "Memento"], "answer": "Memento", "type": "multiple_choice"},
        {"question": "¿Cuál es una buena práctica al aplicar patrones de diseño?", "options": ["Usarlos en cualquier parte del código sin análisis previo", "Reemplazar todas las estructuras existentes con patrones", "Comprender el problema antes de aplicar un patrón", "Evitar la reutilización de patrones en proyectos distintos"], "answer": "Comprender el problema antes de aplicar un patrón", "type": "multiple_choice"},
        {"question": "¿Cuál es un error común al usar patrones de diseño?", "options": ["No seguir el principio de abierto/cerrado", "Usar patrones innecesarios que aumentan la complejidad del código", "No encapsular objetos correctamente", "No aplicar la herencia en todos los casos"], "answer": "Usar patrones innecesarios que aumentan la complejidad del código", "type": "multiple_choice"},
        {"question": "¿En qué situaciones es ideal aplicar el patrón Visitor?", "options": ["Cuando se necesita una única instancia de una clase", "Cuando se quiere añadir nuevas operaciones a una jerarquía sin modificar sus clases", "Cuando se requiere recorrer una colección sin exponer su estructura interna", "Cuando se quiere crear un objeto de manera eficiente"], "answer": "Cuando se quiere añadir nuevas operaciones a una jerarquía sin modificar sus clases", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un patrón de diseño creacional?", "options": ["Observer", "Prototype", "Decorator", "Chain of Responsibility"], "answer": "Prototype", "type": "multiple_choice"}
    ],
    "Tema 6: Desarrollo Basado en Pruebas (TDD)": [
        {"question": "¿Cuál es el enfoque principal del Desarrollo Basado en Pruebas (TDD)?", "options": ["Escribir el código primero y luego las pruebas.", "Escribir las pruebas automatizadas antes del código.", "Escribir pruebas manuales después de la implementación.", "No escribir pruebas hasta la fase de integración."], "answer": "Escribir las pruebas automatizadas antes del código.", "type": "multiple_choice"},
        {"question": "¿Cuál es el primer paso del ciclo de TDD?", "options": ["Escribir la prueba (Red).", "Escribir el código mínimo (Green).", "Refactorización (Refactor).", "Ejecutar todas las pruebas."], "answer": "Escribir la prueba (Red).", "type": "multiple_choice"},
        {"question": "¿Qué se espera que suceda inicialmente al ejecutar una prueba en el ciclo de TDD?", "options": ["La prueba debe pasar inmediatamente.", "La prueba debe fallar, confirmando que la funcionalidad aún no está implementada.", "La prueba debe generar un error de compilación.", "La prueba debe quedar en un estado pendiente."], "answer": "La prueba debe fallar, confirmando que la funcionalidad aún no está implementada.", "type": "multiple_choice"},
        {"question": "¿Cuál es el objetivo principal del paso (\"Green\") del ciclo de TDD?", "options": ["Escribir código completo y optimizado.", "Documentar exhaustivamente la funcionalidad.", "Escribir el código justo y solamente lo necesario para que la prueba pase.", "Realizar pruebas de integración con otros módulos."], "answer": "Escribir el código justo y solamente lo necesario para que la prueba pase.", "type": "multiple_choice"},
        {"question": "En el contexto de TDD, ¿cuál es la distinción fundamental entre un \"mock\" y un \"stub\" al trabajar con dependencias de un componente bajo prueba?", "options": ["Un \"stub\" se utiliza para simular el comportamiento de un objeto devolviendo salidas predefinidas, mientras que un \"mock\" se centra en verificar que se hayan producido interacciones específicas con ese objeto.", "Un \"mock\" es una implementación simplificada de una dependencia con cierta lógica, mientras que un \"stub\" es un objeto que solo se utiliza para cumplir con la firma de un método sin funcionalidad real.", "Tanto los \"mocks\" como los \"stubs\" se utilizan para aislar el código bajo prueba, pero los \"mocks\" son más adecuados para probar unidades pequeñas y los \"stubs\" para probar integraciones entre componentes.", "Los \"stubs\" son más complejos de implementar ya que requieren definir un comportamiento específico, mientras que los \"mocks\" son objetos genéricos que registran interacciones."], "answer": "Un \"stub\" se utiliza para simular el comportamiento de un objeto devolviendo salidas predefinidas, mientras que un \"mock\" se centra en verificar que se hayan producido interacciones específicas con ese objeto.", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes es una ventaja principal de utilizar TDD?", "options": ["Aumenta el tiempo inicial de desarrollo significativamente.", "Genera una documentación extensa que siempre está desactualizada.", "Dificulta la refactorización del código existente.", "Detección Temprana de Errores."], "answer": "Detección Temprana de Errores.", "type": "multiple_choice"},
        {"question": "¿Cómo actúan las pruebas automatizadas creadas con TDD?", "options": ["Como una guía para los testers manuales.", "Como una documentación preliminar del sistema.", "Como una documentación viva que describe el comportamiento esperado del sistema.", "Como un registro de los errores encontrados en el pasado."], "answer": "Como una documentación viva que describe el comportamiento esperado del sistema.", "type": "multiple_choice"},
        {"question": "¿Cómo fomenta TDD la creación de código?", "options": ["Con clases grandes y altamente acopladas.", "Más limpio y modular, con componentes pequeños y bien definidos.", "Con una gran cantidad de lógica compleja desde el inicio.", "Con un diseño rígido y difícil de modificar."], "answer": "Más limpio y modular, con componentes pequeños y bien definidos.", "type": "multiple_choice"},
        {"question": "¿Qué se requiere para adoptar TDD de manera efectiva?", "options": ["Formar al equipo en buenas prácticas de escritura de pruebas y aceptar que el tiempo invertido en la fase inicial se traduce en menos tiempo dedicado a la depuración en el futuro.", "Escribir la mayor cantidad de pruebas posible sin importar su calidad.", "Enfocarse en probar solo las funcionalidades más críticas al final del desarrollo.", "No modificar las pruebas una vez que han sido escritas."], "answer": "Formar al equipo en buenas prácticas de escritura de pruebas y aceptar que el tiempo invertido en la fase inicial se traduce en menos tiempo dedicado a la depuración en el futuro.", "type": "multiple_choice"},
        {"question": "¿Con qué metodologías ágiles encaja perfectamente TDD?", "options": ["TDD no se relaciona directamente con metodologías ágiles.", "Metodologías con una planificación exhaustiva a largo plazo.", "Metodologías que priorizan la documentación detallada antes de la codificación.", "Aquellas basadas en iteraciones rápidas y entregas continuas de software funcional."], "answer": "Aquellas basadas en iteraciones rápidas y entregas continuas de software funcional.", "type": "multiple_choice"},
        {"question": "¿Qué impacto tiene TDD en la calidad del software?", "options": ["Mejora la calidad al detectar errores de forma temprana y reducir el tiempo dedicado a depurar.", "Disminuye la calidad al enfocar el esfuerzo en las pruebas en lugar del código funcional.", "No tiene un impacto significativo en la calidad del software.", "La calidad depende completamente de la experiencia del desarrollador, independientemente de la metodología."], "answer": "Mejora la calidad al detectar errores de forma temprana y reducir el tiempo dedicado a depurar.", "type": "multiple_choice"},
        {"question": "¿Qué diferencia principal existe entre TDD y las Pruebas Tradicionales?", "options": ["En TDD las pruebas son manuales y en las tradicionales son automatizadas.", "En las pruebas tradicionales se escriben pruebas unitarias y en TDD no.", "Primero las pruebas, luego el código en TDD, mientras que en las tradicionales es primero el código, luego las pruebas.", "Primero las pruebas, luego el código según las pruebas tradicionales, mientras que en TDD es primero el código, luego las pruebas."], "answer": "Primero las pruebas, luego el código en TDD, mientras que en las tradicionales es primero el código, luego las pruebas.", "type": "multiple_choice"},
        {"question": "¿Cómo se alinea TDD con el proceso de diseño de software en un contexto ágil?", "options": ["Traduciendo criterios de aceptación simples en pruebas unitarias y repitiendo el ciclo hasta completar la aplicación.", "Definiendo toda la arquitectura del sistema antes de escribir cualquier prueba.", "Centrándose en la implementación del código y dejando las pruebas para el final de cada iteración.", "No existe una alineación específica entre TDD y el diseño ágil de software."], "answer": "Traduciendo criterios de aceptación simples en pruebas unitarias y repitiendo el ciclo hasta completar la aplicación.", "type": "multiple_choice"},
        {"question": "Dentro de los patrones de implementación de TDD se encuentra 'Fake it 'til you make it'. ¿En qué consiste este patrón de implementación?", "options": ["Este patrón se refiere a la idea de comenzar con una implementación mínima y luego ir mejorándola poco a poco, usando sustitutos temporales para partes del código que aún no están listas.", "Este patrón implica realizar una implementación completamente funcional desde el principio, sin importar que algunas partes del sistema aún no estén definidas.", "Este patrón se refiere a la creación de pruebas que se basan solo en datos estáticos sin necesidad de implementar el código real, y se evita escribir pruebas hasta tener la implementación completa.", "Este patrón sugiere que las pruebas deben escribir un código completamente detallado, sin necesidad de crear implementaciones mínimas para las pruebas."], "answer": "Este patrón se refiere a la idea de comenzar con una implementación mínima y luego ir mejorándola poco a poco, usando sustitutos temporales para partes del código que aún no están listas.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un principio de diseño de software relacionado con TDD?", "options": ["Alto acoplamiento entre componentes.", "Código complejo para abarcar todas las posibles funcionalidades futuras.", "El código debe funcionar, ser fácil de entender, tener mínima duplicación y ser lo más simple posible.", "Clases con múltiples responsabilidades para evitar la fragmentación del código."], "answer": "El código debe funcionar, ser fácil de entender, tener mínima duplicación y ser lo más simple posible.", "type": "multiple_choice"},
        {"question": "¿Cuál es una buena práctica en TDD relacionada con el número de pruebas por regla de negocio?", "options": ["Escribir la menor cantidad de pruebas posible para ahorrar tiempo.", "Una prueba por cada regla de negocio.", "Escribir una prueba que cubra múltiples reglas de negocio para mayor eficiencia.", "No existe una recomendación específica sobre el número de pruebas por regla de negocio."], "answer": "Una prueba por cada regla de negocio.", "type": "multiple_choice"},
        {"question": "¿Cuál es el propósito principal de utilizar \"dobles de prueba\" en TDD?", "options": ["Aumentar la complejidad de las pruebas para simular escenarios más realistas.", "Probar la comunicación entre diferentes módulos del sistema en un entorno controlado.", "Simular colaboraciones entre objetos y facilitar el aislamiento del código a probar.", "Generar automáticamente una gran cantidad de casos de prueba para aumentar la cobertura."], "answer": "Simular colaboraciones entre objetos y facilitar el aislamiento del código a probar.", "type": "multiple_choice"},
        {"question": "¿Cómo contribuye TDD a la Integración Continua (CI) y la Entrega Continua (CD)?", "options": ["Al contar con un amplio conjunto de pruebas automatizadas que permiten detectar errores de integración de forma temprana y asegurar que el sistema sigue funcionando tras cada cambio.", "Al eliminar la necesidad de realizar pruebas de integración manuales en un entorno de CI/CD.", "Al simplificar el proceso de despliegue al garantizar que solo se entrega código probado manualmente.", "TDD no tiene una relación directa con las prácticas de Integración y Entrega Continua."], "answer": "Al contar con un amplio conjunto de pruebas automatizadas que permiten detectar errores de integración de forma temprana y asegurar que el sistema sigue funcionando tras cada cambio.", "type": "multiple_choice"},
        {"question": "¿Qué se sugiere como una estrategia para trabajar con código legado sin pruebas al adoptar TDD?", "options": ["Reemplazar todo el código existente con una nueva implementación basada en pruebas desde el inicio.", "Ignorar el código legado y enfocarse únicamente en aplicar TDD al nuevo código que se desarrolle.", "Identificar el punto de cambio, localizar puntos de inflexión y añadir cualquier tipo de prueba para empezar a tener cierta cobertura.", "Documentar exhaustivamente todo el código legado antes de intentar escribir cualquier prueba."], "answer": "Identificar el punto de cambio, localizar puntos de inflexión y añadir cualquier tipo de prueba para empezar a tener cierta cobertura.", "type": "multiple_choice"},
        {"question": "¿Qué se recomienda para adoptar TDD con éxito?", "options": ["Enfocarse en lograr una cobertura de pruebas del 100% desde las primeras etapas del proyecto.", "Escribir la mayor cantidad de código funcional posible antes de comenzar a escribir las pruebas.", "Delegar la responsabilidad de escribir las pruebas a un equipo de QA independiente.", "Practicar continuamente, hacer de TDD el comportamiento por defecto y no escribir código sin una prueba que lo necesite."], "answer": "Practicar continuamente, hacer de TDD el comportamiento por defecto y no escribir código sin una prueba que lo necesite.", "type": "multiple_choice"}
    ],
      "Tema 7: Documentación de Software": [
        {"question": "¿Por qué es importante escribir documentación en un proyecto software?", "options": ["Para reemplazar la necesidad de escribir buen código", "Para facilitar la incorporación de nuevos miembros al equipo", "Para llevar un control del trabajo del equipo de desarrollo", "Para evitar el uso de control de versiones"], "answer": "Para facilitar la incorporación de nuevos miembros al equipo", "type": "multiple_choice"},
        {"question": "¿Qué documento recoge los requisitos funcionales y no funcionales de un sistema?", "options": ["BRD", "ERS", "Manual de usuario", "Guía de estilos"], "answer": "ERS", "type": "multiple_choice"},
        {"question": "¿Cuál es el estándar principal para documentar pruebas de software?", "options": ["ISO/IEC 15289", "IEEE 829", "UML", "Guía de documentación de Google"], "answer": "IEEE 829", "type": "multiple_choice"},
        {"question": "¿Qué herramienta permite generar automáticamente documentación de la estructura de una API?", "options": ["Swagger", "Doxygen", "UML", "AsciiDoc"], "answer": "Swagger", "type": "multiple_choice"},
        {"question": "¿Qué ocurre si la documentación se queda desactualizada?", "options": ["Mejora la calidad del código", "Incrementa la velocidad del desarrollo", "Genera confusión y errores", "No pasa nada"], "answer": "Genera confusión y errores", "type": "multiple_choice"},
        {"question": "¿Qué estándar define todos los documentos necesarios a lo largo del ciclo de vida del software?", "options": ["IEEE 830", "ISO/IEC 15289", "IEEE 831", "IEEE 829"], "answer": "ISO/IEC 15289", "type": "multiple_choice"},
        {"question": "¿Qué herramienta es más comúnmente usada en proyectos Python para documentar?", "options": ["JavaDoc", "Docusaurus", "Sphinx", "MkDocs"], "answer": "Sphinx", "type": "multiple_choice"},
        {"question": "¿Qué representa un wireframe?", "options": ["El diseño gráfico final", "La estructura base de la interfaz de usuario", "El comportamiento backend", "El flujo de las pruebas unitarias"], "answer": "La estructura base de la interfaz de usuario", "type": "multiple_choice"},
        {"question": "¿Qué característica deben tener los comentarios en el código?", "options": ["Ser largos y explicativos", "Ser breves, claros y precisos", "Específicos para clases abstractas", "Solo necesarios en código de prueba"], "answer": "Ser breves, claros y precisos", "type": "multiple_choice"},
        {"question": "¿Qué debe incluir un plan de pruebas?", "options": ["Capturas de pantalla", "Estrategia, herramientas y criterios de aceptación", "Listado de bugs", "Listado de riesgos"], "answer": "Estrategia, herramientas y criterios de aceptación", "type": "multiple_choice"},
        {"question": "¿Qué contiene una historia de usuario?", "options": ["Solo requisitos técnicos", "Rol, acción, motivo y criterio de aceptación", "Código fuente", "Requisitos funcionales y no funcionales"], "answer": "Rol, acción, motivo y criterio de aceptación", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes no es un lenguaje de marcado?", "options": ["AsciiDoc", "Markdown", "reStructuredText", "UML"], "answer": "UML", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes es una guía de estilo reconocida?", "options": ["PostgreSQL Style Guide", "Microsoft Writing Style Guide", "Manual de Selenium", "PyDoc Manual"], "answer": "Microsoft Writing Style Guide", "type": "multiple_choice"},
        {"question": "¿Cuál es el objetivo principal de un manual de usuario?", "options": ["Describir la arquitectura interna", "Enseñar al usuario cómo utilizar el software", "Listar los bugs del sistema", "Mostrar la implementación de la API"], "answer": "Enseñar al usuario cómo utilizar el software", "type": "multiple_choice"},
        {"question": "¿Qué herramienta permite documentar, probar y compartir APIs en entornos colaborativos?", "options": ["Swagger", "JavaDoc", "Postman", "Selenium"], "answer": "Postman", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes no es un diagrama UML?", "options": ["Diagrama de Clases", "Diagrama de Secuencia", "Diagrama de Requisitos", "Diagrama de Casos de Uso"], "answer": "Diagrama de Requisitos", "type": "multiple_choice"},
        {"question": "¿Para qué sirve un registro de errores?", "options": ["Desarrollar wireframes", "Documentar decisiones de diseño", "Registrar incidencias detectadas y soluciones aplicadas", "Mostrar el historial de versiones"], "answer": "Registrar incidencias detectadas y soluciones aplicadas", "type": "multiple_choice"},
        {"question": "¿Qué propone el modelo C4?", "options": ["Estandarizar casos de prueba", "Documentar arquitectura en distintos niveles de abstracción", "Medir rendimiento de aplicaciones", "Gestionar APIs externas"], "answer": "Documentar arquitectura en distintos niveles de abstracción", "type": "multiple_choice"},
        {"question": "¿Qué debe contener un caso de prueba?", "options": ["Solo el resultado esperado", "Diagrama de flujo de la prueba", "ID, descripción, precondiciones, entradas, pasos y resultados esperados", "Lista de errores históricos"], "answer": "ID, descripción, precondiciones, entradas, pasos y resultados esperados", "type": "multiple_choice"},
        {"question": "¿Cuál es un problema habitual en la documentación de software?", "options": ["Usar herramientas modernas", "Tener documentación desincronizada con el código fuente", "Generar documentación automática", "Demasiada documentación"], "answer": "Tener documentación desincronizada con el código fuente", "type": "multiple_choice"}
    ],
    "Tema 8: Contenerización de Aplicaciones": [
        {"question": "¿Qué es la contenerización de aplicaciones?", "options": ["Proceso de ejecutar software en la nube", "Virtualización completa de hardware", "Empaquetar aplicaciones y dependencias en contenedores", "Ejecutar múltiples sistemas operativos a la vez"], "answer": "Empaquetar aplicaciones y dependencias en contenedores", "type": "multiple_choice"},
        {"question": "¿Qué elemento es fundamental en un contenedor?", "options": ["Máquina virtual", "BIOS", "Imagen", "Kernel externo"], "answer": "Imagen", "type": "multiple_choice"},
        {"question": "¿Cuál es una ventaja clave de los contenedores?", "options": ["Uso eficiente de recursos", "Mayor peso que las máquinas virtuales", "Menor portabilidad", "Requieren más sistema operativo"], "answer": "Uso eficiente de recursos", "type": "multiple_choice"},
        {"question": "¿Qué diferencia a un contenedor de una VM?", "options": ["Los contenedores incluyen su propio kernel", "Las VMs no requieren hipervisor", "Los contenedores comparten el kernel del host", "Las VMs son más ligeras"], "answer": "Los contenedores comparten el kernel del host", "type": "multiple_choice"},
        {"question": "¿Qué herramienta es la más usada para contenerización?", "options": ["Docker", "VMware", "VirtualBox", "Git"], "answer": "Docker", "type": "multiple_choice"},
        {"question": "¿Qué es una imagen en Docker?", "options": ["Una foto del contenedor", "Una plantilla inmutable con todo lo necesario para correr una app", "Una copia del sistema operativo", "Un archivo de logs"], "answer": "Una plantilla inmutable con todo lo necesario para correr una app", "type": "multiple_choice"},
        {"question": "¿Qué comando lanza un contenedor desde una imagen en Docker?", "options": ["docker build", "docker ps", "docker run", "docker pull"], "answer": "docker run", "type": "multiple_choice"},
        {"question": "¿Qué son los namespaces en Linux?", "options": ["Aíslan recursos como procesos y redes en contenedores", "Sistemas de archivos", "Tipos de usuarios", "Conjuntos de puertos"], "answer": "Aíslan recursos como procesos y redes en contenedores", "type": "multiple_choice"},
        {"question": "¿Qué gestionan los cgroups?", "options": ["Usuarios y permisos", "Recursos como CPU, memoria y disco", "Versiones de kernel", "Redes"], "answer": "Recursos como CPU, memoria y disco", "type": "multiple_choice"},
        {"question": "¿Qué tipo de almacenamiento persiste tras eliminar un contenedor?", "options": ["Memoria RAM", "Volumen", "Bind Mount", "Cache"], "answer": "Volumen", "type": "multiple_choice"},
        {"question": "¿Qué tipo de red Docker aísla completamente al contenedor?", "options": ["None", "Host", "Overlay", "Bridge"], "answer": "None", "type": "multiple_choice"},
        {"question": "¿Qué permite Docker Compose?", "options": ["Definir múltiples servicios en un solo archivo", "Crear interfaces gráficas", "Compilar imágenes", "Acceder a la nube"], "answer": "Definir múltiples servicios en un solo archivo", "type": "multiple_choice"},
        {"question": "¿Qué ventaja tiene contenerizar microservicios?", "options": ["Monitoreo más complejo", "Escalabilidad y despliegue independiente", "Más dependencias", "Menor portabilidad"], "answer": "Escalabilidad y despliegue independiente", "type": "multiple_choice"},
        {"question": "¿Cuál es la diferencia entre imagen y contenedor?", "options": ["Ninguna, son sinónimos", "Imagen es la plantilla; contenedor es la instancia en ejecución", "Imagen contiene datos; contenedor no", "Contenedor es más grande que la imagen"], "answer": "Imagen es la plantilla; contenedor es la instancia en ejecución", "type": "multiple_choice"},
        {"question": "¿Qué comando se usa para ver contenedores en ejecución?", "options": ["docker run", "docker ps", "docker build", "docker exec"], "answer": "docker ps", "type": "multiple_choice"},
        {"question": "¿Qué gestor de contenedores no requiere daemon y es rootless?", "options": ["Docker", "Podman", "LXC", "VirtualBox"], "answer": "Podman", "type": "multiple_choice"},
        {"question": "¿Qué permite almacenar imágenes?", "options": ["Dockerfile", "Registro (registry)", "Volumen", "Kernel"], "answer": "Registro (registry)", "type": "multiple_choice"},
        {"question": "¿Qué es Containerd?", "options": ["Es una imagen de Docker", "Herramienta para debug", "Runtime ligero para ejecutar contenedores", "Interfaz gráfica de Docker"], "answer": "Runtime ligero para ejecutar contenedores", "type": "multiple_choice"},
        {"question": "¿Qué contiene un Dockerfile?", "options": ["Instrucciones para construir una imagen", "Datos de ejecución del contenedor", "Logs del sistema", "Información del sistema host"], "answer": "Instrucciones para construir una imagen", "type": "multiple_choice"},
        {"question": "¿Qué hace el comando docker pull?", "options": ["Inicia un contenedor", "Detiene una imagen", "Descarga una imagen del registro", "Ejecuta una red"], "answer": "Descarga una imagen del registro", "type": "multiple_choice"}
    ],
     "Tema 9: CI/CD y Despliegue Continuo": [
        {"question": "El despliegue continuo es", "options": ["una estrategia de desarrollo en la que los cambios de código de la aplicación se publican automáticamente al entorno de producción tras pasar una serie de pruebas predefinidas.", "una técnica de diseño gráfico que permite optimizar la resolución de las imágenes antes del despliegue del sitio web.", "un proceso manual en el que los desarrolladores publican actualizaciones solo después de completar todo el ciclo de desarrollo y aprobación por parte del equipo de marketing.", "una metodología de respaldo que almacena copias del código fuente cada vez que un desarrollador guarda un archivo."], "answer": "una estrategia de desarrollo en la que los cambios de código de la aplicación se publican automáticamente al entorno de producción tras pasar una serie de pruebas predefinidas.", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes herramientas se utiliza comúnmente para la integración continua y despliegue continuo (CI/CD)?", "options": ["MySQL.", "GitHub Actions.", "Bootstrap.", "Nginx."], "answer": "GitHub Actions.", "type": "multiple_choice"},
        {"question": "Señala la opción incorrecta:", "options": ["En la etapa de seguridad, en la etapa de compilación y pruebas, el código se convierte en ejecutable y se validan sus funcionalidades.", "DAST (Dynamic Application Security Testing) analiza la aplicación mientras está en ejecución.", "SAST (Static Application Security Testing) analiza el código sin ejecutarlo.", "Se deben usar credenciales en archivos de configuración."], "answer": "Se deben usar credenciales en archivos de configuración.", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes afirmaciones es una buena práctica del despliegue del continuo de aplicaciones?", "options": ["Uso de credenciales en archivos de configuración.", "No verificar cambios en código de terceros.", "Uso de repositorios privados con control de acceso."], "answer": "Uso de repositorios privados con control de acceso.", "type": "multiple_choice"},
        {"question": "El archivo de configuración de GitHub Actions suele tener extensión _.exe_.", "options": ["Verdadero.", "Falso (Se usa YAML, por ejemplo: .yml)."], "answer": "Falso (Se usa YAML, por ejemplo: .yml).", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes opciones es un beneficio de CI/CD seguro?", "options": ["Incrementa la cantidad de pruebas visuales que se deben realizar manualmente antes del lanzamiento.", "Aumenta el número de líneas de código escritas por el equipo cada día.", "Reducción de riesgos de ataques y fugas de datos.", "Mejora la calidad del diseño gráfico en la interfaz de usuario."], "answer": "Reducción de riesgos de ataques y fugas de datos.", "type": "multiple_choice"},
        {"question": "Un rollback es", "options": ["el proceso de realizar pruebas de seguridad adicionales en una nueva versión antes de lanzarla.", "el proceso de volver a una versión anterior de la aplicación cuando una actualización presenta problemas.", "la acción de compilar el código fuente para crear una nueva versión de la aplicación.", "el proceso de agregar nuevas funcionalidades a una aplicación sin necesidad de realizar pruebas"], "answer": "el proceso de volver a una versión anterior de la aplicación cuando una actualización presenta problemas.", "type": "multiple_choice"},
        {"question": "Con un Feature branching:", "options": ["Cada funcionalidad se desarrolla en una rama separada.", "Se trabaja directamente en la rama main para una implementación directa.", "Se crean pull request sin revisión previa.", "Se hace un commit and push en la rama main cada vez que se realiza un cambio."], "answer": "Cada funcionalidad se desarrolla en una rama separada.", "type": "multiple_choice"},
        {"question": "¿Qué significa CI en desarrollo de software?", "options": ["Código Interactivo.", "Comunicación Inmediata.", "Integración Continua.", "Instalación Controlada."], "answer": "Integración Continua.", "type": "multiple_choice"},
        {"question": "Github actions se utiliza para…", "options": ["la creación de bases de datos en la nube sin necesidad de configuración.", "el despliegue de páginas estáticas.", "la automatización de la integración de diseño gráfico en la aplicación.", "gestionar la documentación en producción."], "answer": "el despliegue de páginas estáticas.", "type": "multiple_choice"},
        {"question": "¿Qué es una pipeline?", "options": ["Un servidor.", "Una app móvil.", "Una serie de pasos automatizados.", "Un lenguaje de programación."], "answer": "Una serie de pasos automatizados.", "type": "multiple_choice"},
        {"question": "¿Cuál no es un beneficio del CI/CD seguro?", "options": ["Reducción de ataques y fugas de datos.", "Codigo más bonito.", "Mayor confianza en la estabilidad del código.", "Cumplimientos de normativas y estándares de calidad."], "answer": "Codigo más bonito.", "type": "multiple_choice"},
        {"question": "¿Por qué no se sube un archivo _node_modules_ a un repositorio común?", "options": ["Porque contiene archivos sensibles como contraseñas y claves de API.", "Es un archivo muy pesado.", "Porque no se puede acceder a él desde sistemas operativos diferentes a Linux.", "Porque se genera automáticamente."], "answer": "Es un archivo muy pesado.", "type": "multiple_choice"},
        {"question": "En un sistema centralizado…", "options": ["Cada persona guarda sus cambios.", "Todos los cambios se guardan en un único lugar, obligando a una conexión constante.", "Los cambios se almacenan en múltiples servidores dispersos para mayor seguridad y disponibilidad.", "Los cambios nunca están visibles para los usuarios."], "answer": "Todos los cambios se guardan en un único lugar, obligando a una conexión constante.", "type": "multiple_choice"},
        {"question": "¿Qué hace el comando _npm install_?", "options": ["Eliminar todas las dependencias de la aplicación.", "Limpiar el directorio.", "Instalar las dependencias indicadas en el package.json.", "Inicializar todas las variables de la aplicación."], "answer": "Instalar las dependencias indicadas en el package.json.", "type": "multiple_choice"},
        {"question": "Los pipelines en CI se ejecutan automáticamente tras detectar cambios.", "options": ["Verdadero.", "Falso."], "answer": "Verdadero.", "type": "multiple_choice"},
        {"question": "El Despliegue continuo y la entrega continua:", "options": ["son lo mismo.", "el despliegue continuo necesita interacción manual para publicar los cambios a producción y la entrega continua no.", "La entrega continua necesita interacción manual para publicar los cambios a producción y el despliegue continuo no.", "El despliegue continuo despliega los cambios a producción si se pasan unas pruebas, y la entrega continua verifica los cambios para poder integrarlos a la rama principal de un repositorio compartido."], "answer": "La entrega continua necesita interacción manual para publicar los cambios a producción y el despliegue continuo no.", "type": "multiple_choice"},
        {"question": "¿Cuál es un área crítica de seguridad?", "options": ["La interfaz gráfica.", "El código fuente, compilación, pruebas y despliegue.", "La estructura de la aplicación.", "Los estilos visuales de la aplicación."], "answer": "El código fuente, compilación, pruebas y despliegue.", "type": "multiple_choice"},
        {"question": "¿Github se utiliza para el control de versiones?", "options": ["Verdadero.", "Falso."], "answer": "Verdadero.", "type": "multiple_choice"},
        {"question": "¿Cuál no es una herramienta de CI/CD completa?", "options": ["Gitlab.", "Jenkins.", "Cloudfare.", "Travis CI."], "answer": "Cloudfare.", "type": "multiple_choice"}
    ],
    "Tema 10: Aspectos Legales y Éticos en el Desarrollo de Software": [
        {"question": "¿Cuál es el objetivo principal de los aspectos legales y éticos en el desarrollo de software?", "options": ["Aumentar los beneficios de las empresas de software.", "Proteger a los usuarios, la sociedad y la integridad profesional.", "Agilizar el proceso de desarrollo de software.", "Reducir los costes de producción del software."], "answer": "Proteger a los usuarios, la sociedad y la integridad profesional.", "type": "multiple_choice"},
        {"question": "¿Qué tipo de obligaciones imponen los aspectos legales en el desarrollo de software?", "options": ["Valores y principios morales.", "Obligaciones que impone la ley (como protección de datos).", "Decisiones responsables sin base legal.", "Normas establecidas por las empresas."], "answer": "Obligaciones que impone la ley (como protección de datos).", "type": "multiple_choice"},
        {"question": "¿Qué orientan los aspectos éticos en el desarrollo de software?", "options": ["El cumplimiento estricto de las leyes.", "Valores y principios que orientan las decisiones responsables.", "La maximización de la eficiencia técnica.", "Los requisitos del cliente sin considerar las consecuencias."], "answer": "Valores y principios que orientan las decisiones responsables.", "type": "multiple_choice"},
        {"question": "¿En qué áreas críticas interviene el software que requieren estándares éticos?", "options": ["Redes sociales y videojuegos.", "Salud, seguridad aérea, educación o finanzas.", "Diseño gráfico y marketing online.", "Comunicación personal y entretenimiento."], "answer": "Salud, seguridad aérea, educación o finanzas.", "type": "multiple_choice"},
        {"question": "¿Qué organizaciones se dieron cuenta de la urgencia de definir estándares éticos en los años noventa?", "options": ["Microsoft y Apple.", "IEEE Computer Society y la ACM.", "Google y Facebook.", "Amazon y Netflix."], "answer": "IEEE Computer Society y la ACM.", "type": "multiple_choice"},
        {"question": "¿Cómo se llama el código de ética resultado del trabajo conjunto de ACM e IEEE?", "options": ["Código de Buenas Prácticas de Software.", "Software Engineering Code of Ethics and Professional Practice.", "Estándares Legales del Desarrollo de Software.", "Guía Ética para Ingenieros Informáticos."], "answer": "Software Engineering Code of Ethics and Professional Practice.", "type": "multiple_choice"},
        {"question": "¿Qué organización adoptó y tradujo el código de la ACM/IEEE al contexto hispanohablante?", "options": ["IEEE España.", "ACM Latinoamérica.", "SISTEDES.", "ISO Software."], "answer": "SISTEDES.", "type": "multiple_choice"},
        {"question": "¿Qué tipo de retos éticos plantea la aparición de la inteligencia artificial?", "options": ["Retos relacionados únicamente con la velocidad de procesamiento.", "Retos puramente técnicos sin implicaciones sociales.", "Preguntas sobre la responsabilidad en errores y la garantía de no reproducción de sesgos.", "Desafíos centrados en la interfaz de usuario."], "answer": "Preguntas sobre la responsabilidad en errores y la garantía de no reproducción de sesgos.", "type": "multiple_choice"},
        {"question": "¿En cuántos principios éticos fundamentales está dividido el Código de Ética y Conducta Profesional de ACM (v5.2)?", "options": ["Seis.", "Siete.", "Ocho.", "Nueve."], "answer": "Ocho.", "type": "multiple_choice"},
        {"question": "¿Cuál es el eje principal del Código de Ética y Conducta Profesional de ACM?", "options": ["La eficiencia en el desarrollo de software.", "La satisfacción del cliente.", "El interés público.", "El beneficio económico de la empresa."], "answer": "El interés público.", "type": "multiple_choice"},
        {"question": "¿Qué enfatiza el código ético de SISTEDES además de los principios generales?", "options": ["La rapidez en la entrega de proyectos.", "El uso exclusivo de tecnologías patentadas.", "La educación ética y el uso de ejemplos reales.", "La minimización de la documentación técnica."], "answer": "La educación ética y el uso de ejemplos reales.", "type": "multiple_choice"},
        {"question": "¿Cuál es uno de los principales propósitos de un código de ética como el de ACM/IEEE o SISTEDES?", "options": ["Facilitar la competencia desleal entre empresas.", "Proteger al público y al usuario frente a posibles daños.", "Limitar la innovación en el desarrollo de software.", "Favorecer los intereses empresariales por encima de todo."], "answer": "Proteger al público y al usuario frente a posibles daños.", "type": "multiple_choice"},
        {"question": "¿Qué principio ético universal destaca la importancia de proteger la seguridad, la salud y el bienestar social?", "options": ["Honestidad y veracidad.", "Interés público.", "Minimización de riesgos.", "Protección de derechos fundamentales."], "answer": "Interés público.", "type": "multiple_choice"},
        {"question": "¿Qué exige el principio de no maleficencia en el desarrollo de software?", "options": ["Maximizar los beneficios económicos a toda costa.", "Diseñar y mantener software seguro y libre de fallos graves.", "Ignorar las posibles consecuencias negativas del software.", "Entregar el software lo más rápido posible sin pruebas exhaustivas."], "answer": "Diseñar y mantener software seguro y libre de fallos graves.", "type": "multiple_choice"},
        {"question": "¿Qué implica la responsabilidad profesional en el ejercicio de la profesión del software?", "options": ["Actuar únicamente según las directrices de la empresa.", "Ignorar las normas éticas y legales si dificultan el trabajo.", "Actuar conforme a normas éticas y legales, y reconocer limitaciones personales.", "Ocultar los fallos de seguridad para evitar problemas."], "answer": "Actuar conforme a normas éticas y legales, y reconocer limitaciones personales.", "type": "multiple_choice"},
        {"question": "En el caso de Occidental Engineering, ¿qué problema técnico crítico se descubrió en el prototipo Safe Skies?", "options": ["Problemas de interfaz de usuario.", "Un fallo donde un avión podía desaparecer del sistema cuando había demasiados.", "Lentitud en el procesamiento de datos.", "Incompatibilidad con sistemas operativos."], "answer": "Un fallo donde un avión podía desaparecer del sistema cuando había demasiados.", "type": "multiple_choice"},
        {"question": "En el caso de subcontratación en Lesak, ¿qué parentesco tenía la vicepresidenta de MBE Design Group con el dueño de Lesak?", "options": ["Era su esposa.", "Era su hermana.", "Era su hija.", "Era su prima."], "answer": "Era su hija.", "type": "multiple_choice"},
        {"question": "¿Qué tecnología permitía el sistema TTWI (Through-the-Wall Imaging) en el Caso 3?", "options": ["Escuchar conversaciones a través de paredes.", "Ver a través de paredes usando radar de impulsos.", "Desactivar sistemas electrónicos a distancia.", "Camuflar objetos haciéndolos invisibles."], "answer": "Ver a través de paredes usando radar de impulsos.", "type": "multiple_choice"},
        {"question": "Según el Principio 1.3 del Código ACM, ¿qué se debe proporcionar sobre las capacidades, limitaciones y riesgos del software?", "options": ["Información técnica detallada solo para expertos.", "Información completa de manera honesta y confiable.", "Información mínima para no alarmar a los usuarios.", "Información optimista exagerando las funcionalidades."], "answer": "Información completa de manera honesta y confiable.", "type": "multiple_choice"},
        {"question": "¿Qué busca el enfoque \"ethical by design\" en el desarrollo de software?", "options": ["Añadir consideraciones éticas al final del proyecto.", "Integrar principios éticos en cada etapa del desarrollo desde el diseño.", "Externalizar la responsabilidad ética a un equipo especializado.", "Cumplir con los requisitos funcionales sin considerar la ética."], "answer": "Integrar principios éticos en cada etapa del desarrollo desde el diseño.", "type": "multiple_choice"}
    ],
    "Tema 11: Securización de aplicaciones web": [
        {"question": "¿Cuál de los siguientes es un pilar del modelo CIA en seguridad?", "options": ["Compatibilidad", "Integridad", "Accesibilidad", "Escalabilidad"], "answer": "Integridad", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes es un ejemplo de autenticación multifactor?", "options": ["Contraseña compleja", "SMS con código", "Nombre de usuario", "Captcha"], "answer": "SMS con código", "type": "multiple_choice"},
        {"question": "Verdadero o falso: \"Las cookies HttpOnly pueden ser accedidas mediante JavaScript en el navegador.\"", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "Verdadero o falso: \"El uso de eval() en JavaScript es una buena práctica de seguridad.\"", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "¿Qué herramienta permite la autenticación sin contraseña usando biometría?", "options": ["OAuth", "WebAuthn", "LDAP", "JWT"], "answer": "WebAuthn", "type": "multiple_choice"},
        {"question": "¿Qué cabecera permite controlar los orígenes permitidos en CORS?", "options": ["Access-Control-Allow-Origin", "Referrer-Policy", "Content-Type", "X-CORS-Token"], "answer": "Access-Control-Allow-Origin", "type": "multiple_choice"},
        {"question": "¿Qué opción describe mejor el concepto de \"Confianza cero\"?", "options": ["Permitir acceso local", "Validar solo usuarios externos", "Verificar siempre, sin asumir confianza", "Depender del firewall"], "answer": "Verificar siempre, sin asumir confianza", "type": "multiple_choice"},
        {"question": "¿Cuál de estos no es parte de un JSON Web Token (JWT)?", "options": ["Header", "Payload", "Footer", "Signature"], "answer": "Footer", "type": "multiple_choice"},
        {"question": "¿Qué herramienta analiza código sin ejecutarlo (SAST)?", "options": ["Burp Suite", "ZAP", "SonarQube", "Nmap"], "answer": "SonarQube", "type": "multiple_choice"},
        {"question": "¿Qué mecanismo evita el almacenamiento de secretos en código?", "options": ["SAST", "Vault", "HSTS", "CSRF"], "answer": "Vault", "type": "multiple_choice"},
        {"question": "¿Cuál es el objetivo del principio de mínimo privilegio?", "options": ["Proporcionar máximo acceso", "Compartir credenciales", "Restringir el acceso solo a lo necesario", "Mantener sesiones activas"], "answer": "Restringir el acceso solo a lo necesario", "type": "multiple_choice"},
        {"question": "¿Qué vulnerabilidad se caracteriza por inyectar scripts maliciosos en el navegador?", "options": ["CSRF", "XSS", "Broken Access Control", "SSRF"], "answer": "XSS", "type": "multiple_choice"},
        {"question": "¿Cuál es una práctica recomendada para manejar tokens de acceso?", "options": ["Almacenarlos en localStorage", "No cifrarlos", "Usar HTTPS y expiración corta", "Compartir por URL"], "answer": "Usar HTTPS y expiración corta", "type": "multiple_choice"},
        {"question": "¿Qué protocolo proporciona autenticación y autorización federada?", "options": ["JWT", "OAuth + OpenID Connect", "API Key", "TLS"], "answer": "OAuth + OpenID Connect", "type": "multiple_choice"},
        {"question": "¿Qué opción representa una medida de seguridad para el frontend?", "options": ["Uso de innerHTML", "Cookies sin restricciones", "Uso de CSP y headers de seguridad", "Permitir scripts externos sin control"], "answer": "Uso de CSP y headers de seguridad", "type": "multiple_choice"},
        {"question": "¿Qué es un ataque de relleno de credenciales?", "options": ["Inyección de SQL", "Uso de contraseñas robadas en múltiples sitios", "Suplantación de IP", "Sobrecarga del servidor"], "answer": "Uso de contraseñas robadas en múltiples sitios", "type": "multiple_choice"},
        {"question": "¿Qué tipo de prueba permite descubrir rutas y parámetros ocultos?", "options": ["SAST", "Pentesting manual", "Linter", "Firewall"], "answer": "Pentesting manual", "type": "multiple_choice"},
        {"question": "Verdadero o falso: \"WebAuthn permite autenticación sin contraseña.\"", "options": ["Verdadero", "Falso"], "answer": "Falso", "type": "true_false"},
        {"question": "¿Qué estándar regula la seguridad en pagos con tarjeta?", "options": ["GDPR", "PCI-DSS", "HIPAA", "ISO 27001"], "answer": "PCI-DSS", "type": "multiple_choice"}
    ],
    "Tema 12: Ingeniería Inversa de Software": [
        {"question": "¿En qué consiste el desensamblado de un código?", "options": ["Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Convierte el binario en instrucciones de lenguaje ensamblador", "Traduce el código en lenguaje de alto nivel a lenguaje binario", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original"], "answer": "Convierte el binario en instrucciones de lenguaje ensamblador", "type": "multiple_choice"},
        {"question": "¿En qué consiste la descompilación de un código?", "options": ["Traduce el código en lenguaje de alto nivel a lenguaje binario", "Convierte el binario en instrucciones de lenguaje ensamblador", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel"], "answer": "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "type": "multiple_choice"},
        {"question": "¿En qué consiste la compilación de un código?", "options": ["Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Convierte el binario en instrucciones de lenguaje ensamblador", "Traduce el código en lenguaje de alto nivel a lenguaje binario"], "answer": "Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "type": "multiple_choice"},
        {"question": "¿En qué consiste el ensamblado de un código?", "options": ["Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Traduce el código en lenguaje de alto nivel a lenguaje binario", "Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Convierte el binario en instrucciones de lenguaje ensamblador"], "answer": "Convierte el binario en instrucciones de lenguaje ensamblador", "type": "multiple_choice"},
        {"question": "¿Qué es la EULA?", "options": ["Contrato legal que el usuario acepta antes de utilizar un software", "Protocolo de seguridad utilizado en redes privadas", "Lenguaje de programación orientado a objetos", "Tipo de licencia libre para distribuir contenido multimedia"], "answer": "Contrato legal que el usuario acepta antes de utilizar un software", "type": "multiple_choice"},
        {"question": "¿Qué protegen los derechos de autor en el contexto del software?", "options": ["La estructura lógica y los métodos subyacentes del software, como los algoritmos y las rutinas de procesamiento de datos.", "La expresión concreta del programa, en su forma de código fuente y ejecutable, pero no los métodos o ideas que subyacen en él.", "Los diseños arquitectónicos del hardware utilizado para ejecutar el software, incluyendo la disposición de sus componentes físicos.", "La especificación y los protocolos de comunicación utilizados por el software para la interacción en redes y la transmisión de datos."], "answer": "La expresión concreta del programa, en su forma de código fuente y ejecutable, pero no los métodos o ideas que subyacen en él.", "type": "multiple_choice"},
        {"question": "¿Qué es la propiedad intelectual?", "options": ["Es un conjunto de normas que regulan la propiedad física de los bienes muebles e inmuebles.", "Es el derecho exclusivo que tiene el Estado para explotar comercialmente las ideas desarrolladas dentro de sus fronteras.", "Es el conjunto de requisitos que se deben cumplir para poder trabajar en algunos proyectos.", "Conjunto de derechos que protegen las creaciones del intelecto, como invenciones, marcas y secretos industriales."], "answer": "Conjunto de derechos que protegen las creaciones del intelecto, como invenciones, marcas y secretos industriales.", "type": "multiple_choice"},
        {"question": "¿Qué es la ingeniería inversa en el contexto del software?", "options": ["Un proceso que implica la creación de una versión funcional de un software a partir de su código fuente disponible, sin modificar su estructura interna.", "El análisis y descomposición de un producto de software para extraer sus componentes y entender su funcionamiento, con el fin de crear un software compatible o mejorar el original.", "La reimplementación de un software a partir de su especificación funcional, sin tener acceso a su código fuente o componentes internos.", "Un enfoque que busca mejorar el rendimiento de un software mediante la manipulación de su código ejecutable para optimizar su eficiencia sin alterar su funcionalidad."], "answer": "El análisis y descomposición de un producto de software para extraer sus componentes y entender su funcionamiento, con el fin de crear un software compatible o mejorar el original.", "type": "multiple_choice"},
        {"question": "¿En cuál de los siguientes casos podría contradecirse legalmente una cláusula de una licencia de software?", "options": ["Aunque el usuario no haya leído la licencia, la instalación del software implica aceptación tácita, por lo que debe cumplirla en su totalidad.", "Si el software se utiliza únicamente con fines educativos, cualquier cláusula puede ignorarse por motivos pedagógicos.", "Cuando una cláusula vulnera derechos reconocidos por la legislación vigente, como el derecho a realizar ingeniería inversa para lograr interoperabilidad.", "Bajo ninguna circunstancia puede desobedecer una cláusula contractual si el usuario ha aceptado la licencia, independientemente de su contenido."], "answer": "Cuando una cláusula vulnera derechos reconocidos por la legislación vigente, como el derecho a realizar ingeniería inversa para lograr interoperabilidad.", "type": "multiple_choice"},
        {"question": "¿Cuál no es el fin ético de la ingeniería inversa?", "options": ["Garantizar la interoperabilidad de sistemas.", "Vulnerar protecciones para obtener ventajas económicas.", "Reparar o mejorar software/hardware sin soporte oficial.", "Detectar vulnerabilidades en productos para mejorar la seguridad."], "answer": "Vulnerar protecciones para obtener ventajas económicas.", "type": "multiple_choice"},
        {"question": "¿Cuáles son las principales fases de la ingeniería inversa?", "options": ["Diseño, compilación, validación y distribución, centradas en reproducir el software original con mejoras funcionales.", "Captura, edición, reconstrucción y despliegue, orientadas a modificar el comportamiento del software sin analizar su estructura.", "Análisis estático, desensamblado, documentación y modelado, enfocadas en entender el funcionamiento interno sin acceso al código fuente.", "Desarrollo, prueba, refactorización y liberación, aplicadas durante el ciclo de vida convencional del desarrollo de software."], "answer": "Análisis estático, desensamblado, documentación y modelado, enfocadas en entender el funcionamiento interno sin acceso al código fuente.", "type": "multiple_choice"},
        {"question": "¿Cuál de las siguientes afirmaciones describe mejor el papel emergente de la inteligencia artificial (IA) en la ingeniería inversa según el texto?", "options": ["La IA se utiliza principalmente para reemplazar completamente a los ingenieros de software en el análisis de código.", "La IA está demostrando ser una herramienta poderosa para automatizar y acelerar tareas complejas de análisis manual en la ingeniería inversa.", "La IA se limita a la generación de pseudocódigo sin capacidad para ofrecer resúmenes funcionales.", "La IA ha disminuido la importancia de la reconstrucción de código fuente a partir de ejecutables en la ingeniería inversa."], "answer": "La IA está demostrando ser una herramienta poderosa para automatizar y acelerar tareas complejas de análisis manual en la ingeniería inversa.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes enunciados describe con mayor precisión los objetivos principales de la ingeniería inversa en el ámbito del software?", "options": ["Reproducir funcionalidades de un sistema sin necesidad de comprender su estructura ni su comportamiento interno.", "Analizar y comprender el diseño y funcionamiento de un software existente, a menudo sin acceso al código fuente, con fines como la interoperabilidad, la auditoría de seguridad o la recuperación de información.", "Optimizar el rendimiento del software original modificando directamente sus componentes binarios sin ningún tipo de análisis previo.", "Proteger sistemas contra vulnerabilidades mediante técnicas de ofuscación y criptografía aplicadas a sus ejecutables."], "answer": "Analizar y comprender el diseño y funcionamiento de un software existente, a menudo sin acceso al código fuente, con fines como la interoperabilidad, la auditoría de seguridad o la recuperación de información.", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes mecanismos representa una técnica común utilizada para dificultar la ingeniería inversa del software mediante la alteración deliberada de su legibilidad o comprensión?", "options": ["Ofuscación de código, que transforma el código para hacerlo intencionadamente difícil de analizar sin alterar su funcionalidad.", "Criptografía y empaquetado, que ocultan el contenido ejecutable mediante cifrado o compresión.", "AntiDebugging y detección de entornos virtuales, que impiden el análisis dinámico en entornos controlados.", "Hardware seguro, que impide el acceso directo al sistema mediante protección física o chips especializados."], "answer": "Ofuscación de código, que transforma el código para hacerlo intencionadamente difícil de analizar sin alterar su funcionalidad.", "type": "multiple_choice"},
        {"question": "¿Cuál no es una técnica de la ofuscación?", "options": ["Transformar nombres de variables y funciones en identificadores sin sentido.", "Eliminar comentarios y documentación del código fuente.", "Reordenar instrucciones sin alterar el resultado final.", "Insertar código basura o condicionar la ejecución con múltiples saltos lógicos."], "answer": "Eliminar comentarios y documentación del código fuente.", "type": "multiple_choice"},
        {"question": "¿Cuál es el objetivo principal de la ingeniería inversa?", "options": ["Crear un producto desde cero sin referencias", "Analizar un producto para entender su funcionamiento", "Diseñar un nuevo sistema completamente innovador", "Eliminar fallos en una fase de producción inicial"], "answer": "Analizar un producto para entender su funcionamiento", "type": "multiple_choice"},
        {"question": "¿Cómo puede afectar el uso de hardware seguro al proceso de ingeniería de requisitos en el desarrollo de un sistema?", "options": ["Impone requisitos no funcionales adicionales, como restricciones de acceso físico o cifrado en hardware, que deben ser considerados desde las etapas iniciales del análisis.", "Elimina la necesidad de definir requisitos de seguridad, ya que el hardware seguro proporciona protección completa de manera automática.", "Simplifica la validación de requisitos funcionales, al garantizar que todas las operaciones del sistema se ejecuten en un entorno confiable por defecto.", "Sustituye los requisitos de interoperabilidad, dado que los dispositivos seguros actúan como estándares universales en cualquier entorno de ejecución."], "answer": "Impone requisitos no funcionales adicionales, como restricciones de acceso físico o cifrado en hardware, que deben ser considerados desde las etapas iniciales del análisis.", "type": "multiple_choice"},
        {"question": "¿En qué conflicto histórico se popularizó el uso del término \"ingeniería inversa\"?", "options": ["Primera Guerra Mundial", "Guerra Fría", "Segunda Guerra Mundial", "Guerra de Vietnam"], "answer": "Guerra Fría", "type": "multiple_choice"},
        {"question": "¿Qué herramienta se utiliza comúnmente para ingeniería inversa de software?", "options": ["AutoCAD", "Adobe Illustrator", "Ghidra", "Arduino IDE"], "answer": "Ghidra", "type": "multiple_choice"},
        {"question": "¿Qué fase implica la verificación del comportamiento del modelo reconstruido?", "options": ["Recolección de información", "Análisis estructural", "Validación", "Modelado y documentación"], "answer": "Validación", "type": "multiple_choice"}
    ],
    "Tema 13: Vibe Coding y programación asistida por la IA": [
        {"question": "¿Qué distingue principalmente al \"vibe coding\" de otros enfoques asistidos por IA?", "options": ["Que solo utiliza lenguaje natural.", "Que acepta las sugerencias de la IA sin revisar en detalle.", "Que se basa en compilar constantemente.", "Que se ejecuta exclusivamente en navegadores."], "answer": "Que acepta las sugerencias de la IA sin revisar en detalle.", "type": "multiple_choice"},
        {"question": "¿Qué herramienta mencionada funciona como un IDE completo?", "options": ["GitHub Copilot", "Cursor", "Tabnine", "Ponicode"], "answer": "Cursor", "type": "multiple_choice"},
        {"question": "¿Cuál es un riesgo legal clave del uso de código generado por IA?", "options": ["Incluir sin saberlo fragmentos con derechos de autor.", "Que los lenguajes usados sean obsoletos.", "Que se rompan las reglas del compilador.", "Que el código sea demasiado eficiente."], "answer": "Incluir sin saberlo fragmentos con derechos de autor.", "type": "multiple_choice"},
        {"question": "¿Qué característica tiene Lovable que lo diferencia de herramientas como Copilot?", "options": ["Ofrece refactorización en tiempo real.", "Genera código basado en voz.", "Permite crear apps completas sin escribir código.", "Detecta errores lógicos automáticamente."], "answer": "Permite crear apps completas sin escribir código.", "type": "multiple_choice"},
        {"question": "¿Cuál es un riesgo ético destacado relacionado con la responsabilidad del código generado por IA?", "options": ["Que los usuarios finales no puedan modificarlo.", "No está claro quién es responsable si el código falla.", "Las empresas lo reclaman como código libre.", "No se puede compilar sin licencia."], "answer": "No está claro quién es responsable si el código falla.", "type": "multiple_choice"},
        {"question": "¿Cuál es un problema frecuente al aceptar código sugerido sin comprensión profunda?", "options": ["Reduce el tamaño del proyecto.", "Mejora demasiado el rendimiento.", "Dificulta el mantenimiento y depuración.", "Limita la capacidad de escalar horizontalmente."], "answer": "Dificulta el mantenimiento y depuración.", "type": "multiple_choice"},
        {"question": "¿Qué afirmación refleja una limitación contextual de las IAs actuales?", "options": ["Entienden todos los contextos empresariales.", "No comprenden bien los objetivos globales de un proyecto.", "Solo funcionan con proyectos en Python.", "No pueden generar HTML o CSS."], "answer": "No comprenden bien los objetivos globales de un proyecto.", "type": "multiple_choice"},
        {"question": "¿Quién introdujo el término \"vibe coding\"?", "options": ["Los desarrolladores de GitHub Copilot.", "Andrej Karpathy.", "Los creadores de Cursor.", "Un grupo de investigación en procesamiento del lenguaje natural."], "answer": "Andrej Karpathy.", "type": "multiple_choice"},
        {"question": "¿Por qué es problemático el uso de IA en entornos con datos sensibles?", "options": ["La información puede enviarse a servidores externos.", "El código generado siempre es público.", "Las IAs no soportan cifrado.", "Se pierde el control del teclado."], "answer": "La información puede enviarse a servidores externos.", "type": "multiple_choice"},
        {"question": "¿Qué impacto ambiental tiene el uso masivo de IAs generativas en desarrollo?", "options": ["Reducción total del uso energético.", "Ninguno, ya que se usa en la nube.", "Aumento del consumo eléctrico y emisiones de CO₂.", "Solo afecta a usuarios sin conexión."], "answer": "Aumento del consumo eléctrico y emisiones de CO₂.", "type": "multiple_choice"},
        {"question": "¿Qué rol mantiene el desarrollador en el enfoque de vibe coding?", "options": ["Ninguno, todo lo hace la IA.", "Define la intención y supervisa la calidad del código.", "Se limita a validar compilaciones.", "Corrige manualmente cada sugerencia."], "answer": "Define la intención y supervisa la calidad del código.", "type": "multiple_choice"},
        {"question": "¿Qué hace Amazon CodeGuru que lo diferencia de otras herramientas?", "options": ["Genera código desde cero.", "Solo se integra con GitHub.", "Analiza rendimiento y detecta malas prácticas.", "Crea dashboards en tiempo real."], "answer": "Analiza rendimiento y detecta malas prácticas.", "type": "multiple_choice"},
        {"question": "¿Qué puede hacer la IA al detectar errores en código?", "options": ["Detener automáticamente la ejecución.", "Cambiar el lenguaje del proyecto.", "Proponer correcciones y explicarlas.", "Reiniciar el entorno de desarrollo."], "answer": "Proponer correcciones y explicarlas.", "type": "multiple_choice"},
        {"question": "¿Qué función NO cubre típicamente Lovable?", "options": ["Generar backend.", "Crear documentación técnica.", "Construir login y dashboards.", "Desplegar en la nube."], "answer": "Crear documentación técnica.", "type": "multiple_choice"},
        {"question": "¿Qué desafío ético plantea el entrenamiento de modelos con código público?", "options": ["El código deja de funcionar.", "No se pidió consentimiento a los autores originales.", "El código se hace obsoleto al ser usado por IA.", "Se dificulta el aprendizaje automático."], "answer": "No se pidió consentimiento a los autores originales.", "type": "multiple_choice"},
        {"question": "¿Qué práctica fomenta la erosión de habilidades básicas del desarrollador?", "options": ["Uso de algoritmos clásicos.", "Aceptar sugerencias de IA sin reflexión crítica.", "Trabajar con código open source.", "Programar en C++."], "answer": "Aceptar sugerencias de IA sin reflexión crítica.", "type": "multiple_choice"},
        {"question": "¿A qué se refiere Andrej Karpathy con \"vibe coding\"?", "options": ["Un método que requiere una revisión manual intensiva de cada línea de código.", "Un enfoque donde el desarrollador se deja llevar por las sugerencias de la IA, permitiendo que el código evolucione orgánicamente.", "Una técnica centrada únicamente en la optimización del rendimiento del código.", "Un proceso que minimiza el uso de herramientas asistidas por IA."], "answer": "Un enfoque donde el desarrollador se deja llevar por las sugerencias de la IA, permitiendo que el código evolucione orgánicamente.", "type": "multiple_choice"},
        {"question": "¿Qué hacen los benchmarks como WebDev Arena?", "options": ["Evalúan la seguridad de código Java.", "Comparan modelos LLMs resolviendo desafíos de desarrollo.", "Miden el uso de CPU por lenguaje.", "Optimizan el despliegue continuo."], "answer": "Comparan modelos LLMs resolviendo desafíos de desarrollo.", "type": "multiple_choice"},
        {"question": "¿Cuál es una ventaja del uso de lenguaje natural en programación asistida?", "options": ["Requiere permisos root.", "Solo es útil en HTML.", "Hace el flujo de trabajo más intuitivo.", "Solo funciona con IA locales."], "answer": "Hace el flujo de trabajo más intuitivo.", "type": "multiple_choice"},
        {"question": "¿Qué podría pasar si se integra código de IA sin revisión en un entorno comercial?", "options": ["Aumenta la velocidad sin consecuencias.", "Se puede incurrir en demandas por violación de licencias.", "Se compila más rápido siempre.", "Mejora automáticamente la seguridad."], "answer": "Se puede incurrir en demandas por violación de licencias.", "type": "multiple_choice"}
    ],
    "Tema 15: Tratamiento de Legacy Code": [
        {"question": "¿Qué es el \"legacy code\"?", "options": ["Código muy antiguo", "Código heredado difícil de manejar", "Código mal documentado"], "answer": "Código heredado difícil de manejar", "type": "multiple_choice"},
        {"question": "¿Cuál es uno de los principales riesgos al modificar legacy code?", "options": ["Complicar la documentación", "", "Introducir nuevos bugs"], "answer": "Introducir nuevos bugs", "type": "multiple_choice"},
        {"question": "¿Qué técnica ayuda a entender el comportamiento de legacy code?", "options": ["Añadir pruebas automatizadas", "Solamente leer comentarios", "Usar variables globales"], "answer": "Añadir pruebas automatizadas", "type": "multiple_choice"},
        {"question": "¿Por qué es importante refactorizar legacy code?", "options": ["Para aumentar la complejidad", "Para reducir la deuda técnica", "Para mejorar la mantenibilidad"], "answer": "Para mejorar la mantenibilidad", "type": "multiple_choice"},
        {"question": "¿Qué patrón es útil para aislar dependencias en legacy code?", "options": ["Singleton", "Dependency Injection", "Observer"], "answer": "Dependency Injection", "type": "multiple_choice"},
        {"question": "¿Cuál es el primer paso recomendado antes de modificar legacy code?", "options": ["Cambiar el nombre de las funciones", "Eliminar código muerto", "Cubrir el código con pruebas"], "answer": "Cubrir el código con pruebas", "type": "multiple_choice"},
        {"question": "¿Qué herramienta ayuda a identificar áreas problemáticas en legacy code?", "options": ["Javadoc", "Análisis estático de código", "Swagger"], "answer": "Análisis estático de código", "type": "multiple_choice"},
        {"question": "¿Qué significa \"characterization test\" en el contexto de legacy code?", "options": ["Prueba que documenta el comportamiento actual del código", "Prueba de rendimiento", "Prueba de integración continua"], "answer": "Prueba que documenta el comportamiento actual del código", "type": "multiple_choice"},
        {"question": "¿Cuál es una buena práctica al trabajar con legacy code?", "options": ["Hacer grandes cambios de una vez", "Realizar cambios pequeños y controlados", "Ignorar los errores de compilación"], "answer": "Realizar cambios pequeños y controlados", "type": "multiple_choice"},
        {"question": "¿Qué es la \"deuda técnica\" en legacy code?", "options": ["Dinero que se debe al equipo de desarrollo", "Acumulación de decisiones de diseño subóptimas", "Falta de comentarios en el código"], "answer": "Acumulación de decisiones de diseño subóptimas", "type": "multiple_choice"},
        {"question": "¿Qué facilita la refactorización de legacy code?", "options": ["Variables globales", "Código duplicado", "Pruebas automatizadas"], "answer": "Pruebas automatizadas", "type": "multiple_choice"},
        {"question": "¿Qué patrón ayuda a introducir pruebas en legacy code?", "options": ["Factory", "Single Responsibility", "Test Harness"], "answer": "Test Harness", "type": "multiple_choice"},
        {"question": "¿Qué es el \"code coverage\" y por qué es útil en legacy code?", "options": ["Un indicador del porcentaje de código cubierto por pruebas", "Una métrica de rendimiento", "Un tipo de refactorización"], "answer": "Un indicador del porcentaje de código cubierto por pruebas", "type": "multiple_choice"},
        {"question": "¿Qué es recomendable hacer si no se entiende una parte del legacy code?", "options": ["Eliminarla", "Añadir pruebas para documentar su comportamiento", "Pedirle a la IA que lo cambie"], "answer": "Añadir pruebas para documentar su comportamiento", "type": "multiple_choice"},
        {"question": "¿Qué técnica ayuda a reducir el acoplamiento en legacy code?", "options": ["Uso de variables globales", "Uso de métodos estáticos", "Introducir interfaces"], "answer": "Introducir interfaces", "type": "multiple_choice"},
        {"question": "¿Por qué es peligroso reescribir todo el legacy code de una vez?", "options": ["Porque no reduce la deuda técnica", "Porque se pueden perder funcionalidades y aumentar los errores", "Porque no todo el código puede estar mal"], "answer": "Porque se pueden perder funcionalidades y aumentar los errores", "type": "multiple_choice"},
        {"question": "¿Qué es el \"Refactoring\" en el contexto de legacy code?", "options": ["El proceso de mejorar la estructura interna del código sin cambiar su comportamiento externo", "El proceso de eliminar código muerto", "El proceso de documentar el código existente"], "answer": "El proceso de mejorar la estructura interna del código sin cambiar su comportamiento externo", "type": "multiple_choice"},
        {"question": "¿Qué ayuda a reducir el miedo a modificar legacy code?", "options": ["Tener una buena suite de pruebas y buena documentación", "Estar familiarizado con el lenguaje de programación", "Tener comentarios"], "answer": "Tener una buena suite de pruebas y buena documentación", "type": "multiple_choice"},
        {"question": "¿Qué es una \"prueba de humo\" en el contexto de legacy code?", "options": ["Prueba que verifica el comportamiento", "Prueba básica para comprobar que el sistema funciona tras un cambio", "Prueba de rendimiento"], "answer": "Prueba básica para comprobar que el sistema funciona tras un cambio", "type": "multiple_choice"},
        {"question": "¿Qué actitud es recomendable al enfrentarse a legacy code?", "options": ["Cambiar todo de una vez", "Anteponer tu criterio a la documentación", "Ser cauteloso y validar cada cambio"], "answer": "Ser cauteloso y validar cada cambio", "type": "multiple_choice"}
    ],
    "Tema 16: Protocolo Modelo-Contexto (MCP)": [
        {"question": "¿Cuál es el objetivo principal del Protocolo Modelo-Contexto (MCP)?", "options": ["Desarrollar un nuevo modelo de IA", "Establecer un protocolo estandarizado para conectar modelos de IA con fuentes de datos externas", "Crear un sistema operativo para dispositivos inteligentes", "Mejorar la velocidad de conexión entre servidores físicos"], "answer": "Establecer un protocolo estandarizado para conectar modelos de IA con fuentes de datos externas", "type": "multiple_choice"},
        {"question": "¿Qué problema común de integración resuelve el MCP?", "options": ["La falta de potencia de cómputo en los dispositivos móviles", "El sobreajuste de los modelos de IA durante el entrenamiento", "La necesidad de crear conectores independientes para cada combinación de modelo y fuente de datos", "La latencia entre modelos entrenados y su uso en dispositivos"], "answer": "La necesidad de crear conectores independientes para cada combinación de modelo y fuente de datos", "type": "multiple_choice"},
        {"question": "¿Cómo se describe mejor la arquitectura fundamental del MCP?", "options": ["Una arquitectura blockchain donde los datos se validan en un registro público", "Una red peer-to-peer descentralizada donde todos comparten datos sin servidores", "Un diseño cliente-servidor donde la aplicación de IA actúa como cliente que se conecta a servidores de datos", "Un modelo federado de entrenamiento distribuido"], "answer": "Un diseño cliente-servidor donde la aplicación de IA actúa como cliente que se conecta a servidores de datos", "type": "multiple_choice"},
        {"question": "Dentro de MCP, ¿qué función tiene un servidor MCP?", "options": ["Entrenar y actualizar el modelo de IA con nuevos datos", "Proporcionar acceso a datos y funcionalidades externas al modelo de IA", "Aumentar la velocidad de procesamiento del modelo", "Coordinar múltiples agentes de IA en paralelo"], "answer": "Proporcionar acceso a datos y funcionalidades externas al modelo de IA", "type": "multiple_choice"},
        {"question": "Dentro de MCP, ¿qué función tiene un cliente MCP?", "options": ["Almacenar copias de los datos del servidor", "Ejecutar el modelo de IA localmente en una máquina cliente", "Facilitar la comunicación entre la aplicación de IA y los servidores MCP", "Traducir instrucciones del modelo a comandos de máquina"], "answer": "Facilitar la comunicación entre la aplicación de IA y los servidores MCP", "type": "multiple_choice"},
        {"question": "En un flujo típico de comunicación MCP, ¿qué ocurre primero?", "options": ["El servidor MCP envía datos al modelo sin solicitud", "El cliente MCP consulta al servidor sobre sus capacidades", "El modelo de IA se actualiza automáticamente con nuevos parámetros", "El servidor solicita acceso a la API del modelo"], "answer": "El cliente MCP consulta al servidor sobre sus capacidades", "type": "multiple_choice"},
        {"question": "¿Qué significa que las conexiones en MCP sean \"bidireccionales\"?", "options": ["El modelo de IA puede tanto solicitar información al servidor como invocar acciones en él", "Toda la comunicación se limita a una sola dirección (del servidor a la IA)", "Los datos fluyen solo del modelo al servidor sin respuestas", "Solo se pueden usar con redes privadas"], "answer": "El modelo de IA puede tanto solicitar información al servidor como invocar acciones en él", "type": "multiple_choice"},
        {"question": "¿Cuál es una ventaja clave de usar el MCP?", "options": ["Aumenta automáticamente la capacidad de memoria de los modelos de IA", "Evita el acceso a datos externos para mejorar la privacidad", "Permite usar un único protocolo estándar en lugar de múltiples integraciones personalizadas", "Crea modelos completamente nuevos desde cero"], "answer": "Permite usar un único protocolo estándar en lugar de múltiples integraciones personalizadas", "type": "multiple_choice"},
        {"question": "MCP ayuda a mantener el contexto en los sistemas de IA cuando…", "options": ["El modelo de IA se reinicia en cada nueva sesión", "Se entrena el modelo con datos desordenados", "El asistente de IA cambia entre diferentes herramientas y conjuntos de datos durante una tarea", "El servidor realiza pruebas automáticas sobre la IA"], "answer": "El asistente de IA cambia entre diferentes herramientas y conjuntos de datos durante una tarea", "type": "multiple_choice"},
        {"question": "¿Cuál es un ejemplo de caso de uso real de MCP?", "options": ["Un modelo de IA que mejora automáticamente la calidad de las fotos", "Un sistema que entrena varios modelos sin supervisión", "Un asistente de codificación que lee el código en un repositorio para dar sugerencias basadas en el contexto", "Un motor de búsqueda que indexa páginas web aleatorias"], "answer": "Un asistente de codificación que lee el código en un repositorio para dar sugerencias basadas en el contexto", "type": "multiple_choice"},
        {"question": "¿Qué significa que MCP sea \"independiente del modelo\" (model-agnostic)?", "options": ["Solo funciona con un modelo de IA particular", "Puede trabajar con cualquier asistente de IA o modelo de lenguaje, sin importar el proveedor", "Selecciona automáticamente el mejor modelo de IA para cada tarea", "Funciona únicamente con modelos entrenados en la nube"], "answer": "Puede trabajar con cualquier asistente de IA o modelo de lenguaje, sin importar el proveedor", "type": "multiple_choice"},
        {"question": "¿Cuál de los siguientes no es un componente principal del MCP?", "options": ["La especificación del protocolo y sus SDK", "Servidores MCP locales y en la nube", "Un repositorio interno de datos no relacionado", "Conectores estandarizados para APIs abiertas"], "answer": "Un repositorio interno de datos no relacionado", "type": "multiple_choice"},
        {"question": "¿Cómo puede usarse MCP en un entorno empresarial?", "options": ["Conectando todos los sistemas de la empresa a la nube sin control", "Reemplazando al departamento de TI en la toma de decisiones", "Un asistente interno recupera información de sistemas CRM y bases de conocimiento de forma segura", "Usando asistentes virtuales para marketing automático sin permisos"], "answer": "Un asistente interno recupera información de sistemas CRM y bases de conocimiento de forma segura", "type": "multiple_choice"},
        {"question": "¿Cuál podría ser una limitación práctica de MCP?", "options": ["Requiere configurar y mantener servidores MCP, lo que puede agregar complejidad inicial", "Asegura datos a nivel militar automáticamente", "Impide que los modelos de IA accedan a datos externos por diseño", "Solo es compatible con Linux"], "answer": "Requiere configurar y mantener servidores MCP, lo que puede agregar complejidad inicial", "type": "multiple_choice"},
        {"question": "¿Cómo se intercambian mensajes entre clientes y servidores en MCP?", "options": ["Conversando por chat en tiempo real", "Usando mensajes en formato JSON (JSON-RPC 2.0) a través de HTTP", "Intercambiando archivos de texto manualmente", "A través de mensajes binarios encriptados con QR"], "answer": "Usando mensajes en formato JSON (JSON-RPC 2.0) a través de HTTP", "type": "multiple_choice"},
        {"question": "¿Qué operaciones típicas puede realizar un modelo de IA mediante un servidor MCP?", "options": ["Reentrenar otros modelos directamente en el servidor", "Realizar procesamiento de imágenes localmente sin ayuda", "Leer archivos de datos y ejecutar funciones o consultas en el servidor", "Modificar el hardware del servidor de forma remota"], "answer": "Leer archivos de datos y ejecutar funciones o consultas en el servidor", "type": "multiple_choice"},
        {"question": "Al usar MCP con múltiples herramientas, ¿qué permite esto a un agente de IA?", "options": ["Solo elegir una herramienta al azar para cada tarea", "Entrar automáticamente en un modo de aprendizaje no supervisado", "Acceder simultáneamente a varias fuentes de información y combinarlas en su razonamiento", "Ejecutar múltiples instancias del mismo servidor MCP"], "answer": "Acceder simultáneamente a varias fuentes de información y combinarlas en su razonamiento", "type": "multiple_choice"},
        {"question": "¿Por qué es importante que MCP sea un estándar abierto?", "options": ["Obliga a todos los usuarios a pagar una licencia costosa", "Cambia continuamente sin una versión estable", "Facilita que varios proveedores y herramientas sean compatibles sin licencias cerradas", "Impide el uso de servidores privados"], "answer": "Facilita que varios proveedores y herramientas sean compatibles sin licencias cerradas", "type": "multiple_choice"},
        {"question": "¿Qué permite un servidor MCP personalizado?", "options": ["Convertir el servidor en un modelo de IA", "Crear nuevos idiomas de programación automáticamente", "Conectar sistemas internos o bases de datos privadas de la organización con los modelos de IA", "Generar modelos de IA basados en ADN"], "answer": "Conectar sistemas internos o bases de datos privadas de la organización con los modelos de IA", "type": "multiple_choice"},
        {"question": "¿Cuál de estas NO es una función del MCP?", "options": ["Proporcionar contexto adicional a un asistente de IA durante una conversación", "Entrenar un nuevo modelo de lenguaje por sí mismo", "Ejecutar funciones externas (como consultas o comandos) en respuesta a solicitudes del modelo de IA", "Gestionar el acceso a fuentes de datos remotas"], "answer": "Entrenar un nuevo modelo de lenguaje por sí mismo", "type": "multiple_choice"}
    ]
}

class AppController:
    def __init__(self, master):
        self.master = master
        self.master.title("Cuestionario de Temas")
        self.master.geometry("200x350")
        
        self.menu_frame = None
        self.quiz_frame = None
        self.results_frame = None

        self.show_menu()

    def clear_frame(self):
        """Limpia el contenido del frame maestro."""
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.clear_frame()
        self.menu_frame = QuizMenuFrame(self.master, self.start_quiz_session)
        self.menu_frame.pack(fill="both", expand=True)

    def start_quiz_session(self, quiz_questions):
        self.clear_frame()
        self.quiz_frame = QuizSessionFrame(self.master, quiz_questions, self.show_results)
        self.quiz_frame.pack(fill="both", expand=True)

    def show_results(self, score, total_questions, correct_answers, incorrect_answers):
        self.clear_frame()
        self.results_frame = QuizResultsFrame(self.master, score, total_questions, correct_answers, incorrect_answers, self.show_menu)
        self.results_frame.pack(fill="both", expand=True)


class QuizMenuFrame(tk.Frame):
    def __init__(self, master, start_quiz_callback):
        super().__init__(master)
        self.master = master
        self.start_quiz_callback = start_quiz_callback
        self.selected_topics_vars = {}
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Selecciona los temas para el cuestionario:", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        selection_buttons_frame = tk.Frame(self)
        selection_buttons_frame.pack(pady=5)

        select_all_button = ttk.Button(selection_buttons_frame, text="Seleccionar Todos", command=self.select_all_topics)
        select_all_button.pack(side=tk.LEFT, padx=5)

        deselect_all_button = ttk.Button(selection_buttons_frame, text="Deseleccionar Todos", command=self.deselect_all_topics)
        deselect_all_button.pack(side=tk.LEFT, padx=5)

        self.checkbox_frame_container = tk.Frame(self)
        self.checkbox_frame_container.pack(fill="both", expand=True, padx=20, pady=10)

        self.canvas = tk.Canvas(self.checkbox_frame_container)
        self.scrollbar = tk.Scrollbar(self.checkbox_frame_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        def get_topic_sort_key(topic_name):
            try:
                parts = topic_name.split(' ')
                if len(parts) > 1 and parts[0] == 'Tema' and parts[1].isdigit():
                    return int(parts[1])
                return float('inf')
            except (ValueError, IndexError):
                return float('inf')

        for topic_name in sorted(ALL_QUESTIONS.keys(), key=get_topic_sort_key):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.scrollable_frame, text=topic_name, variable=var, font=("Arial", 12))
            cb.pack(anchor="w", pady=2)
            self.selected_topics_vars[topic_name] = var

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Frame for quiz start buttons
        quiz_start_buttons_frame = tk.Frame(self)
        quiz_start_buttons_frame.pack(pady=10)

        # Button for 40 questions from selected topics
        start_selected_button = tk.Button(quiz_start_buttons_frame, text="Iniciar Cuestionario (40 Preguntas de Temas Seleccionados)", command=self._prepare_and_start_quiz_selected, font=("Arial", 10, "bold"))
        start_selected_button.pack(pady=5)

        # Button for ALL questions from ALL topics
        start_all_topics_button = tk.Button(quiz_start_buttons_frame, text="Iniciar Cuestionario (Todas las Preguntas de Todos los Temas)", command=self._prepare_and_start_quiz_all_topics, font=("Arial", 10, "bold"), bg="lightgreen")
        start_all_topics_button.pack(pady=5)


    def select_all_topics(self):
        for var in self.selected_topics_vars.values():
            var.set(True)

    def deselect_all_topics(self):
        for var in self.selected_topics_vars.values():
            var.set(False)

    def _prepare_and_start_quiz_selected(self):
        """Prepares and starts a quiz session with 40 questions from selected topics."""
        selected_topics = [topic for topic, var in self.selected_topics_vars.items() if var.get()]

        if not selected_topics:
            messagebox.showwarning("Sin selección", "Por favor, selecciona al menos un tema para iniciar el cuestionario de temas seleccionados.")
            return

        all_selected_questions = []
        for topic in selected_topics:
            all_selected_questions.extend(ALL_QUESTIONS[topic])

        if not all_selected_questions:
            messagebox.showinfo("Sin preguntas", "Los temas seleccionados no contienen preguntas. Por favor, elige otros temas.")
            return

        num_questions_to_ask = 40
        if len(all_selected_questions) < num_questions_to_ask:
            messagebox.showinfo("Pocas preguntas", f"Solo hay {len(all_selected_questions)} preguntas disponibles en los temas seleccionados. Se usarán todas.")
            num_questions_to_ask = len(all_selected_questions)

        quiz_questions = random.sample(all_selected_questions, num_questions_to_ask)
        self.start_quiz_callback(quiz_questions)

    def _prepare_and_start_quiz_all_topics(self):
        """Prepares and starts a quiz session with ALL questions from ALL topics."""
        all_questions = []
        for topic in ALL_QUESTIONS.keys():
            all_questions.extend(ALL_QUESTIONS[topic])
        
        if not all_questions:
            messagebox.showinfo("Sin preguntas", "No hay preguntas disponibles en ningún tema para realizar el test completo.")
            return

        # No specific number of questions here, take all of them
        random.shuffle(all_questions) # Shuffle all questions
        quiz_questions = all_questions 

        self.start_quiz_callback(quiz_questions)


class QuizSessionFrame(tk.Frame):
    def __init__(self, master, questions, show_results_callback):
        super().__init__(master)
        self.master = master
        self.questions = questions
        self.show_results_callback = show_results_callback
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.user_answers = {}
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.master.geometry("800x600")
        
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(fill="x", pady=5)

        self.question_number_label = tk.Label(self.info_frame, text="", font=("Arial", 14, "bold"))
        self.question_number_label.pack(side=tk.LEFT, padx=10)

        self.score_counter_label = tk.Label(self.info_frame, text="Correctas: 0 | Incorrectas: 0", font=("Arial", 12))
        self.score_counter_label.pack(side=tk.RIGHT, padx=10)

        self.question_label = tk.Label(self, text="", font=("Arial", 12), wraplength=700, justify="left")
        self.question_label.pack(pady=10, anchor="w")

        self.options_frame = tk.Frame(self)
        self.options_frame.pack(pady=10, anchor="w")

        self.radio_var = tk.StringVar()

        self.feedback_label = tk.Label(self, text="", font=("Arial", 10, "italic"))
        self.feedback_label.pack(pady=5, anchor="w")

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        self.answer_button = tk.Button(self.button_frame, text="Responder", command=self.check_answer, font=("Arial", 12), bg="lightblue")
        self.answer_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Siguiente Pregunta", command=self.go_to_next_question, font=("Arial", 12), state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.finish_button = tk.Button(self.button_frame, text="Finalizar Test", command=self.confirm_finish_quiz, font=("Arial", 12), bg="orange")
        self.finish_button.pack(side=tk.RIGHT, padx=10)

    def update_score_display(self):
        self.score_counter_label.config(text=f"Correctas: {self.correct_answers} | Incorrectas: {self.incorrect_answers}")

    def display_question(self):
        if self.current_question_index < len(self.questions):
            q_data = self.questions[self.current_question_index]
            self.question_number_label.config(text=f"Pregunta {self.current_question_index + 1}/{len(self.questions)}:")
            self.question_label.config(text=q_data['question'])
            self.feedback_label.config(text="")
            self.update_score_display()

            for widget in self.options_frame.winfo_children():
                widget.destroy()

            self.radio_var.set("")

            self.answer_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)

            if q_data['type'] == 'multiple_choice':
                random.shuffle(q_data['options'])
                for i, option in enumerate(q_data['options']):
                    rb = tk.Radiobutton(self.options_frame, text=option, variable=self.radio_var, value=option, font=("Arial", 11), wraplength=650, justify="left")
                    rb.pack(anchor="w", pady=2)
            elif q_data['type'] == 'true_false':
                options_tf = ['Verdadero', 'Falso']
                for option in options_tf:
                    rb = tk.Radiobutton(self.options_frame, text=option, variable=self.radio_var, value=option, font=("Arial", 11), wraplength=650, justify="left")
                    rb.pack(anchor="w", pady=2)
            
            if self.current_question_index == len(self.questions) - 1:
                self.next_button.config(text="Ver Resultados")
            else:
                self.next_button.config(text="Siguiente Pregunta")
        else:
            self.show_results_callback(self.correct_answers, len(self.questions), self.correct_answers, self.incorrect_answers)

    def check_answer(self):
        user_selection = self.radio_var.get()
        if not user_selection:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción antes de responder.")
            return

        current_q_data = self.questions[self.current_question_index]
        self.user_answers[self.current_question_index] = user_selection

        for widget in self.options_frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.config(state=tk.DISABLED)

        if user_selection == current_q_data['answer']:
            self.correct_answers += 1
            self.feedback_label.config(text="¡Correcto!", fg="green")
        else:
            self.incorrect_answers += 1
            self.feedback_label.config(text=f"Incorrecto. La respuesta correcta era: {current_q_data['answer']}", fg="red")
        
        self.update_score_display()
        
        self.answer_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def go_to_next_question(self):
        self.current_question_index += 1
        self.display_question()

    def confirm_finish_quiz(self):
        response = messagebox.askyesno("Finalizar Test", "¿Estás seguro de que quieres finalizar el test? Tu progreso actual se guardará y se mostrarán los resultados.")
        if response:
            self.show_results_callback(self.correct_answers, len(self.questions), self.correct_answers, self.incorrect_answers)


class QuizResultsFrame(tk.Frame):
    def __init__(self, master, score, total_questions, correct_answers, incorrect_answers, return_to_menu_callback):
        super().__init__(master)
        self.master = master
        self.score = score
        self.total_questions = total_questions
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers
        self.return_to_menu_callback = return_to_menu_callback
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry("500x700")
        result_label = tk.Label(self, text="--- Cuestionario Terminado ---", font=("Arial", 16, "bold"))
        result_label.pack(pady=20)

        score_label = tk.Label(self, text=f"Has obtenido {self.score} de {self.total_questions} preguntas correctas.", font=("Arial", 14))
        score_label.pack(pady=10)

        correct_label = tk.Label(self, text=f"Respuestas Correctas: {self.correct_answers}", font=("Arial", 12), fg="green")
        correct_label.pack(pady=5)

        incorrect_label = tk.Label(self, text=f"Respuestas Incorrectas: {self.incorrect_answers}", font=("Arial", 12), fg="red")
        incorrect_label.pack(pady=5)

        percentage = (self.score / self.total_questions) * 100
        percentage_label = tk.Label(self, text=f"Tu puntuación: {percentage:.2f}%", font=("Arial", 14, "bold"))
        percentage_label.pack(pady=10)

        return_button = tk.Button(self, text="Volver al Menú Principal", command=self.return_to_menu_callback, font=("Arial", 12))
        return_button.pack(pady=30)


if __name__ == "__main__":
    root = tk.Tk()
    app_controller = AppController(root)
    root.mainloop()
