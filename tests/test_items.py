from testproject.items import TestprojectItem

def test_item_fields():
    item = TestprojectItem()
    fields = ["hotelName", "rating", "location", "latitude", "longitude", "roomName", "price", "imageUrl", "city_id"]
    for field in fields:
        assert field in item.fields