from .model import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .schemas import UserCreateModel
from .utils import generate_password_hash, verify_password

class UserService:
    async def get_user_by_email(self,email: str, session: AsyncSession):
        """Get user by email"""
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        
        user = result.first()

        return user

    async def user_exists(self,email:str , session: AsyncSession):
        """Check if user exists"""
        user= await self.get_user_by_email(email, session)


        if user is None:
            return False

        else:
            return True


    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)


        new_user.password_hash = generate_password_hash(user_data_dict["password"])


        #print(new_user)
        session.add(new_user)
        await session.commit()

        return new_user