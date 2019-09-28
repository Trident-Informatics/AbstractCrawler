import time as systime
import requests
import random
from stem import Signal
from stem.control import Controller


'''
The abstract crawler which is going to guide its descendants mine the data which it itself cannot
Such descendants of the crawler are to implement the annotated ```@abstractmethod``` functions accordingly and may override other methods accordingly as well
The abstract crawler guides the descendant crawlers to be implemented in such a manner but does not restrict them of trying new ways of implementing themselves as well

However, the crawler strongly advices its descendants to follow these guidelines:
    - The crawler prefers all the functions to be commented in Google style for the future usage and maintainability
    - Name all the functions in simple letters with underscore seperated words (For the readabilty ofcourse, because the crawler is too lazy)
    - Descendants (class names) shall be named just like the ```AbstractCrawler``` itself (Just to confirm that it is a real descendant and not adopted)

authors:
    - Oshan Mendis (@Oshan96)


TODO: File write functions need to be implemented
'''
class AbstractCrawler:

    '''
    AbstractCrawler is a web crawler which needs to be inherited and built according to your needs

    Args: 
        url_list (list): The list of URLs of the pages which needs to be crawled
        tor_pass: password set in torrc file
        DEFAULT_TIME_OUT (int): Crawler sleeps after each web page is crawled for the given time period (in seconds)
    
    Attributes:
        url_list (list): Stores the given URL list
        tor_pass (str): Crawler uses tor so the password stated in the torrc file needs to be passed
        session (Session): Stores the session object which is going to be used
        DEFAULT_TIME_OUT (int): Stores the given time out period (in seconds)
        user_agents (list): List of user agents which can be used to rotate the user-agent of the request header
        proxies (dictionary): proxies which are going to be used for the session

    '''
    def __init__(self, url_list, tor_pass, DEFAULT_TIME_OUT = 5):
        self.url_list = url_list
        self.tor_pass = tor_pass
        self.DEFAULT_TIME_OUT = DEFAULT_TIME_OUT

        self.user_agents = [
            #Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            #Firefox
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        ]

        self.proxies = {
                      'http': 'socks5://127.0.0.1:9050',
                      'https': 'socks5://127.0.0.1:9050'
        }

        self.session = self.get_new_session()


    '''
    Creates a new session for crawling

    Returns:
        session: The newly created session object
    '''
    def get_new_session(self):
        self.renew_connection()
        session = requests.Session()
        session.proxies = self.proxies

        session.headers.update ({
            'User-Agent:',get_random_user_agent()
        })

        return session


    '''
    Renew connection
    '''
    def renew_connection(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password = tor_pass)
            controller.signal(Signal.NEWNYM)


    '''
    Get a random user-agent from user_agents

    Returns:
        user_agent: a random user_agent string from the user_agents list
    '''
    def get_random_user_agent(self):
        return random.choice(self.user_agents)
    

    '''
    The crawling web page details (html) needs to be parsed accordingly. This is an abstract method which needs to be implemented accordingly

    Args:
        link (str): A URL from the url_list
    
    Returns:
        parsedWebPage: HTML parsed object of the given web page
    
    '''
    @abstractmethod
    def parse(self, url):
        pass
    

    '''
    The crawler crawls through the URLs it has been feeded with, with a DEFAULT_TIME_OUT timeout period. And needs to be implemented accordingly
    This implementation of the function calls ```parse(link)``` and gets the HTML parsed object and calls ```scrape(page)``` function and extracts the data
        of that page and appends the result to the list. This process is continued until the last page with timeouts (as per DEFAULT_TIME_OUT value)

    Returns:
        all_extracted_data (list): Returns all the extracted data from all the webpages

    '''
    def crawl_url_list(self):
        all_extracted_data = []

        for url in self.url_list:
            web_page = parse(url)
            scraped_details = scrape(web_page)

            all_extracted_data.append(scraped_details)

            systime.sleep(DEFAULT_TIME_OUT)

        return all_extracted_data

    '''
    The crawler scrapes the data out of the given web page as it is instructed. Needs to be implemented accordingly

    Args:
        web_page (object): A HTML parsed object of the web page
    
    Returns:
        scraped_data (dictionary): scraped data of the web page

    '''
    @abstractmethod
    def scrape(self, web_page):
        pass
    

    


    



