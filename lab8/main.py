from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static",StaticFiles(directory="statics"),name="statics")

templates = Jinja2Templates(directory="templates")


@app.get('/',response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )

@app.get("/table",response_class=HTMLResponse)
async def table(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )

@app.get("/items")
async def items(age : int = 18 ,username: str = "Anonymous"):
    return{
        "message": f"hello {username}, age is {age}"
    }

templates = Jinja2Templates(directory="templates")

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request, username: str= "Anonymous"):
    return templates.TemplateResponse(
        request=request, name="welcome.html", context={"id": id}
    )

#http :// 127.0.0.1

#http://127.0.0.1:8000/item ?username=Song & age = 20 parameter
#http :80 | https :443 | https = http + security/
#python -m fastapi dev main.py