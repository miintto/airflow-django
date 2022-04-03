<div align="center">
  <img src="https://user-images.githubusercontent.com/37063580/161375664-5494fe2f-e6d5-458d-a55c-61d5e3dae9f4.PNG" width="100">
  <img src="https://user-images.githubusercontent.com/37063580/161375744-b2d7dadd-085d-49db-87d2-e996257b5919.PNG" width="100">

</div>

# Airflow-Django

Apache-Airflow는 데이터 파이프 라인을 스케줄링 및 모니터링하는 오픈소스입니다. 
Django 내부에 비즈니스 로직이 강하게 엮여있어서 별도로 분리하기 힘든 경우 해당 프로세스를 Airflow에서 직접 실행하도록 구성였습니다.

## Environments
- **Language:**
  - Python 3.10
- **Framework:**
  - Airflow 2.2.4
  - Celery 5.1.2
  - Django 4.0
- **Container:**
  - Docker 20.10.10
- **Database:**
  - PostrgreSQL 12.7


# 1. Architecture

<img src="https://user-images.githubusercontent.com/37063580/161416452-98e31419-a244-4f0f-94a1-bce942ffa68e.png" width="600">

Airflow는 docker compose를 이용하여 구성하였고, `DockerOperator`를 이용하여 Django 컨테이너를 실행하도록 하였습니다.
`CeleryExecutor`를 사용하여 작업을 분산된 환경에서 실행 가능하도록 하였습니다.

# 2. Quick Start

## 2.1 환경 변수 설정

실행할 django 이미지 및 DB 접속 정보를 입력합니다.
기본적으로 PostgreSQL 기준으로 작성되었습니다.

```bash
$> cp .env.example .env
$> vim .env

# === Dotenv Files === #

# - Django
DJANGO_DEFAULT_IMAGE=django-app:latest
...
```

### 2.1.1 다른 DB 연동

PostgreSQL 이외에 다른 Database를 사용하는 경우 해당 DB 연동 라이브러리를 추가하고 `docker-compose.yml` 파일을 수정해주세요.

```bash
$> poetry add mysqlclient
```

```yml
# docker-compose.yml
    environment:
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: mysql://${AIRFLOW_DB_USER}:${AIRFLOW_DB_PASSWORD}@ ...
...
```

## 2.2 Airflow 실행

```bash
$> docker-compose up -d
```

### 2.2.1 User 생성

초기 실행하는 경우 DB에 유저 정보를 입력합니다.

```bash
$> airflow db init
$> airflow users create \
    --username miintto \
    --firstname Minjae \
    --lastname Park \
    --role Admin \
    --email miintto.log@gmail.com
```

## 2.3 Job 실행

### 2.3.1 Airflow Webserver 접속

localhost 혹은 실행된 서버 도메인의 8080번 포트로 접속합니다.

<img src="https://user-images.githubusercontent.com/37063580/161376967-361e54d8-57e2-4995-91c2-1aa50f3d74b6.png" width="1000">

### 2.3.2 Django 실행

실행할 Django 이미지를 미리 빌드합니다.

```bash
$> docker build -t django-app -f django/Dockerfile .
```

job 실행!

<img src="https://user-images.githubusercontent.com/37063580/161376977-4ee9be9d-f840-461b-8acd-2765a6d839d5.png" width=1000>

Graph 페이지로 들어가 실행 상태를 체크힙니다.

<img src="https://user-images.githubusercontent.com/37063580/161376979-bf2d70a3-0f4b-4346-8adc-443baf97346a.png" width=1000>

모든 작업이 정상적으로 완료되었습니다.

<img src="https://user-images.githubusercontent.com/37063580/161376980-0b47cd6b-d939-4976-8e01-0c415e25231a.png" width=1000>
