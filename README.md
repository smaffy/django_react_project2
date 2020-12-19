Django(DRF), React(SPA), nginx, Docker 

Django DRF + Frontend served separately (same domain)

Authenticate Single-Page Applications (SPAs) with session-based authentication.  
Using Django for our backend while the frontend will be built with React, a JavaScript library designed for building user interfaces.


        ├── backend
        │   ├── Dockerfile
        │   ├── api
        │   │   ├── __init__.py
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   │   └── __init__.py
        │   │   ├── models.py
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── djangocookieauth
        │   │   ├── __init__.py
        │   │   ├── asgi.py
        │   │   ├── settings.py
        │   │   ├── urls.py
        │   │   └── wsgi.py
        │   ├── manage.py
        │   └── requirements.txt
        ├── docker-compose.yml
        ├── frontend
        │   ├── Dockerfile
        │   ├── README.md
        │   ├── package-lock.json
        │   ├── package.json
        │   ├── public
        │   │   ├── favicon.ico
        │   │   ├── index.html
        │   │   ├── manifest.json
        │   │   └── robots.txt
        │   └── src
        │       ├── App.js
        │       ├── index.css
        │       └── index.js
        └── nginx
            ├── Dockerfile
            └── nginx.conf


*****************************
        $ docker-compose up -d --build
        
        $ docker-compose exec backend python manage.py makemigrations
        $ docker-compose exec backend python manage.py migrate
        $ docker-compose exec backend python manage.py createsuperuser
        




pip install Django
pip install djangorestframework

npm install universal-cookie

*****************************


| Approach | Frontend | Backend | 
| :---: | :---: | :---: | 
| Frontend served from Django | Grab the CSRF token using universal-cookies and use credentials: "same-origin" in the requests. | Set CSRF_COOKIE_SAMESITE, SESSION_COOKIE_SAMESITE to "Strict". Enable SESSION_COOKIE_HTTPONLY and disable CSRF_COOKIE_HTTPONLY. |
| Frontend served separately (same domain) | Obtain CSRF token and use credentials: "same-origin" in the fetch request. | Add a route handler for generating the CSRF token that gets set in the response headers. Set SESSION_COOKIE_HTTPONLY, CSRF_COOKIE_HTTPONLY to True and SESSION_COOKIE_SAMESITE, CSRF_COOKIE_SAMESITE to "Strict". |
| Frontend served separately with DRF (same domain) | Obtain CSRF token and use credentials: "same-origin" in the fetch request. |	Add a route handler for generating the CSRF token that gets set in the response headers. Set SESSION_COOKIE_HTTPONLY, CSRF_COOKIE_HTTPONLY to True and SESSION_COOKIE_SAMESITE, CSRF_COOKIE_SAMESITE to "Strict". |
| Frontend served separately (cross-origin) | Obtain CSRF token and use credentials: "include" in the fetch request. | Enable CORS and add a route handler for generating the CSRF token that gets set in the response headers. Set SESSION_COOKIE_HTTPONLY, CSRF_COOKIE_HTTPONLY to True and SESSION_COOKIE_SAMESITE, CSRF_COOKIE_SAMESITE to "Lax". Add the django-cors-headers package and configure the CORS_ALLOWED_ORIGINS, CORS_EXPOSE_HEADERS, and CORS_ALLOW_CREDENTIALS settings. |

