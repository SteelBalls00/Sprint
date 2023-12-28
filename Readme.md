# Rest API для ФСТР
![Изображение](https://avatars.mds.yandex.net/i?id=666d6e5b74b723a62694e6a80218a35f9ef04b43-9858868-images-thumbs&n=13)

**[Данный проект опубликован на pythonanywhere.com](http://steelballs00.pythonanywhere.com)**
## 1. Описание и задача


***
Федерации Спортивного Туризма России (ФСТР) ведёт базу горных перевалов, которая пополняется туристами.

После преодоления очередного перевала, турист заполняет отчёт в формате PDF и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает эту информацию, верифицирует, а затем вносит её в базу, которая ведётся в Google-таблице.
Весь процесс очень неудобный и долгий и занимает в среднем от 3 до 6 месяцев.
***
ФСТР заказала разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.
***
### Требовалось разработать REST API, которое будет обслуживать мобильное приложение.

##### Для пользователя в мобильном приложении доступны следующие действия:

- Внесение информации о новом объекте (перевале) в карточку объекта.
- Редактирование в приложении неотправленных на сервер ФСТР данных об объектах, 
на перевале не всегда работает Интернет.
- Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим 
их автозаполнением при внесении данных о новых объектах.
- Отправка данных на сервер ФСТР.
- Получение уведомления о статусе отправки (успешно/неуспешно).
- Согласие пользователя с политикой обработки персональных данных в случае 
нажатия на кнопку «Отправить» при отправке данных на сервер.

##### Пользователь с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:

- данные о пользователе: ФИО, телефон и email;
- название перевала и его описание;
- координаты перевала, его высота и сложность восхождение в разное время года;
- несколько фотографий перевала.

## 2. Методы используемые в Rest API

После ввода данных турист нажимает кнопку «Отправить» в мобильном приложении.
Мобильное приложение вызовет метод submitData REST API.

```sh
Метод POST submitData
```
![Изображение](https://downloader.disk.yandex.ru/preview/493bdd6c691286b2e5a01de313cdc3378e4b239a64e5fa1a363090c80d127e41/658d5812/WntvEQQkcB8kuKGSUgiB0lWpxrcJqDDJFNxdjztAP8S4d_6IudauT3wMRoDoMklTCn6BGPw1MpNx7Rtw0pNAOA%3D%3D?uid=0&filename=Screen_5_main.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

Метод submitData принимает JSON в теле запроса с информацией о перевале. Ниже находится пример такого JSON-а:
```python
{
    "beauty_title": "	Белухинсний перевал",
    "title": "Белухинсний перевал (через вершину В. Белуха)",
    "other_titles": "Белуха",
    "connect": "", // что соединяет, текстовое поле
    "level": {
        "summer": "3B",
        "autumn": "3B",
        "winter": "3B",
        "spring": "3B"
    },
    "user": {
        "fam": "Грозный",
        "name": "Иван",
        "otc": "Васильевич",
        "email": "cometome@son.ru",
        "phone": "81234567890"
    },
    "coord": {
        "latitude": "49°48’8"N",
        "longitude": "86°35’25"E",
        "height": 4506
    },
    "images": [{"title": "Восхождение на Белуху через перевал Делоне", "image": "<изображение1>"},
    {"title": "Взгляд новичка или Белуха в марте", "image": "<изображение2>"}]
}
```

**Результат метода: JSON**

 - **status** — код HTTP, целое число:
   - 500 — ошибка при выполнении операции;
   - 400 — Bad Request (при нехватке полей);
   - 200 — успех.
 - **message** — строка:
   - Причина ошибки (если она была);
   - Отправлено успешно;
   - Если отправка успешна, дополнительно возвращается id вставленной записи.
 - **id** — идентификатор, который был присвоен объекту при добавлении в базу данных.

**Примеры:**
 - { "status": 500, "message": "Ошибка подключения к базе данных","id": null}
 - { "status": 200, "message": null, "id": 42 }


![Изображение](https://downloader.disk.yandex.ru/preview/83cf3c3369888ae227a68f81b4ad235dbc76449bbc061c486609c2f401fe3a25/658d58e9/5YULNw7G7CegYfm0OThhxVWpxrcJqDDJFNxdjztAP8RvMmBML66anG0Gf3aP1eaz65yk_-_zKNqpdyD6EXCnsw%3D%3D?uid=0&filename=Screen_1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

  После добавления в БД информации о новом перевале, со временем производится модерация нового объекта и изменяется его поле  **status**.
 
Допустимые значения поля status:
 - new;
 - pending — если модератор взял в работу;
 - accepted — модерация прошла успешно;
 - rejected — модерация прошла, информация не принята.
***

**Получение информации по одной записи:**
 ```sh
Метод GET /submitData/<id>
```
 ***
**Редактирование информации по одной записи:**
 ```sh
Метод PATCH /submitData/<id>
```
Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона.
Метод принимает тот же самый json, который принимал метод POST submitData.

В качестве результата возвращается два значения:
 - **state**:
    - 1 — если успешно удалось отредактировать запись в базе данных.
    - 0 — в противном случае.
 - **message** - результат обновления.

Например:

**Изменения применены**
![Изображение](https://downloader.disk.yandex.ru/preview/ec163d4788011a7687540b89338363e26272ac7ff498714e19e1141c420d3a34/658d5915/hXnybMLc1DuQ6UQXfJCdTVWpxrcJqDDJFNxdjztAP8SOlhgsHLu8FOQPCXsz_JvjXb3XzqtWPwWqptlJQBL3hA%3D%3D?uid=0&filename=Screen_2_good_upd.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
**Попытка изменения данных пользователя**
![Изображение](https://downloader.disk.yandex.ru/preview/54b5d8f5e87f534a43d0f95a124225f32066918c3741865a809695ced7e9b083/658d5934/fABuc57BkqdWw1Ic8vLuKlWpxrcJqDDJFNxdjztAP8T6lznGKh6TQLZ34XFveSCBsNyWv2wZar6sNmtyJtRJYg%3D%3D?uid=0&filename=Screen_3_user_change.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
**Попытка изменения со статусом, отличным от new**
![Изображение](https://downloader.disk.yandex.ru/preview/eadc42e98af3d503320ec2c05d8578aed2457b277e2f7037edc82e9437f63e51/658d595a/SPvEoDWm0KTHDmklFlXWP1WpxrcJqDDJFNxdjztAP8RtnVsAKwmILGU-m1J6jTydFaVpset4T5FSIEw9YO3NHg%3D%3D?uid=0&filename=Screen_4_not_new.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
***

**Получение данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер**
 ```sh
Метод GET /submitData/?user__email=<email>
```
Есть возможность фильтровать перевалы по нескольким полям, в том числе по e-mail.
![Изображение](https://downloader.disk.yandex.ru/preview/19f336a6986b18008267126652abde00e9bfb98e694e50ed8a1d8f6a001643d4/658d5973/MCmYfjfVm5eqLcopcSUqQrpwx0m54kMp3ZXvxpfi7FeO0xZx9XpG8S6lDaWhdveA3K1_drxPdYxMZxOWArW4Sg%3D%3D?uid=0&filename=Screen_6_filters.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
***

Схема для [swagger](http://steelballs00.pythonanywhere.com/swagger-ui/) сгенерирована с использованием **pyyaml** и **uritemplate**.

