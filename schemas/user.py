from pydantic import BaseModel
from typing import Optional

# Modelos o DTOs
class User(BaseModel):
  id: Optional[str]
  name: str
  email: str
  password: str