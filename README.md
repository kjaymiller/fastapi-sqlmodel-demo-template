# FastAPI + SQLModel Demo Template

This template is to create a solid baseline to start building an app using FastAPI and SQL Model. The hope is that this can be used to jumpstart many demos using FastAPI.

## Setup

### Install the Application 

This application is setup that you can install it locally and then run the application.

```sh
python -m pip install -e .
```

### Run the application

Use uvicorn (or gunicorn which isn't installed) to run the application locally.

```sh
python -m uvicorn "fastapi_app.app:app"
```

You can add any uvicorn modifiers you wish.