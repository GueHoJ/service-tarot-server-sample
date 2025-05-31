# 프로젝트 개요

이 프로젝트는 Django REST Framework 기반의 백엔드 서버와 Nginx, Vault Agent, Langflow 등 다양한 서비스로 구성된 멀티 컨테이너 서버 템플릿입니다.  
주요 목적은 빠른 신규 서버 개발, 인증/권한, 챗봇, 서비스 토큰, 로그, 언어처리 등 다양한 기능을 모듈화하여 제공합니다.

> **참고:**
> - `langflow_service`, 그리고 `django_rest_framework` 내부의 `lang`, `ollamas` 등은 다양한 LLM(대형 언어 모델) 후보군의 성능 및 연동 테스트를 위해 임시로 포함된 모듈입니다. 실제 서비스 적용 전, 모델 선정 및 벤치마킹 용도로 활용되었습니다.
> - 본 서버는 **Vault(시크릿/환경변수 관리)**, **Nginx Proxy Manager(도메인/SSL 관리)**, **PostgreSQL 등 외부 데이터베이스**와의 통합을 전제로 설계되었습니다. 이들 외부 솔루션이 함께 운영되어야 실제 서비스 환경에서 정상적으로 동작합니다.

---

## 디렉토리 구조

```
.
├── django_rest_framework/   # 메인 백엔드(DRF) 서비스
│   ├── app/                # 공통 유틸리티, 미들웨어 등
│   ├── user/               # 사용자 도메인 (DDD 구조)
│   ├── chatbot/            # 챗봇 도메인 (OpenAI 등)
│   ├── servicetoken/       # 서비스 토큰 관리
│   ├── servicelog/         # 서비스 로그 관리
│   ├── ollamas/            # LLM 연동 모듈 (LLM 테스트용)
│   ├── lang/               # 언어처리 도메인 (LLM 테스트용)
│   ├── redirect/           # 리다이렉트 도메인
│   ├── static/, media/     # 정적/미디어 파일
│   ├── templates/          # 템플릿(에러, swagger 등)
│   ├── project/            # Django 프로젝트 설정
│   ├── requirements.txt    # Python 패키지 목록
│   └── Dockerfile          # DRF 서비스용 Dockerfile
├── nginx/                  # Nginx 리버스 프록시 및 정적 웹서버
│   ├── conf.d/             # Nginx 설정 파일
│   ├── web/                # Flutter Web 등 정적 웹앱 배포 디렉토리
│   └── Dockerfile          # Nginx용 Dockerfile
├── langflow_service/       # Langflow 서비스 (AI 워크플로우, LLM 테스트용)
│   ├── requirements.txt
│   └── Dockerfile
├── vault-agent-docker/     # Vault Agent (시크릿 관리)
│   ├── vault-agent-config/ # Vault Agent 설정 및 템플릿
│   └── Dockerfile
├── docker-compose.local.yml # 로컬 개발용 compose
├── docker-compose.dev.yml   # 개발 환경용 compose
└── README.md                # 프로젝트 설명서
```

---

## 주요 서비스 및 역할

### 1. django_rest_framework
- **구성**: DDD 구조(도메인별 디렉토리), 챗봇, 사용자, 서비스 토큰, 로그, 언어처리 등
- **실행**: gunicorn, websocket, static/media 분리, Vault 연동
- **설정**: `project/settings.py`, `.env.local` 등
- **실행 방식**: 
    - `start.sh` 스크립트에서 가상환경 활성화, 정적파일 수집, 마이그레이션, 슈퍼유저 생성 후
    - **ASGI 서버(daphne)를 통해 `project.asgi:application`을 8000 포트로 실행**
    - 즉, 이 서버는 WSGI가 아닌 ASGI 기반으로 동작하며, HTTP와 WebSocket을 모두 지원합니다.

### 2. nginx
- **역할**: 리버스 프록시, 정적 파일/Flutter Web 서비스, SSL/TLS, 서브도메인 라우팅
- **설정**: `nginx/conf.d/default.conf` 등
- **HTTP & WebSocket 관리**:
    - 80/443 포트에서 HTTP/HTTPS 요청을 수신
    - `/` 경로: Django(ASGI) 서버로 프록시 (HTTP 요청)
    - `/ws/` 경로: WebSocket 통신을 Django(ASGI)로 프록시 (Upgrade 헤더 등 세팅)
    - `/static/`, `/media/`: 정적/미디어 파일 직접 서빙
    - 정적 리소스 캐싱 및 CORS 헤더 처리

### 3. vault-agent-docker
- **역할**: HashiCorp Vault 기반 시크릿(환경변수, 인증정보 등) 관리
- **설정**: 템플릿 기반 환경설정 자동화

### 4. langflow_service
- **역할**: Langflow 기반 AI 워크플로우 서비스 (LLM 테스트 및 벤치마킹)

---

## 개발 및 실행 방법

1. **컨테이너 이름, 포트 등 환경에 맞게 수정**
2. **.git, .idea 등 불필요한 파일/폴더 삭제**
3. **Python 인터프리터 및 의존성 설정**
4. **Vault, Nginx, DRF 등 포트 및 도메인 환경 맞춤**
5. **필요시 Flutter Web 빌드 및 nginx/web에 배포**
6. **docker-compose로 전체 서비스 실행**

---

## 커스텀/확장 포인트

- 도메인별 디렉토리 추가 및 DDD 구조 확장
- Nginx 서브도메인/SSL/정적 파일 라우팅 커스텀
- Vault Agent 템플릿 및 시크릿 관리 정책 확장
- Langflow 등 AI 서비스 연동

---

## 참고자료

아래는 Sample Project README.md의 원본 내용입니다.

---

[참고자료]

# Sample Project For New Server Development

## 1. rename every container after replication of this project
~~~yml
# example for auth_server dev
services:
  django_rest_framework: # <= django_rest_framework_auth_server 로 변경
    build:
      context: ./django_rest_framework
    container_name: django_rest_framework # <= django_rest_framework_auth_server 로 변경
    ...
~~~

## 2. remove .git and .idea folder

## 3. change python interpreter

### Settings > Project: your-server > Python Interpreter > Add Interpreter

> <img width="1006" alt="스크린샷 2024-08-23 오후 9 31 05" src="https://github.com/user-attachments/assets/80a3cb55-c8f1-4bf4-8496-42cba68a3d79">

## 4. change port for server

### docker-compose.yml, nginx and DRF configurations
### 8000 > 8001 > 8002 ...

#### docker-compose.yml
~~~yml
services:
  django_rest_framework_auth_server:
    build:
      context: ./django_rest_framework
    container_name: django_rest_framework_auth_server
    command: >
      bash -c "
      python manage.py collectstatic --noinput
      && python manage.py makemigrations 
      && python manage.py migrate --database default
      && python manage.py makesuperuser
      && gunicorn project.wsgi:application --bind 0.0.0.0:8000 --timeout 300 --workers 12 --threads 8"
    volumes:
      - ./django_rest_framework:/django_rest_framework
    working_dir: /django_rest_framework
    env_file:
      - .env.local
    ports:
      # 외부 포트: 내부 포트
      - "8001:8000"
  ...

  nginx_auth_server:
    build:
      context: ./nginx  # Path to the directory containing the Dockerfile
    container_name: nginx-server-auth-server
    ports:
      # 외부 포트: 내부 포트
      # - "80:80"
      # - "443:443" HTTPS 문제는 도메인 단에서 처리
      - "8101":"80" # 쉽게 관리하기 위해서 DRF 포트에 100 더한 값으로 정의, lsof -i :8101 명령어로 포트 사용 중인지 확인 가능
~~~
![docker-compose.yml](https://github.com/user-attachments/assets/5945212a-ef4b-4d28-a484-bf4366231ab3)


#### ./nginx/conf.d/default.conf
~~~conf
# upstream django_rest_framework {
#      server django_rest_framework:8000;
# }

upstream django_rest_framework_auth_server {
     server django_rest_framework_auth_server:8000;
}
~~~
![default.conf](https://github.com/user-attachments/assets/40c1ccd2-73a5-4335-986c-255690e8b1b6)

## 5. add url to csrf_trusted_origins of vault 

### secret > django-rest-framework > dev > settings > create new version

<img width="1472" alt="vault csrf tructed origins" src="https://github.com/user-attachments/assets/4b1e48e2-c3bd-4aa1-b519-0e380af9a8f8">

## 6. configure nginx subdomain

~~~conf
server {
    listen 443 ssl;
    server_name sample.conai.ai;  # Read domain from environment variable

    ssl_certificate /etc/nginx/certs/star_conai_ai.crt;
    ssl_certificate_key /etc/nginx/certs/conai_ai_private.key;  # Ensure you have a key file
    ssl_trusted_certificate /etc/nginx/certs/My_CA_Bundle.ca-bundle;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://django_rest_framework;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        # 원하는 경로로 설정 할 수 없어서 오류에서 뱉는 경로에 맞춤
        alias /etc/nginx/html/static/;
    }

    location /media/ {
        # 원하는 경로로 설정 할 수 없어서 오류에서 뱉는 경로에 맞춤
        # media 쪽은 확인 필요
        alias /etc/nginx/html/media/;
    }

    # Optionally, you can also add caching headers for static files
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }
}
~~~

## 7. deploy flutter web app if needed

### flutter build web

### copy flutter web app to ./nginx/web

### configure nginx for flutter web app

~~~conf
# HTTPS 설정 for web.conai.ai
server {
    listen 443 ssl;
    server_name web.conai.ai;

    # SSL 설정 (기존의 인증서 경로와 동일하게 설정)
    ssl_certificate /etc/nginx/certs/star_conai_ai.crt;
    ssl_certificate_key /etc/nginx/certs/conai_ai_private.key;
    ssl_trusted_certificate /etc/nginx/certs/My_CA_Bundle.ca-bundle;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Flutter 웹 애플리케이션 빌드된 파일 경로
    root /var/www/flutter_web/build/web;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;  # Flutter의 SPA 처리
    }

    # 캐시를 위한 설정 (선택 사항)
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }
}
~~~









