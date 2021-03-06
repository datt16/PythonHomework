# TMS

----- **T**ask**M**anagement**S**ystem -----  
授業用課題のリポジトリです

![image](https://user-images.githubusercontent.com/44765362/119964123-d19ada00-bfe3-11eb-9796-d4057f1064ae.png)



## 概要

flask を用いてタスク管理アプリ用の api を作りました。
vuetify を使って ui も作ってみました。

## 使い方

```
 > cd backend
 > pip install -r requirements.txt
 > python3 app.py
```

## 仕様

- アプリの初期 url  
  http://127.0.0.1:5000/
  もしくは
  http://localhost:5000/

以下最初の `http://<hoge>:5000`はどちらでもアクセスできます。

- api の url  
   GET : http://127.0.0.1:5000/api/tasks  
   POST : http://127.0.0.1:5000/api/tasks  
   PUT : http://127.0.0.1:5000/api/tasks/[task:id]  
   DELETE : http://127.0.0.1:5000/api/tasks/[task:id]

POST、PUT はデータを一緒に送らないと動きません。

- データ形式

```
application/json" -d
'{
    "title":"String",       # タスクのタイトル
    "dueD":"String",        # タスクの期限(日付)
    "dueT":"String",        # タスクの期限(時刻)
    "priority": Integer,    # タスクの優先度(0~3)
    "description":"String", # タスクの説明
    "done": Integer         # タスクが完了済みかどうか(1,0)
}'
```

## 使用したライブラリ

**backend**

```
Flask==1.1.1
Flask-Cors==3.0.8
flask-marshmallow==0.10.1
Flask-SQLAlchemy==2.4.0
Jinja2==3.0.1
marshmallow==3.2.0
marshmallow-sqlalchemy==0.19.0
SQLAlchemy==1.3.23
```

**frontend**

```
node.js   v10.15.2
npm       5.8.0
```

```
vuetify  v2.0.0 (画面のデザインに使用、フレームワーク)
axios   v0.19.0 (自作のapiとの通信に使用)
```

## frontend フォルダーからの実行方法

```
 > cd frontend
 > npm install
 > npm run serve
```

**先に backend から app.py を実行しないと正しく動きません**
