from pydantic import BaseModel, Field
from datetime import datetime

class DataCreate(BaseModel):
    device_id: str = Field(..., example="camila_01", description="Identificador do dispositivo")
    category: str = Field(..., example="produção", description="Categoria do dado")
    type: str = Field(..., example="temperatura", description="Tipo do dado coletado")
    value: float = Field(..., example=25.4, description="Valor numérico medido")
    unit: str = Field(..., example="°C", description="Unidade de medida")
    timestamp: datetime = Field(..., example="2025-09-30T14:25:00Z", description="Data e hora da medição")