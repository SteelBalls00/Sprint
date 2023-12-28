# Rest API ��� ����
[![N|Solid](https://avatars.mds.yandex.net/i?id=666d6e5b74b723a62694e6a80218a35f9ef04b43-9858868-images-thumbs&n=13)](https://nodesource.com/products/nsolid)

**[������ ������ ����������� �� pythonanywhere.com](http://steelballs00.pythonanywhere.com)**
## 1. �������� � ������


***
��������� ����������� ������� ������ (����) ���� ���� ������ ���������, ������� ����������� ���������.

����� ����������� ���������� ��������, ������ ��������� ����� � ������� PDF � ���������� ��� �� ����������� ����� ���������. ���������� ������ ���� �������� ��� ����������, ������������, � ����� ������ � � ����, ������� ������ � Google-�������.
���� ������� ����� ��������� � ������ � �������� � ������� �� 3 �� 6 �������.
***
���� �������� ����������� ��������� ���������� ��� Android � IOS, ������� ��������� �� �������� ������ �� �������� ������ � �������� � ��������� ����� ��������� ������� �� ��� ����.

������������ ��������� ����������� ����� �������. � ����� ��� ����� ������� ������ � �������� � ���������� � ���������� �� � ����, ��� ������ �������� ������ � ��������.

��������� �� ��������� ����� �������������� � ������� � ���� ������ ����������, ���������� �� �������������, � �� � ���� ������� ������ ������� � ��������� ���������� ������ ��������� � ������������� ���� � ���������, ��������� �������.
***
### ����������� ����������� REST API, ������� ����� ����������� ��������� ����������.

##### ��� ������������ � ��������� ���������� �������� ��������� ��������:

- �������� ���������� � ����� ������� (��������) � �������� �������.
- �������������� � ���������� �������������� �� ������ ���� ������ �� ��������, 
�� �������� �� ������ �������� ��������.
- ���������� ��� � ���������� ������ (������� � ����������� �����) � ����������� 
�� ��������������� ��� �������� ������ � ����� ��������.
- �������� ������ �� ������ ����.
- ��������� ����������� � ������� �������� (�������/���������).
- �������� ������������ � ��������� ��������� ������������ ������ � ������ 
������� �� ������ ����������� ��� �������� ������ �� ������.

##### ������������ � ������� ���������� ���������� ����� ���������� � ���� ��������� ������ � ��������:

- ������ � ������������: ���, ������� � email;
- �������� �������� � ��� ��������;
- ���������� ��������, ��� ������ � ��������� ����������� � ������ ����� ����;
- ��������� ���������� ��������.

## 2. ������ ������������ � Rest API

����� ����� ������ ������ �������� ������ ����������� � ��������� ����������.
��������� ���������� ������� ����� submitData REST API.

```sh
����� POST submitData
```
[![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_5_main.png)](https://nodesource.com/products/nsolid)
����� submitData ��������� JSON � ���� ������� � ����������� � ��������. ���� ��������� ������ ������ JSON-�:
```python
{
    "beauty_title": "	����������� �������",
    "title": "����������� ������� (����� ������� �. ������)",
    "other_titles": "������",
    "connect": "", // ��� ���������, ��������� ����
    "level": {
        "summer": "3B",
        "autumn": "3B",
        "winter": "3B",
        "spring": "3B"
    },
    "user": {
        "fam": "�������",
        "name": "����",
        "otc": "����������",
        "email": "cometome@son.ru",
        "phone": "81234567890"
    },
    "coord": {
        "latitude": "49�48�8"N",
        "longitude": "86�35�25"E",
        "height": 4506
    },
    "images": [{"title": "����������� �� ������ ����� ������� ������", "image": "<�����������1>"},
    {"title": "������ ������� ��� ������ � �����", "image": "<�����������2>"}]
}
```

**��������� ������: JSON**

 - **status** � ��� HTTP, ����� �����:
   - 500 � ������ ��� ���������� ��������;
   - 400 � Bad Request (��� �������� �����);
   - 200 � �����.
 - **message** � ������:
   - ������� ������ (���� ��� ����);
   - ���������� �������;
   - ���� �������� �������, ������������� ������������ id ����������� ������.
 - **id** � �������������, ������� ��� �������� ������� ��� ���������� � ���� ������.

**�������:**
 - { "status": 500, "message": "������ ����������� � ���� ������","id": null}
 - { "status": 200, "message": null, "id": 42 }


 [![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_1.png)](https://nodesource.com/products/nsolid)

  ����� ���������� � �� ���������� � ����� ��������, �� �������� ������������ ��������� ������ ������� � ���������� ��� ����  **status**.
 
���������� �������� ���� status:
 - new;
 - pending � ���� ��������� ���� � ������;
 - accepted � ��������� ������ �������;
 - rejected � ��������� ������, ���������� �� �������.
***

**��������� ���������� �� ����� ������:**
 ```sh
����� GET /submitData/<id>
```
 ***
**�������������� ���������� �� ����� ������:**
 ```sh
����� PATCH /submitData/<id>
```
������������� ����� ��� ����, ����� ���, ��� �������� � ���� ���, ����� ����� � ����� ��������.
����� ��������� ��� �� ����� json, ������� �������� ����� POST submitData.

� �������� ���������� ������������ ��� ��������:
 - **state**:
    - 1 � ���� ������� ������� ��������������� ������ � ���� ������.
    - 0 � � ��������� ������.
 - **message** - ��������� ����������.

��������:

**��������� ���������**
[![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_2_good_upd.png)](https://nodesource.com/products/nsolid)
**������� ��������� ������ ������������**
[![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_3_user_change.png)](https://nodesource.com/products/nsolid)
**������� ��������� �� ��������, �������� �� new**
[![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_4_not_new.png)](https://nodesource.com/products/nsolid)
***

**��������� ������ ��� ���� ��������, ������� ������������ � ������ <email> �������� �� ������**
 ```sh
����� GET /submitData/?user__email=<email>
```
���� ����������� ����������� �������� �� ���������� �����, � ��� ����� �� e-mail.
[![N|Solid](https://www.pythonanywhere.com/user/SteelBalls00/files/home/SteelBalls00/Sprint/media/Screen_6_filters.png)](https://nodesource.com/products/nsolid)
***

����� ��� [swagger](http://steelballs00.pythonanywhere.com/swagger-ui/) ������������� � �������������� **pyyaml** � **uritemplate**.

