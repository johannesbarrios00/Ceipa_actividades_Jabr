¿Qué pasa si agregamos 10 tipos de transacciones?
Si seguimos con este estilo y nos piden manejar 10 tipos distintos, el código se volvería un desorden total. Imagina tener que meterle a la función calcular_monto_total diez if seguidos para aplicar las reglas de cada tipo. El archivo se haría gigante, difícil de leer y muy frágil cada vez que queramos modificar algo o agregar un tipo número 11.

¿Por qué separar los datos de la lógica es una pesadilla para hacer debugging?
El problema de tener la información (el diccionario) por un lado y las funciones por el otro, es como pasar un cheque firmado de mano en mano por toda una oficina:

Alguien lo va a arruinar y no sabrás quién: Como los datos viajan "sueltos" de función en función, cualquier parte del código puede alterar un monto o borrar un cliente por accidente. Cuando el programa falle al final, te vas a volver loco revisando todas las funciones para descubrir cuál de todas dañó la información original.

Los datos no saben defenderse: Si una función le mete un monto negativo o texto en lugar de números, el diccionario simplemente lo acepta. Tendrías que escribir código de validación repitiéndolo en cada función externa que toque el dato.

Si cambias algo, todo se rompe: Si mañana decides que la variable monto se debe llamar valor, tienes que ir a buscar y cambiar esa palabra en todas y cada una de las funciones que la usan. Si se te olvida actualizar una sola, el programa colapsa y te toca rastrear el error desde cero.

Al pasar a Programación Orientada a Objetos, el dato (monto) y su comportamiento (las reglas de cómo usarlo) viven juntos bajo el mismo techo (la Clase). Si hay un error con el monto, ya sabes exactamente a qué única puerta ir a tocar para arreglarlo, lo que hace el debugging muchísimo más fácil.
