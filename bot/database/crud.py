from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select
from .models import User, LessonProgress, Base
from bot.config import Config

engine = create_async_engine(Config.DB_URL.replace("postgresql://", "postgresql+asyncpg://"))
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_or_create_user(telegram_id: int, full_name: str, username: str = None):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == telegram_id))
        user = result.scalar_one_or_none()
        if not user:
            user = User(id=telegram_id, full_name=full_name, username=username)
            session.add(user)
            await session.commit()
        return user
