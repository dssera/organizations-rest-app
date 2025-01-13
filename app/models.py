from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped
from app.db import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    house = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    organizations = relationship("Organization",
                                 back_populates="building")


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    phone_numbers = Column(String)
    building_id = Column(Integer, ForeignKey("buildings.id"))

    building = relationship("Building",
                            back_populates="organizations")
    activities = relationship("Activity",
                              secondary="organization_activities",
                              back_populates="organizations")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer,
                       ForeignKey("activities.id"),
                       nullable=True)

    children = relationship("Activity",
                            lazy="joined",
                            join_depth=3)
    organizations = relationship("Organization",
                                 secondary="organization_activities",
                                 back_populates="activities")

class OrganizationActivity(Base):
    __tablename__ = "organization_activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))


