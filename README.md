# 🫘 Daily Diet
System to register meals and control diet

## 🚀 Techs
Python, Flask, SQLAlchemy, SQLite


## 🛠️ Clone

To clone and run this application, you'll need Python installed on your computer.

📥 Clone the repository:

```bash
  git clone https://github.com/lucaslomba/DailyDiet.git
```

📂 Navigate to the project directory:

```bash
  cd DailyDiet
```

## 🛠️ Install dependencies

📥 Install using requirements.txt:

```bash
    pip3 install -r requirements.txt --upgrade
```

### Start project 

```bash
$ python3 app.py

```

## API Reference

### Login

```http
  POST api_url/login
```

Request body

```JSON
{
    "username": "string",
    "password": "string"
}
```

### Logout

```http
  GET api_url/logout
```

### Create user

```http
  POST api_url/user
```

Request body

```JSON
{
    "username": "string",
    "password": "string"
}
```

### Get all meals by user ID

```http
  GET /api/user/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. |

### Create meal

```http
  POST api_url/meal
```

Request body

```JSON
{
    "name": "string",
    "description": "string",
    "is_diet": "string"
}
```

### Update user by ID

```http
  PUT /api/meal/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. |

Request body

```JSON
{
    "name": "string",
    "description": "string",
    "is_diet": "string"
}
```

### Delete meal by ID

```http
  DELETE /api/meal/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. |


## Authors

- [@lucaslomba](https://github.com/lucaslomba)

