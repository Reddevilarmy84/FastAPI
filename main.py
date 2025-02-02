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
        "request": request,
        "title": "Home Page"
    }
    return templates.TemplateResponse("home.html", context)

@app.get("/parser/")
async def parser(request: Request, year: int, page: int):
    json = json_to_dict_list(path_to_json)
    data = {
        "request": request,
        "year": year,
        "page": page,
        "title": 'Парсер LordFilms',
        'json': json,
    }
    return templates.TemplateResponse("parser.html", data)