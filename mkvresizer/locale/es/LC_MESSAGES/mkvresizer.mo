��          �   %   �      P  )   Q  3   {     �     �      �  ?   
     J      V  (   w     �  /   �  '   �  ,        .  R   J     �  k   �  *     0   A  7   r  |   �  %   '  ,   M  <   z      �  6  �  0     8   @  $   y      �  %   �  N   �     4	  .   A	  5   p	     �	  <   �	  3   �	  4    
  #   U
  _   y
     �
  g   �
  6   Q  >   �  @   �  �     -   �  4   �  C   �  #   8        	                                                                                                              
         * Change version and date in version.py   * Create a new gentoo ebuild with the new version   * Edit Changelog in README   * Make a new tag in github   * Upload to portage repository Change files and directories owner and permissions recursively. DESCRIPTION Database port. By default '5432' Database server. By default '127.0.0.1'. EXAMPLES Generate a book with all movies in the database Generates the movie collection document Insert films from current numbered directory Insert movies with index 23 Inserts a directory with movies with the index of the last directory numeric name. New Release: Path where the movie book it's going to be generated. You can use this parameter as many times as you want. Postgresql database connection parameters: This app has the following mandatory parameters: This command generates a movie book in the output path. This command insert in database all movies (up to 6) in 23 directory. Each film must have it's cover with the same filename. Uninstall command only works in Linux User of the database. By default 'postgres'. You can choose PDF or ODT arguments. PDF is used by default. You pressed 'Ctrl+C', exiting... Project-Id-Version: RecPermissions
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2018-10-22 18:51+0100
Last-Translator: root <turulomio@yahoo.es>
Language-Team: Spanish
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
   * Cambiar la versión y la fecha en version.py   * Crea un nuevo ebuild de Gentoo con la nueva versión   * Modificar el Changelog en README   * Hacer un nuevo tag en GitHub   * Subelo al repositorio del portage Cambia el propietario y los permisos de ficheros y directorios recursivamente. DESCRIPCIÓN Puerto de la base de datos. Por defecto '5432' Servidor de la base de datos. Por defecto '127.0.0.1' EJEMPLOS Genera un libro con todas las películas en la base de datos Genera el documento con la colección de películas Añade las películas del directorio numerado actual Añade películas con el índice 23 Añade un directorio con películas cuyo índice es el nombre numérico del último directorio. Nueva versión: Ruta donde se va a crear el libro de películas. Puedes usar este parámetro tantas veces como quieras. Parámetros de conexión a la base de datos Postgresql Esta aplicación tiene los siguientes parámetros obligatorios Este comando genera un libro de películas en la ruta de salida. Este comando añade a la base de datos hasta 6 películas del directorio 23. Cada película debe tener su carátula con el mismo nombre. El comando 'uninstall' solo funciona en Linux Usuario de la base de datos. Por defecto 'postgres'. Puedes elegir PDF ó ODT como argumentos. PDF es usado por defecto. Se ha pulsado 'Ctrl+C', saliendo... 