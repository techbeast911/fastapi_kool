from sqlmodel import SQLModel 
from datetime import datetime
from typing import Optional, List, Dict, Any, Union


class Quality(SQLModel, table=True):
    """Quality model."""


    date_received: datetime
    """Date the sample was received."""
    serial_number: str
    """Serial number of the sample."""
    product_sku: str
    """Product SKU."""
    performance: int 
    """Performance rating."""
    accessories_checking: str
    """Accessories checking."""
    status: str
    """Status of the sample."""
    officer_that_passed_unit: str
    """Officer that passed the unit."""
    date_passed_to_inventory: datetime
    """Date passed to inventory."""
    
    
