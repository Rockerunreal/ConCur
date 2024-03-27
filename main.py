from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.responses import RedirectResponse
import os
import uvicorn
from fastapi.templating import Jinja2Templates
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
import json
import urllib




app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index_ru():
    htmlfile = open('templates/main.html', 'r', encoding='utf-8')
    index = htmlfile.read()
    return HTMLResponse(content=index)

@app.get("/ru/", response_class=HTMLResponse)
async def some_route(request: Request):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)

    return templates.TemplateResponse("index_ru_desctop.html",
          {
              "request": request,

              "val1": data["USD-RUB"],

              "val2": data["USD-TRY"],

              "val3": data["TRY-USD"],

              "val4": data["TRY-RUB"],

              "val5": data["RUB-TRY"],

              "val6": data["RUB-USD"]
          }
)

@app.get("/m.ru/", response_class=HTMLResponse)
async def some_route(request: Request):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
    return templates.TemplateResponse("index_ru_mobile.html",
          {
              "request": request,

              "val1": data["USD-RUB"],

              "val2": data["USD-TRY"],

              "val3": data["TRY-USD"],

              "val4": data["TRY-RUB"],

              "val5": data["RUB-TRY"],

              "val6": data["RUB-USD"]

          }
)

@app.get("/tyr/", response_class=HTMLResponse)
async def some_route(request: Request):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
    return templates.TemplateResponse("index_tyr_desctop.html",
          {
              "request": request,

              "val1": data["USD-RUB"],

              "val2": data["USD-TRY"],

              "val3": data["TRY-USD"],

              "val4": data["TRY-RUB"],

              "val5": data["RUB-TRY"],

              "val6": data["RUB-USD"]
          }
)


@app.get("/m.tyr/", response_class=HTMLResponse)
async def some_route(request: Request):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
    return templates.TemplateResponse("index_tyr_mobile.html",
          {
              "request": request,

              "val1": data["USD-RUB"],

              "val2": data["USD-TRY"],

              "val3": data["TRY-USD"],

              "val4": data["TRY-RUB"],

              "val5": data["RUB-TRY"],

              "val6": data["RUB-USD"]
          }
)


@app.get("/RU/{path}")
def get_picture(path):
    path1 = os.path.join('static','RU',path)
    return FileResponse(f'{path1}')

@app.get("/data.json")
def get_picture(path):
    return FileResponse("/data.json")

@app.get("/tyr/RU/{path}")
def get_picture(path):
    path1 = os.path.join('static','RU',path)
    return FileResponse(f'{path1}')

@app.get("/m.tyr/RU/{path}")
def get_picture(path):
    path1 = os.path.join('static','RU',path)
    return FileResponse(f'{path1}')

@app.get("/m.ru/RU/{path}")
def get_picture(path):
    path1 = os.path.join('static','RU',path)
    return FileResponse(f'{path1}')

@app.get("/ru/RU/{path}")
def get_picture(path):
    path1 = os.path.join('static','RU',path)
    return FileResponse(f'{path1}')

if __name__=="__main__":
    uvicorn.run(app)
    # uvicorn.run(app, host="v2249831.hosted-by-vdsina.ru", port=443,
    #             ssl_keyfile='/etc/letsencrypt/live/v2249831.hosted-by-vdsina.ru-0001/privkey.pem',
    #             ssl_certfile='/etc/letsencrypt/live/v2249831.hosted-by-vdsina.ru-0001/fullchain.pem')