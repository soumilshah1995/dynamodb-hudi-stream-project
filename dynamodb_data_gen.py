try:
    import uuid
    from datetime import datetime
    import os
    import uuid

    from faker import Faker
    import pynamodb.attributes as at
    from pynamodb.models import Model
    from pynamodb.attributes import *
    from time import sleep
    from dotenv import load_dotenv

    load_dotenv(".env")
except Exception as e:
    raise Exception("Error : {}".format(e))


class OLTP(Model):
    class Meta:
        table_name = os.getenv("DYNAMO_DB_TABLE_NAME")
        region = os.getenv("DEV_AWS_REGION_NAME")
        aws_access_key_id = os.getenv("DEV_AWS_ACCESS_KEY")
        aws_secret_access_key = os.getenv("DEV_AWS_SECRET_KEY")

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    city = UnicodeAttribute()
    state = UnicodeAttribute()

class Datetime(object):
    @staticmethod
    def get_year_month_day_hour_minute_seconds():
        """
        Return Year month and day
        :return: str str str
        """
        dt = datetime.now()
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour
        minute = dt.minute
        seconds = dt.second
        return year, month, day, hour, minute,


class DataGenerator(object):

    @staticmethod
    def get_data():
        faker = Faker()

        name = faker.name().split(" ")
        first_name = name[0]
        last_name = name[1]
        address = faker.address()
        text = faker.text()
        id = uuid.uuid4().__str__()
        city = faker.city()
        state = faker.state()
        _ = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "text": text,
            "id": id,
            "city": city,
            "state": state
        }

        return _


def generate_data():
    for i in range(1, 20):
        json_data = DataGenerator.get_data()
        print(json_data)
        OLTP(
            pk=f'orderid#{json_data.get("id")}',
            sk=f'orderid#{json_data.get("id")}',
            city=json_data.get("city"),
            state=json_data.get("state"),
        ).save()
        time.sleep(5)


generate_data()
