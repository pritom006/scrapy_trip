from testproject.pipelines import TestprojectPipeline
from testproject.items import TestprojectItem
from unittest.mock import Mock, patch
import os

def test_process_item():
    pipeline = TestprojectPipeline()
    mock_spider = Mock()
    mock_spider.settings.get = lambda x, default=None: "sqlite:///:memory:"

    pipeline.open_spider(mock_spider)

    # Mock item
    item = TestprojectItem(
        hotelName="Hotel Test",
        rating="5.0",
        location="Test Location",
        latitude="12.34",
        longitude="56.78",
        price="200",
        imageUrl="http://example.com/image.jpg"
    )

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.iter_content = lambda x: [b"data"]

        processed_item = pipeline.process_item(item, mock_spider)

    assert processed_item["hotelName"] == "Hotel Test"
    assert processed_item["rating"] == "5.0"