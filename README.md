# Descripción del proyecto
El proyecto consiste en desarrollar un web scraper. Recorreremos un paginador para obtener datos básicos de productos y realizar algunas capturas de pantalla.

## Inicializar proyecto

###   Clonar e instalar proyecto desde Github

Deberá crear un fork del proyecto ([link](https://github.com/Kemok-Repos/python-ejercicio)) hacia un repositorio personal (configurar como público), para luego clonarlo en su ambiente de desarrollo local. A partir de este momento se espera que utilice git para manejar el código del proyecto.

## Dependencias

*    Utilizaremos [Selenium](https://selenium-python.readthedocs.io) para automatizar la navegación y extracción de datos (el uso de Selenium requiere la instalación de un webdriver: Chrome, Firefox o Chromium). 
*    SQLite para almacenar los datos.
*    Queda a discreción el uso de paquetes adicionales. 

## Requerimientos

Nuestra URL base es la siguiente:
[Sitio de prueba de extracción](https://webscraper.io/test-sites/e-commerce/static/computers/laptops)

*   Obtener un listado de productos del paginador (recorriendo cada una de las páginas) bajo las siguientes condiciones:
    *   Guardar en una tabla el ID (dato importante para visitar el detalle del producto) y nombre de los productos que tengan una calificación igual o mayor a N estrellas, donde N es un número de 1 a 5 definido por el usuario. De no definirse el flag utilizar el número 3 como valor predeterminado.
*   Luego de obtener el listado, deberá visitar el link de cada uno de los productos obtenidos y realizar las siguientes acciones:
    *   Guardar el detalle y precio (no tomar en cuenta las variaciones de HDD) correspondiente a cada producto.
    *   Tomar una captura de pantalla de los productos que tengan 10 o más reviews.
        *    Guardar el nombre asignado al archivo en el producto correspondiente.
 
 ### Ejemplo de cómo llamar el script:
 <pre><code> mi_sript.py --stars 5 </code></pre>

## Puntos a evaluar

*   Cumplir todos los requerimientos.
*   Usar Git correctamente.
*   Aplicar buenas prácticas de programación.
*   Uso de principios SOLID.

## Suman puntos a tu favor

*   Uso de estándares de programación [PEP 8](https://peps.python.org/pep-0008/).
*   Desarrollo guiado por pruebas.
*   Patrones de diseño.
*   Aplicación de algún workflow en Git.
