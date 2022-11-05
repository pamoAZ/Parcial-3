## Table of Contents
1. [Introduccion](#Introduccion)
2. [Desarrollo](#Desarrollo)
3. [Resultados](#Resultados)

### Introduccion
***
Hay una forma de aproximar la integral de una función f(x) entre a y b. Este método consiste en dividir el intervalo h =
b−a/n en n sub-intervalos (n par) iguales ([a, x1], [x1, x2], ..., [xn−1, b]), de forma tal que xi = a + ih. La integral de f(x) definida entre a y b está dada por

En análisis numérico, la regla o método de Simpson (nombrada así en honor de Thomas Simpson) es un método de integración numérica que se utiliza para obtener la aproximación de la integral:

En el caso de que el intervalo [a,b] no sea lo suficientemente pequeño, el error al calcular la integral puede ser muy grande. Para ello, se recurre a la fórmula compuesta de Simpson. Se divide el intervalo [a,b] en n subintervalos iguales (con n par),
## Desarrollo
En la implementacion de este metodo en python, se utilizan las librerias  matplotlib numpy y math, para que el usuario pueda escribir una funcion(que tiene que ser en terminos entendibles para la consola) y por medio del metodo descrito en la introduccion se calcule un valor numero para esta funcion, se utiliza la syntaxis y modulos de las librerias para calcular el valor aproximado a partir de los datos ingresados y el valor real, luego se grafica ambas integrales 
## Resultados
***
A little intro about the installation. 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```
Side information: To use the application in a special environment use ```lorem ipsum``` to start
