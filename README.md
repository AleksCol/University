# Lista de cambios y correciones dentro del programa del Laboratorio 5.

Se corrigieron los siguientes errores: (22/05/2026 a las 7:28 P.M)

Correcciones realizadas en `util.py`

1. `validarnombre`* — La condición `or letra in ' '` rechazaba los espacios, que sí son válidos según el enunciado. Se eliminó esa condición, dejando solo `if not letra in letras`.

2. `validar_documento` — El `return True` estaba dentro del `for`, por lo que solo se validaba el primer carácter del documento. Se movió el `return True` fuera del bucle `for`.

3. `imprimir_tabla` / `imprimir_fila`** — `imprimir_fila` estaba definida fuera de `imprimir_tabla`, por lo que no tenía acceso a la variable `ancho`. Además, el código posterior tenía indentación inconsistente (0, 4 y 8 espacios mezclados). Se anidó `imprimir_fila` dentro de `imprimir_tabla` y se uniformizó toda la indentación a 4 espacios.

Aquí tienes el texto complementado para que tu compañera entienda bien qué hace cada función:

---

**Añadidos:**

Se añadieron las siguientes funciones en el archivo "funciones.py" el 22/05/2026 a las 8:58 P.M

Se importó la biblioteca JSON con `import json`, necesaria para leer y escribir archivos en formato `.json`.

Se añadieron las siguientes funciones:

**1. `cargar_usuarios()`**
Lee el archivo `usuarios.csv` y retorna una lista de diccionarios, donde cada diccionario representa un usuario con las claves `codigo`, `nombre`, `clave` y `rol`. Omite líneas vacías y salta la primera línea (encabezado).

**2. `cargar_estaciones()`**
Lee el archivo `estaciones.csv` y retorna una lista de diccionarios con las claves `codigo` y `nombre` por cada estación registrada. Tiene el mismo comportamiento que `cargar_usuarios()` para manejar líneas vacías y el encabezado.

**3. `cargar_variables()`**
Lee el archivo `variables.json` y retorna únicamente la lista almacenada bajo la clave `"variables"` dentro del JSON.

**4. `cargar_registros()`**
Lee el archivo `registros.json` y retorna únicamente la lista almacenada bajo la clave `"registros"` dentro del JSON.

**5. `guardar_usuarios(usuarios)`**
Recibe la lista de usuarios y sobreescribe el archivo `usuarios.csv` con los datos actualizados. Escribe primero la línea de encabezado `codigo,nombre,clave,rol` y luego una línea por cada usuario.

**6. `guardar_estaciones(estaciones)`**
Recibe la lista de estaciones y sobreescribe el archivo `estaciones.csv` con los datos actualizados. Escribe primero la línea de encabezado `codigo,nombre` y luego una línea por cada estación.

**7. `guardar_registros(registros)`**
Recibe la lista de registros y sobreescribe el archivo `registros.json` envolviendo los datos dentro de un diccionario con la clave `"registros"`, usando indentación de 4 espacios para mantener el formato legible.

**8. `buscar_usuario(usuarios, codigo)`**
Recorre la lista de usuarios buscando uno cuyo `codigo` coincida con el parámetro. Retorna el índice (posición) del usuario en la lista si lo encuentra, o `-1` si no existe.

**9. `autenticar(usuarios, codigo, clave)`**
Usa `buscar_usuario()` para localizar al usuario por código. Si no existe retorna `None`. Si existe, compara la clave ingresada con la almacenada y retorna el diccionario del usuario si coinciden, o `None` si la clave es incorrecta.

