import pathlib
import io
import uuid
from tempfile import template
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploaded"
print((BASE_DIR / "templates").exists())
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/",response_class=HTMLResponse) # http get
def home_view(request:Request):
    return templates.TemplateResponse("home.html",{"request":request, "abc":123})

@app.post("/") # http post
def home_detail_view():
    return {"hello":"world"}

@app.post("/img-echo/", response_class=FileResponse) # http post
async def img_echo_view(file:UploadFile = File(...)):
    bytes_str = io.BytesIO(await file.read())
    fname = pathlib.Path(file.filename)
    fest = fname.suffix # .jpg, .txt
    dest = UPLOAD_DIR / f"{uuid.uuid1()}{fest}"
    with open(str(dest),'wb') as out:
        out.write(bytes_str.read())
    return dest