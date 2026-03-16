from pydantic import BaseModel

class Alert(BaseModel):
    id: int
    message: str
    severity: str  # e.g., 'low', 'medium', 'high'
    timestamp: str  # ISO 8601 format

class AlertResponse(BaseModel):
    alerts: list[Alert]
    count: int

class AlertSchema(BaseModel):
    alert: Alert
