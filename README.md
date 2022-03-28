# Apache-Airflow

## Environments
- **Language:**
  - Python 3.9
- **Framework:**
  - Airflow 2.2.4
- **Database:**
  - PostrgreSQL 12.7

# 1. Quick Start

## 1.1 라이브러리 설치

기본적으로 poetry 를 이용하여 라이브러리의 dependency 를 관리합니다.

```bash
$> virtualenv -p python3.9 .venv
$> source .venv/bin/activate
$> poetry install
```

## 1.2 환경 변수

기본적으로 PostgreSQL 기준으로 작성되었습니다.

```bash
$> cp .env.example .env
$> vim .env

# === Dotenv Files === #

# - Databases
AIRFLOW_DB_USER=
...
```

### 1.2.1 다른 DB 연동

PostgreSQL 이외에 다른 Database를 사용하는 경우 해당 DB 연동 라이브러리를 설치하고 `docker-compose.yml` 파일을 수정해주세요.

```bash
$> poetry add mysqlclient
```

```yml
# docker-compose.yml
    environment:
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: mysql://${AIRFLOW_DB_USER}:${AIRFLOW_DB_PASSWORD}@ ...
...
```

## 1.3 실행
```bash
docker-compose up -d
```

### 1.3.1 User 생성

초기 실행하는 경우 DB에 유저 정보를 입력합니다.

```bash
airflow users create \
    --username miintto \
    --firstname minjae \
    --lastname park \
    --role Admin \
    --email miintto.log@gmail.com
```
