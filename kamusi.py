import os
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class Kamusi(Model):
    """
    Represents a Swahili-English dictionary entry.

    Attributes:
        id (int): Unique identifier for the entry.
        sw (str): Swahili word.
        en (str): English description.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
    """
    id = fields.IntField(pk=True)  # Primary key for the entry
    sw = fields.TextField(description="Swahili word")  # Swahili word
    en = fields.TextField(description="English description")  # English description
    created_at = fields.DatetimeField(auto_now_add=True, null=False)  # Creation timestamp
    updated_at = fields.DatetimeField(auto_now=True, null=False)  # Last update timestamp

    class Meta:
        table = "kamusi"  # Database table name for this model
        table_description = "Swahili-English dictionary"  # Description of the table

    def __str__(self):
        return self.name  # Human-readable representation of a Kamusi entry


async def run():
    passwd = os.getenv('KAMUSI_PASS')
    await Tortoise.init(db_url="mysql://kamusi:"+passwd+"@localhost:3306/kamusi", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    # Create
    event = await Kamusi.create(sw="nani", en="what")

    # Udpate
    await Kamusi.filter(id=event.id).update(en="what (interrogative)")

    # Read
    print(await Kamusi.all().values("id", "sw", "en", "updated_at", "created_at"))

    # Delete
    await Kamusi.filter(id=event.id).delete()

    print(await Kamusi.all().values("id", "sw", "en", "updated_at", "created_at"))

if __name__ == "__main__":
    run_async(run())
