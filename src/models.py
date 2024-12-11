from random import choice
from sqlalchemy import Column, Integer, SmallInteger, String, ForeignKey, Date, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Hero(Base):
    __tablename__ = "heroes"
    __table_args__ =  {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    side = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    birthday = Column(Date())
    power = Column(SmallInteger)
    story = relationship("Story", back_populates="hero", uselist=False, cascade="all, delete-orphan")
    motos = relationship("Moto", back_populates="hero", cascade="all, delete-orphan")
    
    def get_moto(self):
        return choice(self.motos)

    def __repr__(self):
        return f"Hero name: {self.name}"


class Moto(Base):
    __tablename__ = "motos"
    __table_args__ =  {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    moto_id = Column(Integer, nullable=False)
    moto = Column(String(255), unique=True, nullable=False)

    hero = relationship("Hero", back_populates="motos")

    def __repr__(self):
        return f"{self.moto_id}: {self.moto}"


class Battle(Base):
    __tablename__ = "battles"
    __table_args__ =  {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    hero_id_1 = Column(Integer, nullable=False)
    hero_id_2 = Column(Integer, nullable=False)
    moto_id_1 = Column(Integer, nullable=False)
    moto_id_2 = Column(Integer, nullable=False)
    winner = Column(SmallInteger, nullable=False)

    hero1 = relationship("Hero", foreign_keys=hero_id_1, primaryjoin="Battle.hero_id_1==Hero.id")
    hero2 = relationship("Hero", foreign_keys=hero_id_2, primaryjoin="Battle.hero_id_2==Hero.id")
    moto1 = relationship("Moto", foreign_keys=moto_id_1, primaryjoin="Battle.moto_id_1==Moto.id")
    moto2 = relationship("Moto", foreign_keys=moto_id_2, primaryjoin="Battle.moto_id_2==Moto.id")

    def __repr__(self):
        return f"{self.hero_id_1} VS {self.hero_id_2}"


class Story(Base):
    __tablename__ = "stories"
    __table_args__ =  {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    story = Column(Text)
    hero_id = Column(Integer, ForeignKey("heroes.id"))

    hero = relationship("Hero", back_populates="story")

    def __repr__(self):
        return f"{self.hero_id}:{self.story}"
