from sqlmodel import Field, SQLModel, create_engine, Session, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from uuid import UUID, uuid4  

class inventory(SQLModel, table=True):
    __tablename__ = "inventory"

    # id: UUID = Field(
    #     sa_column=Column(pg.UUID, default=uuid4, nullable=False, primary_key=True)
    # )
    product_serial_no: int = Field(default=None, primary_key=True, unique=True)
    date_logged_in: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False)
    )
    product_sku: str = Field(nullable=False)
    product_category: str = Field(nullable=False)  # Removed special characters
    client_name: str = Field(nullable=False)
    date_logged_out: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False)
    )

    def __repr__(self):
        return (
            f"Inventory(product_serial_no={self.product_serial_no}, "
            f"date_logged_in={self.date_logged_in}, product_sku={self.product_sku}, "
            f"product_category={self.product_category}, client_name={self.client_name}, "
            f"date_logged_out={self.date_logged_out})"
        )
