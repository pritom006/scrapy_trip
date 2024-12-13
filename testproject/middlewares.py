

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import requests
import random

from scrapy_selenium.middlewares import SeleniumMiddleware
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


class TestprojectSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class TestprojectDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# class DynamicProxyMiddleware:
#     def __init__(self):
#         self.proxy_list_url = "https://www.sslproxies.org/"  # Free proxy source
#         self.proxies = []

#     def fetch_proxies(self):
#         response = requests.get(self.proxy_list_url)
#         # Parse proxies from the response (e.g., using BeautifulSoup or regex)
#         # For simplicity, assuming a parsed list of proxies:
#         self.proxies = [
#             "http://123.123.123.123:8080",
#             "http://111.222.333.444:3128",
#         ]

#     def process_request(self, request, spider):
#         if not self.proxies:
#             self.fetch_proxies()
#         request.meta['proxy'] = random.choice(self.proxies)



# class CustomSeleniumMiddleware(SeleniumMiddleware):
#     def __init__(self, driver_name, driver_executable_path, driver_arguments):
#         self.driver_name = driver_name
#         options = Options()
#         for arg in driver_arguments:
#             options.add_argument(arg)
#         service = Service(driver_executable_path)

#         if driver_name == "chrome":
#             self.driver = Chrome(service=service, options=options)
#         else:
#             raise NotImplementedError(f"{driver_name} is not supported.")