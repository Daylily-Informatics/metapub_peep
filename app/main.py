from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.pubmed_search import search_pubmed

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str):
    results = search_pubmed(query)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": query})
