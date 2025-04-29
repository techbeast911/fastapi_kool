# from sqlalchemy.ext.asyncio import AsyncSession
# from .schemas import Record, RecordCreate, RecordUpdateModel
# from sqlmodel import select,desc
# from .models import inventory


# class get_records:
#     async def get_all_records(self,session:AsyncSession):
#         statement = select(inventory).order_by(desc(inventory.date_logged_in))
#         result = await session.execute(statement)  # ✅ Correct
#         print(result)

#         records = result.scalars().all()  # Extracts all records

#         return [record.dict() for record in records]  # Converts to JSON
#         #return result.all()
        

#     async def get_record_by_id(self,product_serial_no:str,session:AsyncSession):
#         statement = select(inventory).where(inventory.product_serial_no == product_serial_no)
#         result = await session.execute(statement)  # ✅ Correct


#         record = result.scalars().first() # ✅ Ensures we get an ORM object, not a tuple
        
#         return record.dict() if record else None  # ✅ Convert to dictionary for JSON response

#     async def create_record(self,record:RecordCreate,session:AsyncSession):
#         record_data_dict = record.model_dump()
#         record_data = inventory(**record_data_dict)

#         session.add(record_data)
#         await session.commit()
#         await session.refresh(record_data)
#         return record_data.dict()  # ✅ Convert to a JSON-serializable dictionary


#     async def update_record(self,product_serial_no:str,update_data:RecordUpdateModel,session:AsyncSession):
#         record_to_update =  await self.get_record_by_id(product_serial_no, session)
#         if not record_to_update:
#             return None
#         update_data_dict = update_data.model_dump(exclude_unset=True)

#         for k,v in update_data_dict.items():
#             setattr(record_to_update,k,v)
        
#         await session.commit()
#         await session.refresh(record_to_update)

#         return record_to_update
    
#     async def delete_record(self,product_serial_no:str,session:AsyncSession):
#         record_to_delete = await self.get_record_by_id(product_serial_no, session)
#         if record_to_delete is not None:
#             await session.delete(record_to_delete)
#             await session.commit()

        
#             return {}
        
#         else:
#             return None

#         #return {"message": "Record deleted successfully"}


    

from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Record, RecordCreate, RecordUpdateModel
from sqlmodel import select, desc
from .models import inventory
from datetime import datetime, timezone

class get_records:
    async def get_all_records(self, session: AsyncSession):
        statement = select(inventory).order_by(desc(inventory.date_logged_in))
        result = await session.execute(statement)
        records = result.scalars().all()
        return [record.dict() for record in records]
    
    async def get_record_by_id(self, product_serial_no: str, session: AsyncSession):
        statement = select(inventory).where(inventory.product_serial_no == product_serial_no)
        result = await session.execute(statement)
        record = result.scalars().first()
        
        return record.dict() if record else None
    
    async def create_record(self, record: RecordCreate, session: AsyncSession):
        # Handle timezone issue - Convert timezone-aware to timezone-naive
        record_data_dict = record.model_dump()
        
        # Fix datetime timezone issues
        if hasattr(record.date_logged_in, 'tzinfo') and record.date_logged_in.tzinfo:
            record_data_dict['date_logged_in'] = record.date_logged_in.replace(tzinfo=None)
            
        if hasattr(record.date_logged_out, 'tzinfo') and record.date_logged_out.tzinfo:
            record_data_dict['date_logged_out'] = record.date_logged_out.replace(tzinfo=None)
        
        record_data = inventory(**record_data_dict)
        session.add(record_data)
        await session.commit()
        await session.refresh(record_data)
        return record_data.dict()
    
    async def update_record(self, product_serial_no: str, update_data: RecordUpdateModel, session: AsyncSession):
        statement = select(inventory).where(inventory.product_serial_no == product_serial_no)
        result = await session.execute(statement)
        record_to_update = result.scalars().first()
        
        if not record_to_update:
            return None
            
        # Get the data that needs to be updated
        update_data_dict = update_data.model_dump(exclude_unset=True)
        
        # Fix datetime timezone issues for update
        if 'date_logged_in' in update_data_dict and hasattr(update_data_dict['date_logged_in'], 'tzinfo') and update_data_dict['date_logged_in'].tzinfo:
            update_data_dict['date_logged_in'] = update_data_dict['date_logged_in'].replace(tzinfo=None)
            
        if 'date_logged_out' in update_data_dict and hasattr(update_data_dict['date_logged_out'], 'tzinfo') and update_data_dict['date_logged_out'].tzinfo:
            update_data_dict['date_logged_out'] = update_data_dict['date_logged_out'].replace(tzinfo=None)
        
        # Update the record attributes
        for key, value in update_data_dict.items():
            setattr(record_to_update, key, value)
        
        await session.commit()
        await session.refresh(record_to_update)
        return record_to_update.dict()  # Return as dict for JSON serialization
    
    async def delete_record(self, product_serial_no: str, session: AsyncSession):
        statement = select(inventory).where(inventory.product_serial_no == product_serial_no)
        result = await session.execute(statement)
        record_to_delete = result.scalars().first()
        
        if record_to_delete is not None:
            await session.delete(record_to_delete)
            await session.commit()
            return {}
        else:
            return None
