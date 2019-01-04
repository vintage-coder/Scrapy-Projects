from AdvancedSpider.utils import get_random_agent



BOT_NAME = 'AdvancedSpider'

SPIDER_MODULES = ['AdvancedSpider.spiders']
NEWSPIDER_MODULE = 'AdvancedSpider.spiders'


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
print("========================")
print(USER_AGENT)

ROBOTSTXT_OBEY = True
DOWNLOAD_MAXSIZE=3000000

# AJAXCRAWL_ENABLED = True
TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_HOST = '127.0.0.1'

TELNETCONSOLE_PORT = [6023,6073]

AUTOTHROTTLE_ENABLED = True

# FEED_FORMAT='csv'
# FEED_URI='aibot1.csv'

# CONCURRENT_REQUESTS = 32
# TELNETCONSOLE_ENABLED = False
# DOWNLOAD_DELAY = 3
ITEM_PIPELINES = {
   'AdvancedSpider.pipelines.AdvancedspiderPipeline': 300,
   'AdvancedSpider.pipelines.UrlStoragePipeline':300,
}

SPIDER_MIDDLEWARES = {
   'AdvancedSpider.middlewares.AdvancedspiderSpiderMiddleware': 543,
}
#
DOWNLOADER_MIDDLEWARES = {
   'AdvancedSpider.middlewares.AdvancedspiderDownloaderMiddleware': 543,
}

































































































































































#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False


# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'AdvancedSpider.middlewares.AdvancedspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'AdvancedSpider.pipelines.AdvancedspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
