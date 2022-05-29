from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session

async def on_start_up(app):
    engine = create_async_engine(
        app.CONFIG.DB_URL
    )
    
    session = AsyncSession(engine, expire_on_commit=False)

    app.db = session
    app.db_engine = engine
    

async def on_shutdown(app):
    
    await app.db.close()
    await app.db_engine.dispose()
