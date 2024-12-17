# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


BOT_NAME = "testproject"

SPIDER_MODULES = ["testproject.spiders"]
NEWSPIDER_MODULE = "testproject.spiders"

DATABASE_URL = "postgresql+psycopg2://scrapy_user:scrapy_password@postgres:5432/scrapy_db"


# Obey robots.txt rules
ROBOTSTXT_OBEY = True



# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'testproject.pipelines.TestprojectPipeline': 300,
}





DOWNLOADER_MIDDLEWARES = {
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
}



FILES_STORE = "./images"

DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS = 4

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 30
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]
