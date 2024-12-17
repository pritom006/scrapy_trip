
# useful for handling different item types with a single interface
import os
import requests
from itemadapter import ItemAdapter

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from .models import Property, Base




class TestprojectPipeline:
    def open_spider(self, spider):
        print("Opening database connection...")
        self.engine = create_engine(spider.settings.get('DATABASE_URL'))
        Base.metadata.create_all(self.engine)  # Create tables if they don't exist
        self.Session = sessionmaker(bind=self.engine)
        self.image_dir = os.path.join(spider.settings.get("FILES_STORE", "./images"))
        os.makedirs(self.image_dir, exist_ok=True)

    def close_spider(self, spider):
        self.engine.dispose()

    def process_item(self, item, spider):
        print(f"Processing item: {item}")
        adapter = ItemAdapter(item)
        session = self.Session()

        # Save images
        image_url = adapter.get("imageUrl")  # Use 'images' or 'imageUrl' based on your field name
        image_paths = []
        if image_url:
            image_name = os.path.basename(image_url)
            image_path = os.path.join(self.image_dir, image_name)
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(image_path, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                image_paths.append(image_path)

        # Save to database
        property_data = Property(
            title=adapter.get("hotelName"),
            rating=adapter.get("rating"),
            location=adapter.get("location"),
            latitude=adapter.get("latitude"),
            longitude=adapter.get("longitude"),
            room_type=adapter.get("roomName"),
            price=adapter.get("price"),
            images=",".join(image_paths) if image_paths else None
        )
        session.add(property_data)
        session.commit()
        session.close()
        return item

        
