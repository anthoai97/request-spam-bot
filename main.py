import requests
import random
from proxy_rotator import *
from user_agent import *
from threading import Thread
from tqdm import tqdm
 

THREAD_COUNT = 3

ip_addresses = [ "mysuperproxy.com:5000", "mysuperproxy.com:5001", "mysuperproxy.com:5100", "mysuperproxy.com:5010", "mysuperproxy.com:5050", "mysuperproxy.com:8080", "mysuperproxy.com:8001", 
"mysuperproxy.com:8000", "mysuperproxy.com:8050" ]

def proxy_request(request_type, url, **kwargs):
    while True:
        try:
            proxy = random.randint(0, len(ip_addresses) - 1)
            proxies = {"http": ip_addresses(proxy), "https": ip_addresses(proxy)}
            response = requests.get(request_type, url, proxies=proxies, timeout=5, **kwargs)
            print(f"Proxy currently being used: {proxy['https']}")
            break
        except:
            print("Error, looking for another proxy")
    return response
def send_request():
    proxies = {
        "http": "http://YOUR_SCRAPINGBEE_API_KEY:render_js=False&premium_proxy=True@proxy.scrapingbee.com:8886",
        "https": "https://YOUR_SCRAPINGBEE_API_KEY:render_js=False&premium_proxy=True@proxy.scrapingbee.com:8887"
    }

    response = requests.get(
        url="http://httpbin.org/headers?json",
        proxies=proxies,
        verify=False
    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
def callback():
    
    try:
        for i in range(200):
            region = random.choice(['us', 'de', 'sg', 'vn','ca'])
            proxy = proxy_generator(['us'])
            session = requests.Session()
            session.proxies = dict({'http': proxy})
            m_headers = {'User-Agent': generator_user_agent()}
            r = session.get('https://platform-qa.domain.sg', headers= m_headers)
            print(r)
            
    except KeyboardInterrupt:
        return
    
if __name__ == "__main__":
    threads = []
    for i in range(THREAD_COUNT):
        t = Thread(target=callback)
        threads.append(t)
        t.start()

 

    for t in threads:
        t.join()
    

    