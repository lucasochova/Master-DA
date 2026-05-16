--Muestra los nombres de todas las películas con una clasificación por edades de ‘Rʼ.

SELECT Title titulo, RELEASE_YEAR  año
FROM film
WHERE RATING = 'R'

--Encuentra los nombres de los actores que tengan un “actor_idˮ entre 30 y 40.

SELECT actor_id, Concat (first_name, ' ', last_name)
from actor
where actor_id >30 and actor_id <40

-- Obtén las películas cuyo idioma coincide con el idioma original.

SELECT title titulo , name idioma
FROM film join language ON film.LANGUAGE_ID = "language".LANGUAGE_ID
where ORIGINAL_LANGUAGE_ID = film.LANGUAGE_ID 

-- Ordena las películas por duración de forma ascendente.

SELECT title titulo, release_year año, RENTAL_RATE , RATING, length duracion
from film
ORDER BY LENGTH, RATING  asc

-- Encuentra el nombre y apellido de los actores que tengan ‘Allenʼ en su apellido.

SELECT concat(first_name, ' ',last_name) nombre_y_apellido
FROM actor
WHERE last_name ='ALLEN'

--Encuentra la cantidad total de películas en cada clasificación de la tabla
--"filmˮ y muestra la clasificación junto con el recuento.

select count(film_id), rating
from film
GROUP BY  RATING
order by count(film_id)

--Encuentra el título de todas las películas que son ‘PG13ʼ o tienen una
--duración mayor a 3 horas en la tabla film.

select title, release_year, length, rating
from film
where length >= 180 or rating ='PG-13'
order by length asc


--Encuentra la variabilidad de lo que costaría reemplazar las películas.

select min(replacement_cost) minimo, max(replacement_cost) maximo, avg(replacement_cost) media
from film

--Encuentra la mayor y menor duración de una película de nuestra BBDD.

SELECT min(length) duracion_minima, max(length) duracion_maxima
from film

--Encuentra lo que costó el antepenúltimo alquiler ordenado por día.

SELECT RENTAL_ID , AMOUNT, PAYMENT_DATE 
FROM payment
order BY PAYMENT_DATE DESC 
limit 3

--Encuentra el título de las películas en la tabla “filmˮ que no sean ni ‘NC
--17ʼ ni ‘Gʼ en cuanto a su clasificación.

SELECT title, rating
from FILM AS F 
where rating !='NC-17' AND Rating!='G'
order by RATING 


--Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.
select round(avg(length),2) promedio_duracion, rating
from film
group by rating

--Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.

select title, length, rating
from film
where length >= 180
order by length

--¿Cuánto dinero ha generado en total la empresa?

SELECT sum(amount) ingresos_totales
from payment

--Muestra los 10 clientes con mayor valor de id.


SELECT customer_id, concat(first_name, ' ',last_name), case when active =1 then 'activo' else 'inactivo' end as cliente_activo
from customer
ORDER BY CUSTOMER_ID DESC 
limit 10

--Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igbyʼ.

select film.TITLE pelicula, film_actor.ACTOR_ID, concat(actor.first_name, ' ', actor.last_name) Actores
from film
JOIN film_actor on film.FILM_ID = FILM_ACTOR.FILM_ID 
JOIN actor on film_actor.ACTOR_ID = actor.ACTOR_ID 
where film.TITLE =upper('Egg Igby')

-- Selecciona todos los nombres de las películas únicos.

select distinct(title) titulo, rating, length
from film
order BY title asc

--Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla “filmˮ.

SELECT title titulo, length duracion, category.name categoria
from film
join film_category on film.FILM_ID = film_category.FILM_ID 
join category on film_category.category_id = category.category_id 
where category.name ='Comedy' and length>180


--Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos 
--y muestra el nombre de la categoría junto con el promedio de duración.

SELECT category.name categoria, round(AVG(length),2) Promedio_duracion
FROM film
JOIN film_category ON film.FILM_ID = film_category.FILM_ID 
JOIN category ON film_category.category_id = category.category_id 
GROUP BY category.CATEGORY_ID 
HAVING AVG(length)>110
ORDER BY category.name

--¿Cuál es la media de duración del alquiler de las películas?

SELECT AVG(rental_duration) media_renta
FROM film

--Crea una columna con el nombre y apellidos de todos los actores y actrices.

SELECT concat(first_name,' ', last_name)
FROM actor
ORDER BY first_name

--Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.

SELECT count(rental_id) cantidad_alquiler, date(rental_date) dia
FROM rental
GROUP BY dia
ORDER BY dia DESC 

--Encuentra las películas con una duración superior al promedio.

SELECT title, length
FROM film
WHERE length > (SELECT AVG(length) FROM film) 

--Averigua el número de alquileres registrados por mes.

SELECT count(rental_id) Alquileres_mes, date(date_trunc('month',RENTAL_DATE)) fecha
FROM rental
GROUP BY fecha

--Encuentra el promedio, la desviación estándar y varianza del total pagado.

SELECT avg(amount) promedio, STDDEV(amount) std_dev, variance(amount) viarianza
FROM payment

--¿Qué películas se alquilan por encima del precio medio?

SELECT title, p.AMOUNT 
FROM film
JOIN INVENTORY AS I ON film.FILM_ID = I.FILM_ID 
JOIN RENTAL AS R ON i.INVENTORY_ID = r.INVENTORY_ID 
JOIN PAYMENT AS P ON r.RENTAL_ID = p.RENTAL_ID 
WHERE p.AMOUNT > (SELECT avg(AMOUNT) FROM payment)

--Muestra el id de los actores que hayan participado en más de 40 películas.

SELECT fa.actor_id, count(FILM_ID), concat(FIRST_NAME,' ',LAST_NAME)
FROM film_actor as fa
JOIN actor ON actor.ACTOR_ID = fa.ACTOR_ID
GROUP BY fa.ACTOR_ID,actor.FIRST_NAME, actor.LAST_NAME
ORDER BY fa.ACTOR_ID

--Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.

SELECT I.FILM_ID,f.title ,count(I.INVENTORY_ID)
FROM INVENTORY AS I
JOIN FILM AS F ON i.FILM_ID =f.FILM_ID 
GROUP BY i.FILM_ID, f.title
ORDER BY i.FILM_ID  

--Obtener los actores y el número de películas en las que ha actuado.

SELECT concat(first_name,' ', last_name), count(fa.FILM_ID)
FROM actor AS a
JOIN FILM_ACTOR AS FA ON a.ACTOR_ID =fa.ACTOR_ID 
GROUP BY a.first_name, a.LAST_NAME 
ORDER BY first_name

--Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.

SELECT f.TITLE, concat(ac.FIRST_NAME,' ', ac.LAST_NAME)
FROM film AS f 
JOIN film_actor AS fa ON f.FILM_ID = fa.FILM_ID 
JOIN actor AS ac ON ac.ACTOR_ID = fa.ACTOR_ID 
ORDER BY f.title

--Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.

SELECT concat(a.FIRST_NAME,' ' ,a.LAST_NAME), f.title
FROM ACTOR AS a
JOIN FILM_ACTOR AS fa ON a.ACTOR_ID = fa.ACTOR_ID 
JOIN FILM AS f ON f.FILM_ID = fa.FILM_ID
ORDER BY a.FIRST_NAME, f.title

--Obtener todas las películas que tenemos y todos los registros de alquiler.

SELECT count(FILM_ID)  total_peliculas, (SELECT count(rental_id) total_alquileres FROM RENTAL)
FROM FILM

--Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.

SELECT SUM(p.amount) gastado, r.customer_id ID, concat(c.FIRST_NAME, ' ', c.LAST_NAME ) nombre_cliente
FROM RENTAL AS R 
JOIN PAYMENT AS P ON p.CUSTOMER_ID = r.CUSTOMER_ID 
JOIN CUSTOMER AS C ON R.CUSTOMER_ID = C.CUSTOMER_ID
GROUP BY r.CUSTOMER_ID, c.FIRST_NAME, c.LAST_NAME 
ORDER BY sum(p.amount) DESC
LIMIT 5

--Selecciona todos los actores cuyo primer nombre es 'Johnny'.

SELECT concat(a.FIRST_NAME,' ', a.LAST_NAME) nombre
FROM ACTOR AS A  
WHERE a.FIRST_NAME ='JOHNNY'

--Renombra la columna “first_nameˮ como Nombre y “last_nameˮ como Apellido.

ALTER TABLE ACTOR 
RENAME COLUMN FIRST_NAME  TO NOMBRE;
ALTER TABLE ACTOR 
RENAME COLUMN LAST_NAME TO APELLIDO;

--Cuenta cuántos actores hay en la tabla “actorˮ.

SELECT count(actor_id)
FROM ACTOR AS A 

--Selecciona todos los actores y ordénalos por apellido en orden ascendente.

SELECT nombre, apellido
FROM ACTOR AS A 
ORDER BY APELLIDO ASC 

--Selecciona las primeras 5 películas de la tabla “filmˮ.

SELECT title
FROM FILM AS F 
ORDER BY F.FILM_ID 
LIMIT 5

--Agrupa los actores por su nombre y cuenta cuántos actores tienen el
--mismo nombre. ¿Cuál es el nombre más repetido?

SELECT count(nombre), nombre
FROM ACTOR AS A 
GROUP BY NOMBRE 
ORDER BY count(nombre) DESC 

--Encuentra todos los alquileres y los nombres de los clientes que los realizaron.

SELECT r.RENTAL_ID id_Alquiler,c.CUSTOMER_ID ID_cliente, concat(c.FIRST_NAME ,' ',c.LAST_NAME ) nombre, f.FILM_ID ,f.TITLE titulo 
FROM RENTAL AS R 
JOIN INVENTORY AS I ON R.INVENTORY_ID = I.INVENTORY_ID
JOIN CUSTOMER AS C ON R.CUSTOMER_ID = C.CUSTOMER_ID
JOIN FILM AS F ON I.FILM_ID = F.FILM_ID
ORDER BY r.RENTAL_ID

--Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.

SELECT concat(c.FIRST_NAME,' ', c.LAST_NAME) nombre, count(r.RENTAL_ID) recuento_alquileres
FROM CUSTOMER AS C 
JOIN RENTAL AS R ON C.CUSTOMER_ID = R.CUSTOMER_ID
GROUP BY c.FIRST_NAME, c.LAST_NAME 
ORDER BY count(R.RENTAL_ID) ASC

--Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor
--esta consulta? ¿Por qué? Deja después de la consulta la contestación.

SELECT F.TITLE, c."name" 
FROM FILM AS F 
CROSS JOIN FILM_CATEGORY AS FC
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
ORDER BY f.TITLE 
/* Un cross join no aporta valor en este caso, ya que mezclaria los titulos de las peliculas con categorias a las que no corresponde
un Join normal si aportaria valor ya que podemos utilizar el atributo "name" de la tabla category para visual mejor la categoria
 */ 

--Encuentra los actores que han participado en películas de la categoría 'Action'.

SELECT concat(a.NOMBRE,' ',a.APELLIDO ) actor, c."name" categoria
FROM FILM AS F 
JOIN FILM_CATEGORY AS FC ON fc.FILM_ID = f.FILM_ID 
JOIN CATEGORY AS C ON c.CATEGORY_ID =fc.CATEGORY_ID 
JOIN FILM_ACTOR AS FA ON f.FILM_ID =fa.FILM_ID 
JOIN ACTOR AS A ON FA.ACTOR_ID = A.ACTOR_ID
WHERE c."name" ='Action'
ORDER BY A.NOMBRE

--Encuentra todos los actores que no han participado en películas.

SELECT concat(a.NOMBRE,' ',a.APELLIDO) actor, count(FA.FILM_ID) recuento_peliculas
FROM ACTOR AS A
JOIN FILM_ACTOR AS FA ON A.ACTOR_ID = FA.ACTOR_ID
GROUP BY a.NOMBRE ,a.APELLIDO 
HAVING COUNT(fa.FILM_ID)<1

--Selecciona el nombre de los actores y la cantidad de películas en las que han participado.


SELECT concat(a.NOMBRE,' ',a.APELLIDO) Actor, count(FA.FILM_ID) cantidad_peliculas
FROM ACTOR AS A
JOIN FILM_ACTOR AS FA ON A.ACTOR_ID = FA.ACTOR_ID
GROUP BY a.NOMBRE ,a.APELLIDO 
ORDER BY count(fa.FILM_ID) ASC 

--Crea una vista llamada “actor_num_peliculasˮ que muestre los nombres
--de los actores y el número de películas en las que han participado.

CREATE VIEW actor_num_peliculas AS
SELECT concat(a.NOMBRE,' ',a.APELLIDO) Actor, count(FA.FILM_ID) cantidad_peliculas
FROM ACTOR AS A
JOIN FILM_ACTOR AS FA ON A.ACTOR_ID = FA.ACTOR_ID
GROUP BY a.NOMBRE ,a.APELLIDO 

--Calcula el número total de alquileres realizados por cada cliente.

SELECT concat(c.FIRST_NAME,' ',c.LAST_NAME) cliente, count(r.RENTAL_ID) recuento_alquileres
FROM RENTAL AS R
JOIN CUSTOMER AS C ON c.CUSTOMER_ID = r.CUSTOMER_ID 
GROUP BY c.FIRST_NAME,c.LAST_NAME 
ORDER BY count(r.RENTAL_ID)

--Calcula la duración total de las películas en la categoría 'Action'.

SELECT sum(f.LENGTH) suma_duracion, AVG(f.LENGTH) promedio_duracion, c."name" categoria, count(f.FILM_ID) recuento_peliculas
FROM FILM AS F 
JOIN FILM_CATEGORY AS FC ON F.FILM_ID = FC.FILM_ID
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
WHERE c."name" ='Action'
GROUP BY c."name" 

--Crea una tabla temporal llamada “cliente_rentas_temporalˮ para
--almacenar el total de alquileres por cliente.

CREATE TEMPORARY TABLE cliente_rentas_temporal as 
SELECT count(r.rental_id), r.customer_id
FROM rental AS R
GROUP BY r.customer_id

--Crea una tabla temporal llamada “peliculas_alquiladasˮ que almacene las
--películas que han sido alquiladas al menos 10 veces.

CREATE TEMPORARY TABLE peliculas_alquiladas AS
SELECT count(r.RENTAL_ID) cantidad_alquileres , f.TITLE titulo 
FROM RENTAL AS R 
JOIN INVENTORY AS I ON r.inventory_id = i.INVENTORY_ID 
JOIN FILM AS F ON I.FILM_ID = F.FILM_ID
GROUP BY f.title
ORDER BY count(r.RENTAL_ID) DESC

--Encuentra el título de las películas que han sido alquiladas por el cliente
--con el nombre ‘Tammy Sandersʼ y que aún no se han devuelto. Ordena
--los resultados alfabéticamente por título de película.

SELECT r.RENTAL_ID, f.TITLE, f.REPLACEMENT_COST, c.CUSTOMER_ID, concat(c.FIRST_NAME,' ', c.LAST_NAME)
FROM RENTAL AS R 
JOIN INVENTORY AS I ON R.INVENTORY_ID = I.INVENTORY_ID
JOIN FILM AS F ON I.FILM_ID = F.FILM_ID
JOIN CUSTOMER AS C ON R.CUSTOMER_ID = C.CUSTOMER_ID
WHERE c.FIRST_NAME ='TAMMY' AND c.LAST_NAME ='SANDERS' AND r.RETURN_DATE IS NULL 
ORDER BY f.title

--Encuentra los nombres de los actores que han actuado en al menos una
--película que pertenece a la categoría ‘Sci-Fiʼ. Ordena los resultados
--alfabéticamente por apellido.

SELECT CONCAT (A.NOMBRE ,' ',A.APELLIDO ) actor, c."name" categoria, count(a.NOMBRE) cantidad_peliculas
FROM FILM AS F 
JOIN FILM_ACTOR AS FA ON F.FILM_ID = FA.FILM_ID
JOIN ACTOR AS A ON FA.ACTOR_ID = A.ACTOR_ID
JOIN FILM_CATEGORY AS FC ON F.FILM_ID = FC.FILM_ID
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
WHERE c."name"='Sci-Fi'
GROUP BY a.nombre,a.APELLIDO,c."name" 
ORDER BY a.nombre,a.APELLIDO 

--Encuentra el nombre y apellido de los actores que han actuado en
--películas que se alquilaron después de que la película ‘Spartacus
--Cheaperʼ se alquilara por primera vez. Ordena los resultados
--alfabéticamente por apellido.

SELECT CONCAT(a.NOMBRE,' ',a.APELLIDO) actor, f.title --nombre
FROM ACTOR AS A 
JOIN FILM_ACTOR AS FA ON A.ACTOR_ID = FA.ACTOR_ID 
JOIN FILM AS F ON FA.FILM_ID = F.FILM_ID 
JOIN INVENTORY AS I ON i.FILM_ID = f.FILM_ID 
JOIN RENTAL AS R ON I.INVENTORY_ID = R.INVENTORY_ID 
WHERE r.RENTAL_DATE > (--1 alquiler
	SELECT r2.RENTAL_DATE
	FROM RENTAL AS R2 
	JOIN INVENTORY AS I2 ON r2.INVENTORY_ID = I2.INVENTORY_ID 
	JOIN FILM AS F2 ON I2.FILM_ID = F2.FILM_ID
	WHERE F2.TITLE =upper('Spartacus Cheaper')
	ORDER BY r2.RENTAL_DATE ASC
	LIMIT 1)--solo un valor
GROUP BY f.title,a.nombre,a.APELLIDO --simplificado
order by a.apellido --oreden

--Encuentra el nombre y apellido de los actores que no han actuado en
--ninguna película de la categoría ‘Musicʼ.

SELECT  concat(a.NOMBRE,' ',a.APELLIDO)  --nombre actor
FROM FILM AS F 
JOIN FILM_CATEGORY AS FC ON F.FILM_ID = FC.FILM_ID
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
JOIN FILM_ACTOR AS FA ON F.FILM_ID = FA.FILM_ID
JOIN ACTOR AS A ON FA.ACTOR_ID = A.ACTOR_ID
WHERE c."name" != 'Music' --categoria
GROUP BY a.NOMBRE ,a.APELLIDO 

--Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.

SELECT f.title
FROM RENTAL AS R 
JOIN INVENTORY AS I ON R.INVENTORY_ID = I.INVENTORY_ID 
JOIN FILM AS F ON I.FILM_ID = F.FILM_ID 
WHERE date_part('day', r.return_date - r.rental_date) > 8

--Encuentra el título de todas las películas que son de la misma categoría que ‘Animationʼ.

SELECT f.TITLE 
FROM FILM AS F 
JOIN FILM_CATEGORY AS FC ON F.FILM_ID = FC.FILM_ID
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
WHERE c."name" ='Animation'

--Encuentra los nombres de las películas que tienen la misma duración
--que la película con el título ‘Dancing Feverʼ. Ordena los resultados
--alfabéticamente por título de película.

SELECT f.TITLE, f.LENGTH 
FROM FILM AS F 
WHERE f.LENGTH = (
	SELECT f2.length 
	FROM FILM AS F2 
	WHERE f2.TITLE =upper('Dancing fever'))
	
--Encuentra los nombres de los clientes que han alquilado al menos 7
--películas distintas. Ordena los resultados alfabéticamente por apellido.

SELECT c.FIRST_NAME, count(r.RENTAL_ID)
FROM RENTAL AS R 
JOIN CUSTOMER AS C ON r.customer_id = c.customer_id
GROUP BY c.FIRST_NAME 
HAVING count(r.RENTAL_ID)>=7
ORDER BY count(r.RENTAL_ID) ASC

--Encuentra la cantidad total de películas alquiladas por categoría y
--muestra el nombre de la categoría junto con el recuento de alquileres.

SELECT c."name", count(r.RENTAL_ID) cantidad_alquilada
FROM RENTAL AS R 
JOIN INVENTORY AS I ON i.INVENTORY_ID = r.INVENTORY_ID 
JOIN FILM AS F ON I.FILM_ID = F.FILM_ID
JOIN FILM_CATEGORY AS FC ON F.FILM_ID = FC.FILM_ID
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
GROUP BY c.name
ORDER BY c.name

--Encuentra el número de películas por categoría estrenadas en 2006.

SELECT c."name", count(f.FILM_ID) recuento_peliculas 
FROM FILM AS F 
JOIN FILM_CATEGORY AS FC ON f.FILM_ID = fc.FILM_ID 
JOIN CATEGORY AS C ON FC.CATEGORY_ID = C.CATEGORY_ID
WHERE f.RELEASE_YEAR = 2006
GROUP BY c."name" 
ORDER BY c."name"

--Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.

SELECT S.staff_id, S.first_name, S.last_name, ST.store_id
FROM STAFF AS S
CROSS JOIN  STORE AS ST;

--Encuentra la cantidad total de películas alquiladas por cada cliente y
--muestra el ID del cliente, su nombre y apellido junto con la cantidad de
--películas alquiladas. 

SELECT c.customer_id id_cliente, concat(c.FIRST_NAME,' ',c.LAST_NAME) cliente, count(r.RENTAL_ID) recuento_alquileres
FROM RENTAL AS R 
JOIN CUSTOMER AS C ON c.CUSTOMER_ID = r.CUSTOMER_ID 
GROUP BY c.CUSTOMER_ID, c.FIRST_NAME, c.LAST_NAME 