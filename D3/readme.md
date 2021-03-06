## Fullstack разработчик на Python

## [Веб-версия на Heroku](https://pyfs-d3.herokuapp.com/news/ 'Веб-версия на Heroku')

#  Модуль D3. Представления и шаблоны 

## **Проект** *News Portal*. **Итоговое задание**

### Описание проекта    

Иногда в новостях попадаются такие страсти, что диву даёшься. Некоторые фразы поражают воображение своей «этажностью».

Чтобы вдруг случайно не шокировать читателей вашего портала, забыв вырезать какие-то неприятные моменты, напишите фильтр, который будет убирать всю нецензурную брань в содержании и названии статей (так, на всякий случай), и примените его к названию и содержанию статьи.

В результате работы с модулем вы должны были выполнить следующие задания:

  1. Сделать новую страничку с адресом `/news/`, на которой должен выводиться список всех новостей.

  2. Все cтатьи выведены в виде заголовка, даты публикации и первых 50 символов текста статьи.
  Новости должны выводиться в порядке от более свежей до самой старой. Отображается всё по адресу `/news/`.

  3. Сделать отдельную страницу для полной информации о статье `/news/<id новости>`. На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате `ДЕНЬ-МЕСЯЦ-ГОД ЧАС:МИНУТЫ`.

  4. Написать собственный фильтр **Censor**, который цензурирует нежелательную лексику в названиях и текстах статей.

  5. Все новые странички должны быть частью основного шаблона `default.html`.


## Скриншот

### Без цензуры

![Без цензуры](./D3_.png)

### С цензурой

![С цензурой](./D3.png)
