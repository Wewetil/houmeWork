# homeWork
Test task<br>

Для запуска необходимо поправить example-env на .env, указать в нем нужный порт<br>
Запускается ```docker-compose up -d --build``` <br>
Приложение service - принимает запросы и записывает файл с временем когда пришел запрос, затем в порядке очереди в котором пришли запросы записывает в файл время после sleep<br> 
Приложение client - посылает запросы на приложение srvice.
