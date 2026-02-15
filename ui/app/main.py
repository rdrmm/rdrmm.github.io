from fastapi import FastAPI, Request
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI(title="rdRMM UI")

# Templates and static
templates = Jinja2Templates(directory="ui/app/templates")
app.mount("/ui/static", StaticFiles(directory="ui/app/static"), name="static")

# In-memory demo data
DEVICES = [
    {"id": f"dev-{1000+i}", "name": f"device-{i+1}", "os": os, "online": True if i % 3 != 0 else False, "cpu": 12 + i*6}
    for i, os in enumerate(["linux", "windows", "mac", "linux", "windows", "linux"])  
]


@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "devices": DEVICES, "now": datetime.utcnow()})


@app.get("/admin")
def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request, "devices": DEVICES, "now": datetime.utcnow()})


@app.get("/api/devices")
def api_devices():
    return JSONResponse(DEVICES)


@app.get("/api/device/{device_id}")
def api_device(device_id: str):
    found = next((d for d in DEVICES if d["id"] == device_id), None)
    if not found:
        return JSONResponse({"error": "not found"}, status_code=404)
    return JSONResponse(found)
