# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy only requirements first (to leverage Docker layer caching)
COPY testproject/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set the default command to start the Scrapy spider
CMD ["scrapy", "crawl", "trip"]
