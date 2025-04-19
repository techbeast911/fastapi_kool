from sqlalchemy.ext.asyncio import AsyncSession


class get_records:
    async def get_all_records(self,session:AsyncSession):
        pass

    async def get_record_by_id(self,product_serial_no:str,session:AsyncSession):
        pass

    async def create_record(self,product_serial_no:str,date_logged_in:str,product_sku:str,product_category:str,client_name:str,date_logged_out:str,session:AsyncSession):
        pass

    