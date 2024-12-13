
# useful for handling different item types with a single interface
import os
import requests
from itemadapter import ItemAdapter

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the SQLAlchemy Base
Base = declarative_base()

# Define the Quote model to match the scraped data
# class Quote(Base):
#     __tablename__ = 'quotes'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     text = Column(String, nullable=False)
#     author = Column(String, nullable=False)
#     tags = Column(String, nullable=True)  # Store tags as a comma-separated string

# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String, nullable=False)
#     price = Column(String, nullable=False)
#     availability = Column(String, nullable=False)


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    rating = Column(Float, nullable=True)
    location = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    room_type = Column(String, nullable=True)
    price = Column(String, nullable=True)
    # images = Column(String, nullable=True)

class TestprojectPipeline:
    def open_spider(self, spider):
        print("Opening database connection...")
        self.engine = create_engine(spider.settings.get('DATABASE_URL'))
        Base.metadata.create_all(self.engine)  # Create tables if they don't exist
        self.Session = sessionmaker(bind=self.engine)
        # self.image_dir = os.path.join(spider.settings.get("FILES_STORE", "./images"))
        # os.makedirs(self.image_dir, exist_ok=True)

    def close_spider(self, spider):
        self.engine.dispose()

    def process_item(self, item, spider):
        print(f"Processing item: {item}")
        adapter = ItemAdapter(item)
        session = self.Session()

        # Save images
        # image_paths = []
        # for image_url in adapter.get("images", []):
        #     image_name = os.path.basename(image_url)
        #     image_path = os.path.join(self.image_dir, image_name)
        #     response = requests.get(image_url, stream=True)
        #     if response.status_code == 200:
        #         with open(image_path, "wb") as f:
        #             for chunk in response.iter_content(1024):
        #                 f.write(chunk)
        #         image_paths.append(image_path)

        # Save to database
        property_data = Property(
            title=adapter.get("title"),
            rating=adapter.get("rating"),
            location=adapter.get("location"),
            latitude=adapter.get("latitude"),
            longitude=adapter.get("longitude"),
            room_type=adapter.get("room_type"),
            price=adapter.get("price"),
            # images=",".join(image_paths),
        )
        session.add(property_data)
        session.commit()
        session.close()
        return item

        # Handle different models based on spider
        # if spider.name == "books":
        #     book = Book(
        #         title=item['title'],
        #         price=item['price'],
        #         availability=item['availability']
        #     )
        #     session.add(book)
        # elif spider.name == "quotes":
        #     quote = Quote(
        #         text=item['text'],
        #         author=item['author'],
        #         tags=",".join(item['tags'])
        #     )
        #     session.add(quote)
        # session.commit()
        # session.close()
        # return item