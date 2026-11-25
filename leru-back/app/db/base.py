from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Importe os models aqui para o Alembic detectá-los no autogenerate, ex.:
# from app.models.user import User  # noqa: F401
