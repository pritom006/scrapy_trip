



import scrapy
import json
import re
from testproject.items import TestprojectItem


class TripSpider(scrapy.Spider):
    name = "trip"
    allowed_domains = ["uk.trip.com"]
    start_urls = [
        "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP"
    ]

    def parse(self, response):
        # Extract the script containing JSON data
        json_script = response.xpath(
            "//script[contains(text(), 'window.IBU_HOTEL')]/text()"
        ).get()

        if json_script:
            self.log("Found script containing `window.IBU_HOTEL` data.")
            # Extract JSON-like data from the script using regex
            match = re.search(r"window\.IBU_HOTEL\s*=\s*(\{.*?\});", json_script, re.DOTALL)
            if match:
                try:
                    # Parse the extracted JSON string
                    data = json.loads(match.group(1))

                    # Access the desired data
                    htls_data = data.get("initData", {}).get("htlsData", {})
                    if htls_data:
                        inbound_hotels = htls_data.get("inboundCities", [])
                        if inbound_hotels:
                            city = inbound_hotels[0]
                            city_id = city.get("id", "")
                            city_url = f"https://uk.trip.com/hotels/list?city={city_id}"
                            yield scrapy.Request(url=city_url, callback=self.parse_hotels, meta={'city_id': city_id})
                        else:
                            self.logger.error("No 'inboundCities' found in 'htlsData'.")
                      
                    else:
                        self.logger.error("No 'htlsData' found in 'initData'.")
                except Exception as e:
                    self.logger.error(f"Error parsing JSON data: {e}")
            else:
                self.logger.error("Regex did not match any 'window.IBU_HOTEL' data.")
        else:
            self.logger.error("No script containing 'window.IBU_HOTEL' found.")


    def parse_hotels(self, response):
        city_id = response.meta['city_id']
        json_script = response.xpath(
            "//script[contains(text(), 'window.IBU_HOTEL')]/text()"
        ).get()

        if json_script:
            self.log("Found script containing `window.IBU_HOTEL` data.")
            # Extract JSON-like data from the script using regex
            match = re.search(r"window\.IBU_HOTEL\s*=\s*(\{.*?\});", json_script, re.DOTALL)
            if match:
                try:
                    # Parse the extracted JSON string
                    data = json.loads(match.group(1))

                    # Access the desired data
                    htls_data = data.get("initData", {}).get("firstPageList", {}).get("htlsData", [])
                    for hotel in htls_data:
                        hotel_data = {
                            "hotelName": hotel.get("hotelBasicInfo", {}).get("hotelName", ""),
                            "rating": hotel.get("commentInfo", {}).get("commentScore", ""),
                            "location": hotel.get("positionInfo", {}).get("positionName", ""),
                            # "latitude": hotel.get("lat", "N/A"),
                            # "longitude": hotel.get("lon", "N/A"),
                            "roomName": hotel.get("roomInfo", {}).get("physicalRoomName", ""),
                            "price": hotel.get("hotelBasicInfo", {}).get("price", ""),
                            "city_id": city_id
                            #"imageUrl": hotel.get("imgUrl", "N/A")
                        }
                        yield hotel_data
                except Exception as e:
                    self.logger.error(f"Error parsing JSON data: {e}")
            else:
                self.logger.error("Regex did not match any 'window.IBU_HOTEL' data.")
        else:
            self.logger.error("No script containing 'window.IBU_HOTEL' found.")

