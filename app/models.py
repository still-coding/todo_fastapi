from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    email: str
    password: str
    token: Optional[str]



SQLModel.metadata.create_all(engine)