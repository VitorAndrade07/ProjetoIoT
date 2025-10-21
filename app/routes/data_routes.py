from fastapi import APIRouter
from app.models.data_model import DataCreate
from app.controllers.data_controller import save_to_db, list_data, get_by_device

router = APIRouter()

@router.post("/")
def create_data(data: DataCreate):
    """Cadastra dados manualmente via API"""
    save_to_db(data.dict())
    return {"status": "ok", "message": "Dados salvos com sucesso"}

@router.get("/")
def get_all_data(limit: int = 50):
    """Lista todos os dados, com limite padrão de 50"""
    return list_data(limit)

@router.get("/{device_id}")
def get_data_by_device(device_id: str):
    """Lista os dados de um dispositivo específico"""
    return get_by_device(device_id)


