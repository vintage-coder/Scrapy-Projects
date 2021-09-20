# *Scrapy-Projects*
# A Sample Web Crawler or Spider to scrape the Website using Scrapy Frame Work

> Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

# Basic Concepts

1. Command line tool

2. Spiders

3. Selectors

4. Scrapy shell

5. Items

6. Item Loaders

7. Item Pipeline

8. Feed exports

9. Requests and Responses

10. Link Extractors

11. Settings

12. Exceptions


## 1. Scrapy Architecture Overview
![scrapy_architecture](https://github.com/vintage-coder/Scrapy-Projects/blob/master/Scrapy%20Details/scrapy_architecture_01.png?raw=true){width=200px}

The data flow in Scrapy is controlled by the execution engine, and goes like this:

1. The Engine gets the initial Requests to crawl from the Spider.

2. The Engine schedules the Requests in the Scheduler and asks for the next Requests to crawl.

3. The Scheduler returns the next Requests to the Engine.

4. The Engine sends the Requests to the Downloader, passing through the Downloader Middlewares (see process_request()).

5. Once the page finishes downloading the Downloader generates a Response (with that page) and sends it to the Engine, passing through the Downloader Middlewares (see      process_response()).

6. The Engine receives the Response from the Downloader and sends it to the Spider for processing, passing through the Spider Middleware (see process_spider_input()).

7. The Spider processes the Response and returns scraped items and new Requests (to follow) to the Engine, passing through the Spider Middleware (see process_spider_output()).

8. The Engine sends processed items to Item Pipelines, then send processed Requests to the Scheduler and asks for possible next Requests to crawl.

9. The process repeats (from step 1) until there are no more requests from the Scheduler.

## 2. Web Crawler vs Web Scraper
![crawler_scraper](https://github.com/vintage-coder/Scrapy-Projects/blob/master/Scrapy%20Details/scraping%20vs%20crawling.png)

## 3. Components in Scrapy Framework
![abrevations](https://github.com/vintage-coder/Scrapy-Projects/blob/master/Scrapy%20Details/scrapy_abrevation.png)

# Components
## Scrapy Engine
The engine is responsible for controlling the data flow between all components of the system, and triggering events when certain actions occur.

## Scheduler
The Scheduler receives requests from the engine and enqueues them for feeding them later (also to the engine) when the engine requests them.

## Downloader
The Downloader is responsible for fetching web pages and feeding them to the engine which, in turn, feeds them to the spiders.

## Spiders
Spiders are custom classes written by Scrapy users to parse responses and extract items from them or additional requests to follow.

## Item Pipeline
The Item Pipeline is responsible for processing the items once they have been extracted (or scraped) by the spiders. Typical tasks include cleansing, validation and persistence (like storing the item in a database). For more information see Item Pipeline.

## Downloader middlewares
Downloader middlewares are specific hooks that sit between the Engine and the Downloader and process requests when they pass from the Engine to the Downloader, and responses that pass from Downloader to the Engine.

Use a Downloader middleware if you need to do one of the following:

- process a request just before it is sent to the Downloader (i.e. right before Scrapy sends the request to the website);

- change received response before passing it to a spider;

- send a new Request instead of passing received response to a spider;

- pass response to a spider without fetching a web page;

- silently drop some requests.



## Spider middlewares
Spider middlewares are specific hooks that sit between the Engine and the Spiders and are able to process spider input (responses) and output (items and requests).

Use a Spider middleware if you need to

- post-process output of spider callbacks - change/add/remove requests or items;

- post-process start_requests;

- handle spider exceptions;

- call errback instead of callback for some of the requests based on response content.



### To install scrapy use the following command

```pip3 install scrapy```


[For more information visit scrapy.org](https://scrapy.org/)
