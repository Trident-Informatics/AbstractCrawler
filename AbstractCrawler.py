import time as systime

'''
The abstract crawler which is going to guide its descendants mine the data which it itself cannot
Such descendants of the crawler are to implement the annotated ```@abstractmethod``` functions accordingly and may override other methods accordingly as well
The abstract crawler guides the descendant crawlers to be implemented in such a manner but does not restrict them of trying new ways of implementing themselves as well

However, the crawler strongly advices its descendants to follow these guidelines:
    - The crawler prefers all the functions to be commented in Google style for the future usage and maintainability
    - Name all the functions in simple letters with underscore seperated words (For the readabilty ofcourse, because the crawler is too lazy)
    - Descendants (class names) shall be named just like the ```AbstractCrawler``` himself (Just to confirm that it is a real descendant and not adopted)

authors:
    - Oshan Mendis (@Oshan96)

'''
class AbstractCrawler:

    '''
    AbstractCrawler is a web crawler which needs to be inherited and built according to your needs

    Args: 
        url_list (list): The list of URLs of the pages which needs to be crawled
        DEFAULT_TIME_OUT (int): Crawler sleeps after each web page is crawled for the given time period (in seconds)
    
    Attributes:
        url_list (list): Stores the given URL list
        DEFAULT_TIME_OUT (int): Stores the given time out period (in seconds)

    '''
    def __init__(self, url_list, DEFAULT_TIME_OUT = 5):
        self.url_list = url_list
        self.DEFAULT_TIME_OUT = DEFAULT_TIME_OUT
    

    '''
    The crawling web page details (html) needs to be parsed accordingly. This is an abstract method which needs to be implemented accordingly

    Args:
        link (str): A URL from the url_list
    
    Returns:
        parsedWebPage: HTML parsed object of the given web page
    
    '''
    @abstractmethod
    def parse(url):
        pass
    

    '''
    The crawler crawls through the URLs it has been feeded with, with a DEFAULT_TIME_OUT timeout period. And needs to be implemented accordingly

    '''
    def crawl_url_list():
        systime.sleep(DEFAULT_TIME_OUT)
        for url in self.url_list:
            web_page = parse(url)
            scrape(web_page)
    

    '''
    The crawler scrapes the data out of the given web page as it is instructed. Needs to be implemented accordingly

    Args:
        web_page (object): A HTML parsed object of the web page
    
    Returns:
        scraped_data (dictionary): scraped data of the web page

    '''
    @abstractmethod
    def scrape(web_page):
        pass


    



