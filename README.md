# RESTful_API_Flask

**freestylo test task**


Функции названы однозначно, поэтому комментарии практически отсутствуют.  

3 конечные **точки**:
* **/login **[GET, POST]****
  * реализована с помощью класса PhonesCodes, присутствует проверка на валидность телефона
  * реализовано обновление получаемого кода для одного и того-же телефона
  * пары телефон-ключ хранятся в памяти
  * обработка ошибок минимальная, но присутствует
  * (не реализовано)для полноценной авторизации для доступа\запрета к функционалу нужно применять кэш-хранилище или БД
  * (работает) /login?phone=<телефон> GET запрос с номером телефона, в ответ должен прийти 6-значный код
  * (работает) /login POST запрос вида {"phone": "+71111111111", "code": "QWDCR4"} - в ответ должен прийти {"status": "OK"} если код верный и {"status": "Fail"} если код не верный. 
Можно хранить коды для авторизации в коде, не используя базу данных или кэш хранилища для этого

* **/structure [GET]**
  * реализована с помощью функций
  * обработка ошибок минимальная, но присутствует
  * валидация отсутствует
  * (работает) /structure GET запрос, В ответ должен прийти словарь с количеством каждого типа HTML-тэгов для сайта freestylo.ru
  * (работает) /structure?link=<ссылка> То же, что и выше, но теперь сайт задается в запросе
  * (работает) /structure?link=<ссылка>&tags=html,img То же что и выше, но теперь помимо ссылки задается массив тэгов через запятую, которые нужно вернуть в ответе
  
* **/check_structure **[POST]****
  * реализована с помощью функций
  * обработка ошибок минимальная, но присутствует
  * валидация отсутствует
  * (работает) /check_structure POST запрос вида  `{"link": "freestylo.ru", "structure": {"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}` 
Который для данный ссылки проверяет структуру html тэгов. В ответ должно приходить `{"is_correct": True}` если все верно и `{"is_correct": False, "difference": {"p": 2, "img": 1}}`  если есть ошибки, где difference - это разница структур. 


Примеры запросов в файле **rest-api.http**
