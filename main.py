from fastapi import FastAPI
from app.routes.data_routes import router as data_router
from app.config.mqtt_cliente import start_mqtt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API IoT Camila",
    description="API REST para dados IoT da Bancada Didática 4.0 – Nível 1 (Camila)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(data_router, prefix="/data", tags=["Dados"])

@app.on_event("startup")
def startup_event():
    start_mqtt()
    print("MQTT iniciado")
