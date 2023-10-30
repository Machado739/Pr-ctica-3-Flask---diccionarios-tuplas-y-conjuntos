
# Flask API para Operaciones con Diccionarios, Conjuntos y Tuplas

Esta API de Flask proporciona rutas para realizar diversas operaciones con diccionarios, conjuntos y tuplas. A continuación, se detallan las rutas disponibles y cómo usarlas.

## Operaciones con Diccionarios

### 1. Obtener el diccionario actual

- **Ruta**: `/get_diccionario`
- **Método**: GET
- **Descripción**: Devuelve el diccionario actual como JSON.

### 2. Agregar una clave-valor al diccionario

- **Ruta**: `/agregar_clave_valor/<clave>/<valor>`
- **Método**: GET
- **Descripción**: Agrega una clave y su valor al diccionario.
- **Ejemplo de uso**: `http://localhost:5000/agregar_clave_valor/mi_clave/mi_valor`

### 3. Eliminar una clave del diccionario

- **Ruta**: `/eliminar_clave/<clave>`
- **Método**: GET
- **Descripción**: Elimina una clave específica del diccionario.
- **Ejemplo de uso**: `http://localhost:5000/eliminar_clave/mi_clave`

### 4. Modificar el valor de una clave en el diccionario

- **Ruta**: `/modificar_valor/<clave>/<nuevo_valor>`
- **Método**: GET
- **Descripción**: Modifica el valor de una clave en el diccionario.
- **Ejemplo de uso**: `http://localhost:5000/modificar_valor/mi_clave/nuevo_valor`

### 5. Combinar dos diccionarios mediante parámetros de consulta

- **Ruta**: `/combinar_diccionarios`
- **Método**: GET
- **Descripción**: Combina el diccionario actual con otro diccionario proporcionado en los parámetros de consulta.
- **Ejemplo de uso**: `http://localhost:5000/combinar_diccionarios?diccionario2={"otra_clave":"otro_valor"}`

## Operaciones con Conjuntos

### 6. Agregar un elemento a un conjunto

- **Ruta**: `/agregar_elemento_conjunto/<elemento>`
- **Método**: GET
- **Descripción**: Agrega un elemento al conjunto.
- **Ejemplo de uso**: `http://localhost:5000/agregar_elemento_conjunto/nuevo_elemento`

### 7. Eliminar un elemento de un conjunto

- **Ruta**: `/eliminar_elemento_conjunto/<elemento>`
- **Método**: GET
- **Descripción**: Elimina un elemento específico del conjunto.
- **Ejemplo de uso**: `http://localhost:5000/eliminar_elemento_conjunto/elemento_a_eliminar`

### 8. Combinar dos conjuntos mediante parámetros de consulta

- **Ruta**: `/combinar_conjuntos`
- **Método**: GET
- **Descripción**: Combina dos conjuntos proporcionados en los parámetros de consulta.
- **Ejemplo de uso**: `http://localhost:5000/combinar_conjuntos?conjunto1=["elemento1","elemento2"]&conjunto2=["elemento3","elemento4"]`

### 9. Obtener la diferencia entre dos conjuntos mediante parámetros de consulta

- **Ruta**: `/diferencia_entre_conjuntos`
- **Método**: GET
- **Descripción**: Calcula la diferencia entre dos conjuntos proporcionados en los parámetros de consulta.
- **Ejemplo de uso**: `http://localhost:5000/diferencia_entre_conjuntos?conjunto1=["elemento1","elemento2","elemento3"]&conjunto2=["elemento2","elemento3","elemento4"]`

## Operaciones con Tuplas

### 10. Agregar un elemento a una tupla y crear una nueva tupla

- **Ruta**: `/agregar_elemento_tupla/<elemento>/<tupla>`
- **Método**: GET
- **Descripción**: Agrega un elemento a una tupla y crea una nueva tupla.
- **Ejemplo de uso**: `http://localhost:5000/agregar_elemento_tupla/elemento_para_agregar/[1,2,3]`

### 11. Eliminar un elemento de una tupla y crear una nueva tupla

- **Ruta**: `/eliminar_elemento_tupla/<elemento>`
- **Método**: GET
- **Descripción**: Elimina un elemento de una tupla y crea una nueva tupla.
- **Ejemplo de uso**: `http://localhost:5000/eliminar_elemento_tupla/elemento_a_eliminar?tupla=(1,2,3,4)`

### 12. Concatenar dos tuplas en una nueva tupla

- **Ruta**: `/concatenar_tuplas`
- **Método**: GET
- **Descripción**: Concatena dos tuplas proporcionadas en los parámetros de consulta para crear una nueva tupla.
- **Ejemplo de uso**: `http://localhost:5000/concatenar_tuplas?tupla1=[1,2,3]&tupla2=[4,5,6]`

### 13. Revertir el orden de una tupla y crear una nueva tupla

- **Ruta**: `/revertir_tupla`
- **Método**: GET
- **Descripción**: Revierte el orden de una tupla y crea una nueva tupla.
- **Ejemplo de uso**: `http://localhost:5000/revertir_tupla?tupla=[1,2,3]`

¡Espero que esta información te sea útil para crear un archivo README en tu repositorio de GitHub! Puedes copiar y pegar este contenido en tu archivo README y personalizarlo según tus necesidades.
