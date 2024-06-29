from fastapi import FastAPI, Request, Query, Body, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from enum import Enum
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="statics")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/table", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="table.html",
    )
    # http : 80 | https: 443 | https = http + security
    # python -m fastapi dev nameofFile.py
    # -m fastapi dev nameofFile.py
    #


@app.get("/item")
async def item(userName: str = "Anonymouse", age: int = 18):
    return {"message": f"{userName} you so ez v2, age of you is {age}"}


@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request, userName: str = "Anonymouse"):
    return templates.TemplateResponse(
        request=request, name="welcome.html", context={"user": userName}
    )


# listSubject = ["Digital Skill", "Web Programming", "Programming I", "Statistic"]


# async def searchSubject(listSubject: list, keyword: str) :
#     # return [word for word in lst if keyword in word]
#     response = []
#     for word in listSubject:
#         if keyword in word:
#             response.append(word)
#     return response


# @app.get("/subject", response_class=HTMLResponse)
# async def subject(request: Request, keyword: str | None = None):
#     listSubject.sort()
#     mathSubject = listSubject
#     if keyword:
#         mathSubject = await searchSubject(listSubject, keyword)
#     return templates.TemplateResponse(
#         request=request,
#         name="subject.html",
#         context={"subjectlist": mathSubject},
#     )



# @app.post("/subject")
# async def create_subject(request: Request, subject: Annotated[str, Form()]):
#     if not subject in listSubject:
#         listSubject.append(subject)
#     return templates.TemplateResponse(
#         request=request,
#         name="subject.html",
#         context={"subjectlist": listSubject},
#     )

listSubject=[{"id": 1, "name": "Digital Skill"},
    {"id": 2, "name": "Web Programming"},
    {"id": 3, "name": "Programming I"},
    {"id": 4, "name": "Statistic"},
]


async def searchSubject(listSubject: list, keyword: str):
    return [f"{word['id']} {word['name']}" for word in listSubject if keyword in word["name"]]
    # response = []
    # for word in listSubject:
    #     if keyword in word:
    #         response.append(word)
    # return response


@app.get("/subject", response_class=HTMLResponse)
async def subject(request: Request, keyword: str | None = None):
    newlist = sorted(listSubject, key=lambda d: d["id"])
    matchSubject = newlist
    if keyword:
        matchSubject = await searchSubject(listSubject, keyword)
    else:
        # Return all subjects in "id name" format if no keyword is provided
        matchSubject = [f"{word['id']} {word['name']}" for word in listSubject]
    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": matchSubject},
    )

class Subject(BaseModel):
    id: int = Form()
    name: str = Form()


@app.post("/subject")
async def create_subject(
    request: Request,
    subject_id: Annotated[int, Form()],
    subject_name: Annotated[str, Form()],
):
    global listSubject
    sub = {"id": subject_id, "name": subject_name}
    if not sub in listSubject:
        listSubject.append(sub) 
        listSubject = sorted(listSubject, key=lambda d: d["id"])

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": listSubject},
    )
# listStudent = []


# async def searchStudent(listStudent: list, keywordst: str) :
#     # return [word for word in lst if keyword in word]
#     response = []
#     for word in listStudent:
#         if keywordst in word:
#             response.append(word)
#     return response


# @app.get("/student", response_class=HTMLResponse)
# async def student(request: Request, keywordst: str | None = None):
#     listStudent.sort()
#     mathStudent = listStudent
#     if keywordst:
#         mathStudent = await searchStudent(listStudent, keywordst)
#     return templates.TemplateResponse(
#         request=request,
#         name="student.html",
#         context={"studentlist": mathStudent},
#     )



# @app.post("/student")
# async def create_student(request: Request, student: Annotated[str, Form()]):
#     if not student in listStudent:
#         listStudent.append(student)
#     return templates.TemplateResponse(
#         request=request,
#         name="student.html",
#         context={"studentlist": listStudent},
#     )

listStudent = [
    {"id": 66310047, "name": "Sarinthorn Pamorn"},
    {"id": 66310048, "name": "Napassakorn Cheunchum"},
    {"id": 66310050, "name": "Nutthaphong Boonsong"},
] 

async def searchStudent(listStudent: list, keywords: str):
    return [f"{words['id']} {words['name']}" for words in listStudent if keywords in words["name"]]

    # response = []
    # for word in listStudent:
    #     if keywords in word:
    #         response.append(word)
    # return response


@app.get("/student", response_class=HTMLResponse)
async def student(request: Request, keywords: str | None = None):
    newstudentlist = sorted(listStudent, key=lambda d: d["id"])
    matchStudent = newstudentlist
    if keywords:
        matchStudent = await searchStudent(listStudent, keywords)
    else:
        matchStudent = [f"{words['id']} {words['name']}" for words in listStudent ]

    return templates.TemplateResponse(
        request=request,
        name="student.html",
        context={"studentList": matchStudent},
    )


class Student(BaseModel):
    id: int = Form()
    name: str = Form()


@app.post("/student")
async def create_student(
    request: Request,
    student_id: Annotated[int, Form()],
    student_name: Annotated[str, Form()],
):
    global listStudent
    substudent = {"id": student_id, "name": student_name}
    if not substudent in listStudent:
        listStudent.append(substudent) 
        listStudent = sorted(listStudent, key=lambda d: d["id"])

    return templates.TemplateResponse(
        request=request,
        name="student.html",
        context={"studentList": listStudent},
    )