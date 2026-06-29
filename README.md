# qa-automation-engineer-api-course

## Install requirements

```shell
pip install -r requirements.txt
```

## Create `.env` file

To get started with the project, you need to create a `.env` file in the root of the project directory. This file will
store sensitive environment variables such as database credentials and JWT settings.

### Step-by-Step Guide:

#### 1. Create a .env File:

In your project root directory, create a file named .env.

```shell
touch .env
```

#### 2. Add the Required Variables:

Copy and paste the following environment variables into the `.env` file:

```shell
APP_HOST="http://localhost:8000"

DATABASE_URL="sqlite+aiosqlite:///./local.db"

JWT_ALGORITHM="HS256"
JWT_SECRET_KEY="qa-automation-engineer-api-course-secret-key"
JWT_ACCESS_TOKEN_EXPIRE=1800
JWT_REFRESH_TOKEN_EXPIRE=5184000
```

## Run server

```shell
uvicorn main:app --reload
```

##
link - http://localhost:8000/docs#/

## Docker
```powershell
docker build -t test_stepik_course .

docker run --rm -d -p 8082:8000 `
  -e APP_HOST=http://localhost:8082 `
  -e DATABASE_URL=sqlite+aiosqlite:///./local.db `
  -e JWT_ALGORITHM=HS256 `
  -e JWT_SECRET_KEY=qa-automation-engineer-api-course-secret-key `
  -e JWT_ACCESS_TOKEN_EXPIRE=1800 `
  -e JWT_REFRESH_TOKEN_EXPIRE=5184000 `
  -v I:\it_fork\DB\db_engineer:/data `
  test_stepik_course
```
или у меня ИЛИ
```powershell
docker pull bezobrazieq/test_stepik_course:latest

docker run --rm -d -p 8000:8000 `
  -e APP_HOST=http://localhost:8000 `
  -e DATABASE_URL=sqlite+aiosqlite:////data/local.db `
  -e JWT_ALGORITHM=HS256 `
  -e JWT_SECRET_KEY=automation-engineer-api-course-secret-key `
  -e JWT_ACCESS_TOKEN_EXPIRE=1800 `
  -e JWT_REFRESH_TOKEN_EXPIRE=5184000 `
  -v I:\it_fork\DB\db_engineer:/data `
  bezobrazieq/test_stepik_course:latest
```
```
мои настройки 1 варианта Димы
docker build . -t api_dd

docker run --name web_dd -d -p 8082:8000 -e APP_HOST=http://localhost:8082 -e DATABASE_URL=sqlite+aiosqlite:////data/api_dd.db -e JWT_ALGORITHM=HS256 -e JWT_SECRET_KEY=qa-automation-engineer-api-course-secret-key -e JWT_ACCESS_TOKEN_EXPIRE=1800 -e JWT_REFRESH_TOKEN_EXPIRE=5184000 -v I:\it_fork\DB\db_engineer:/data api_dd

## link - http://localhost:8082/docs#/

инфо: DATABASE_URL=sqlite+aiosqlite:///./api_dd.db - api_dd.db- файл с базой бд (DB/db_engineer)
```