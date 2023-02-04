# yatube-project

## Описание проекта: 

•	**Назначение:** 

Вторая версия социальной сети для публикации личных дневников. 

•	**Реализованный функционал:** 

1. Подключена база данных
2. Десять последних записей выводятся на главную страницу
3. В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие
4. Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы

•	**Цель выполнения проекта:**

Практика работы с фреймворком Django,БД,Админ-панелью

•	**Стек:**

Python 3.7, Django 2.2.19, SQLite, pytest

## Инструкция по развёртыванию проекта

•	**Клонируйте репозиторий:**

```csharp 
git clone git@github.com:antsakharov/yatube_project.git
```

•	**Установите и активируйте виртуальное окружение:**

**для Linux и MacOS**

```csharp 
python3 -m venv venv
```

**для Windows**

```csharp 
python -m venv venv
```

```csharp 
source venv/bin/activate
```

```csharp 
source venv/Scripts/activate
```

•	**Установите зависимости из файла requirements.txt:**

```csharp 
pip install -r requirements.txt
```
•	**Создайте и выполните миграции:**

```csharp 
python manage.py makemigrations
```

```csharp 
python manage.py migrate
```

