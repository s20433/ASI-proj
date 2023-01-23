from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import models, schemas

def create_country(db: Session, id: int, country: schemas.CountryCreate) -> models.Country:

    db_country = models.Country(
        id = id,
        name = country.name
    )
    db.add(db_country)