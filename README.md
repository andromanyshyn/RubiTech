
## Тестовое задание №1 - реализация функций и классов (ориентировочной время выполнения - 4 часа):
A. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на проекты на гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git). Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".

B. Реализовать функцию, принимающую два списка и возвращающую словарь (ключ из первого списка, значение из второго), упорядоченный по ключам. Результат вывести в консоль. Длина первого списка не должна быть равна длине второго. Результат вывести в консоль.

C. Реализовать функцию с помощью методов map и lambda. Функция принимает список элементов (состоящий из строк и цифр), возвращает новый список, с условием - если элемент списка был строкой, в начало строки нужно добавить текст "abc_", в конец строки - "_cba". Если элемент был int - то его значение нужно возвести в квадрат. Результат вывести в консоль.

D. Реализовать функцию, которая замеряет время на исполнение100 запросов к адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно. Допускается написание вспомогательных функций и использование сторонних библиотек. Результат замера времени выводит в консоль. Ожидаемое время не должно превышать 10 секунд.

E. Написать класс, принимающий на вход текст. Один метод класса должен выводить в консоль самое длинное слово в тексте. Второй метод - самое часто встречающееся слово. Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее). Четвертый метод выводит все палиндромы через запятую.

F. Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода. Результат выполнения задания должен быть оформлен в виде файла с кодом.

## Тестовое задание №2 - написать приложение на Django (ориентировочное время выполнения - 24 часа).
Описание приложения: приложение разрабатывается с помощью фреймворка Django, работает с базой данных SQLite, имеет API и веб интерфейсы. 

Цель приложения: каталогизация и структурирование информации по различным веб-ресурсам.

1.	API-интерфейс. Приложение принимает GET и POST запросы:
  a.	POST запрос №1 должен содержать в теле ссылку на какой-либо веб-ресурс. Приложение должно обработать полученную ссылку, разложить ее на протокол, домен, доменную зону и путь. Если в ссылке присутствуют параметры - преобразовать их в словарь. Полученные данные нужно сохранить в таблице базы данных, присвоив уникальный идентификационный номер (uuid). Возвращать пользователю ответ в формате json с разложенными данными и статусом обработки. Если пользователь прислал не ссылку - сообщать ему об этом в ответе.
  
  b.	POST запрос №2 должен содержать в себе csv файл с перечнем ссылок (формат файла - каждая новая строка одна ссылка). Все ссылки нужно обрабатывать по образцу POST запроса №1, а также обработка должна выполняться в фоновом режиме. В ответ добавить общий статус обработки файла (количество обрабатываемых ссылок, количество ошибок, количество ссылок, направленных на сохранение в БД).
  
  c.	GET запрос должен выводить все сохраненные ссылки из БД (добавить возможность выборки по доменной зоне, id, uuid).

## 2. Веб-интерфейс. Требуется реализовать 3 веб-страницы для приложения. 
При вёрстке страниц требуется использовать фреймворк Bootstrap5. Постараться выдержать единый концепт оформления страниц.

a.	Страница 1. Реализовать веб-страницу, содержащую формы для добавления в приложение новых веб-ресурсов. Формы должны добавлять веб-ресурсы как поштучно, так и загрузкой CSV файла. Формат CSV файла тот же, что и для API интерфейса.

b.	Страница 2. Реализовать веб-страницу с таблицей, отображающую все ссылки из базы данных с разбивкой на страницы (пагинация, по 10 элементов на страницу). Также веб-страница должна содержать элементы управления - поиск по доменному имени, возможность фильтрования по доменной зоне, а также удаление конкретного элемента из таблицы и базы данных соответственно.


## 3. Дистрибуция и контейнеризация.
Код приложения должен упаковываться в docker-контейнер и автоматически запускаться при старте контейнера.
