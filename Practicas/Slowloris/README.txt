-h: esta opción especifica la dirección IP o el nombre de dominio del servidor al que se quiere realizar el ataque.

-p: esta opción especifica el puerto del servidor al que se quiere realizar el ataque.

-s: esta opción especifica el número de conexiones HTTP que se deben mantener abiertas sin completarse.

-t: esta opción especifica el tiempo que se debe esperar entre cada conexión HTTP.

-v: esta opción habilita el modo verboso, que muestra información adicional sobre el progreso del ataque.

--https: esta opción habilita el uso de conexiones HTTPS en lugar de HTTP.


slowloris <IP del servidor> -p <puerto del servidor>

slowloris 10.5.11.20 -p 80