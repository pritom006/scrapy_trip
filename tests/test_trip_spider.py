import scrapy
from scrapy.http import HtmlResponse, Request
from testproject.spiders.trip import TripSpider

def test_parse():
    # Sample HTML response containing a mock JSON script
    html_content = """
    <html>
        <head><title>Test Trip</title></head>
        <body>
            <script>
                window.IBU_HOTEL = {
                    "initData": {
                        "htlsData": {
                            "inboundCities": [{"id": "123", "name": "London"}],
                            "outboundCities": [{"id": "456", "name": "Paris"}]
                        }
                    }
                };
            </script>
            <h3>Heading 1</h3>
            <h3>Heading 2</h3>
        </body>
    </html>
    """

    # Create a mock response
    response = HtmlResponse(url="https://uk.trip.com/hotels/", body=html_content, encoding='utf-8')

    # Instantiate the spider
    spider = TripSpider()
    results = list(spider.parse(response))

    # Test that a Scrapy request is returned
    assert len(results) == 1
    assert isinstance(results[0], scrapy.Request)
    assert "list?city=" in results[0].url

def test_parse_hotels():
    # Sample JSON response with mock hotel data
    html_content = """
    <html>
        <script>
            window.IBU_HOTEL = {
                "initData": {
                    "firstPageList": {
                        "hotelList": [
                            {
                                "hotelBasicInfo": {"hotelName": "Hotel ABC", "price": "100", "hotelImg": "img.jpg"},
                                "commentInfo": {"commentScore": "4.5"},
                                "positionInfo": {
                                    "positionName": "Location ABC",
                                    "coordinate": {"lat": "51.5074", "lng": "0.1278"}
                                },
                                "roomInfo": {"physicalRoomName": "Deluxe"}
                            }
                        ]
                    }
                }
            };
        </script>
    </html>
    """

    # Mock the request with meta data
    request = Request(
        url="https://uk.trip.com/hotels/list?city=123", 
        meta={"city_id": "123", "city_name": "London"}
    )

    # Mock the response with the request
    response = HtmlResponse(
        url="https://uk.trip.com/hotels/list?city=123", 
        body=html_content, 
        encoding='utf-8',
        request=request
    )

    # Instantiate the spider
    spider = TripSpider()
    results = list(spider.parse_hotels(response))

    # Test the output item
    assert len(results) == 1
    item = results[0]
    assert item["hotelName"] == "Hotel ABC"
    assert item["rating"] == "4.5"
    assert item["location"] == "Location ABC"
    assert item["latitude"] == "51.5074"
    assert item["longitude"] == "0.1278"
    assert item["roomName"] == "Deluxe"
    assert item["price"] == "100"
    assert item["imageUrl"] == "img.jpg"
    assert item["city_id"] == "123"
    
