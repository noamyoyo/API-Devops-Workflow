import uvicorn
# import socket
from fastapi import FastAPI
from apis.routes import router

def include_router(app):
	app.include_router(router)


def start_application():
	app = FastAPI()
	include_router(app)
	return app 

app = start_application()


if __name__ == '__main__':
	uvicorn.run(app, port=8080, host='0.0.0.0')

