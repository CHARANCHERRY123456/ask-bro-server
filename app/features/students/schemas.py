from pydantic import BaseModel

class R20StudentSchema(BaseModel):
    ID: str
    NAME: str
    GENDER: str
    CGPA: float
    RANK: int | None

    class Config:
        orm_mode = True

class R21StudentSchema(BaseModel):
    ID: str
    NAME: str
    GENDER: str
    CGPA: float
    RANK: int | None
    class Config:
        orm_mode = True