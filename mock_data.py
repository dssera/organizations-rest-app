from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import SessionLocal
from app.models import Organization, Building, Activity, OrganizationActivity


def add_mock_data():
    session = SessionLocal()

    session.query(OrganizationActivity).delete()
    session.query(Organization).delete()
    session.query(Activity).delete()
    session.query(Building).delete()
    session.commit()

    building1 = Building(city="Москва", street="Ленина", house="1", latitude=55.7558, longitude=37.6173)
    building2 = Building(city="Москва", street="Блюхера", house="32/1", latitude=55.7550, longitude=37.6150)
    building3 = Building(city="City of New York", street="Ленина", house="2/1", latitude=40.7128, longitude=-74.0060)
    session.add_all([building1, building2, building3])
    session.commit()

    activity1 = Activity(name="Еда")
    activity2 = Activity(name="Автомобили")

    session.add_all([activity1, activity2])
    session.commit()

    activity3 = Activity(name="Мясная продукция", parent_id=activity1.id)
    activity4 = Activity(name="Молочная продукция", parent_id=activity1.id)
    activity5 = Activity(name="Грузовые автомобили", parent_id=activity2.id)
    activity6 = Activity(name="Легковые автомобили", parent_id=activity2.id)
    session.add_all([activity3, activity4, activity5, activity6])
    session.commit()

    activity7 = Activity(name="Колбасы", parent_id=activity3.id)
    activity8 = Activity(name="Стейки", parent_id=activity3.id)
    activity9 = Activity(name="Творожная продукция", parent_id=activity4.id)

    session.add_all([activity7, activity8, activity9])
    session.commit()

    activity10 = Activity(name="Сырки", parent_id=activity9.id)
    session.add(activity10)
    session.commit()

    org1 = Organization(name="ООО Рога и Копыта", phone_numbers="2-222-222, 3-333-333, 8-923-666-13-13",
                        building_id=building1.id)
    org2 = Organization(name="ООО Пример", phone_numbers="3-333-333", building_id=building2.id)
    org3 = Organization(name="Apple", phone_numbers="323-333-333", building_id=building3.id)

    session.add_all([org1, org2, org3])
    session.commit()

    org_act1 = OrganizationActivity(organization_id=org1.id, activity_id=activity2.id)
    org_act2 = OrganizationActivity(organization_id=org1.id, activity_id=activity1.id)
    org_act3 = OrganizationActivity(organization_id=org2.id, activity_id=activity4.id)
    org_act4 = OrganizationActivity(organization_id=org3.id, activity_id=activity9.id)
    session.add_all([org_act1, org_act2, org_act3, org_act4])
    session.commit()

    session.close()


if __name__ == "__main__":
    add_mock_data()
