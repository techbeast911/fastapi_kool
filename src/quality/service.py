from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Record, RecordCreate, RecordUpdateModel
from sqlmodel import select,desc
from src.quality.models import quality


class get_records:
    async def get_all_records(self,session:AsyncSession):
        statement = select(quality).order_by(desc(quality.date_received))
        #statement = select(quality).order_by(desc(quality.date_passed_to_inventory))
        result = await session.execute(statement)  # ✅ Correct
        print(result)

        records = result.scalars().all()  # Extracts all records

        return [record.dict() for record in records]  # Converts to JSON
        #return result.all()
        

    async def get_record_by_id(self,serial_number:str,session:AsyncSession):
        statement = select(quality).where(quality.serial_number == serial_number)
        #statement = select(quality).where(quality.serial_number == serial_number).order_by(desc(quality.date_passed_to_inventory))
        result = await session.execute(statement)  # ✅ Correct


        record = result.scalars().first() # ✅ Ensures we get an ORM object, not a tuple
        
        return record.dict() if record else None  # ✅ Convert to dictionary for JSON response

    async def create_record(self,record:RecordCreate,session:AsyncSession):
        record_data_dict = record.model_dump()
        record_data = quality(**record_data_dict)

        session.add(record_data)
        await session.commit()
        await session.refresh(record_data)
        return record_data.dict()  # ✅ Convert to a JSON-serializable dictionary


    async def update_record(self,serial_number:str,update_data:RecordUpdateModel,session:AsyncSession):
        record_to_update =  await self.get_record_by_id(serial_number, session)
        if not record_to_update:
            return None
        update_data_dict = update_data.model_dump(exclude_unset=True)

        for k,v in update_data_dict.items():
            setattr(record_to_update,k,v)
        
        await session.commit()
        await session.refresh(record_to_update)

        return record_to_update
    
    async def delete_record(self,serial_number:str,session:AsyncSession):
        record_to_delete = await self.get_record_by_id(serial_number, session)
        if record_to_delete is not None:
            await session.delete(record_to_delete)
            await session.commit()

        
            return {}
        
        else:
            return None

        #return {"message": "Record deleted successfully"}


    