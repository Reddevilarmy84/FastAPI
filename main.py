from fastapi import APIRouter
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Parser import path_to_json, dict_list_to_json, json_to_dict_list, pars, url

app = APIRouter()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    context = {
        "id": id,
        "request": request,
        "title": "Кодим..."
    }
    return templates.TemplateResponse("home.html", context)

@app.get("/parser/{year}")
async def parser(request: Request, year: int = None):
    json = json_to_dict_list(path_to_json)
    context = {
        "year": year,
        "request": request,
        "title": 'Парсер LordFilms',
        'json': json,
    }
    return templates.TemplateResponse("parser.html", context)

@app.get("/details/{id}")
async def details(request: Request, id: int = None):
    json = json_to_dict_list(path_to_json)
    for i in json:
        if i['ID'] == id:
            item = i
    context = {
        "item": item,
        "id": id,
        "request": request,
    }
    return templates.TemplateResponse("details.html", context)