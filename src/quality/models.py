from sqlmodel import Field, SQLModel, create_engine, Session, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from uuid import UUID, uuid4  



class quality(SQLModel, table=True):
    __tablename__ = "quality"
    __table_args__ = {"schema": "quality"}

    date_received: datetime  = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False)
    )
    serial_number: int = Field(default=None, primary_key=True, unique=True)
    product_sku: str = Field(nullable=False)
    performance : int
    accessories_checking: str
    status: str
    officer_that_passed_unit: str
    date_passed_to_inventory: str = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False)
    )

    def __repr__(self):
        return (
            f"Quality(date_received={self.date_received}, "
            f"serial_number={self.serial_number}, product_sku={self.product_sku}, "
            f"performance={self.performance}, accessories_checking={self.accessories_checking}, "
            f"status={self.status}, officer_that_passed_unit={self.officer_that_passed_unit}, "
            f"date_passed_to_inventory={self.date_passed_to_inventory})"
        )
