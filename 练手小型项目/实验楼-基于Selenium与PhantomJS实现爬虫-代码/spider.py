import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
results = []
def parse(response):
    for comment in response.css('div.comment-list-item'):
        result = {
            'username':comment.xpath('.//div[2]/div[1]/a/text()').extract_first().strip(),
            'content':comment.xpath('.//div[2]/div[contains(@class, "comment-item-content")]/p/text()').extract_first().strip()
        }
        print(result)
        results.append(result)

def has_next_page(response):
    next_page = response.xpath('//ul[@class="pagination"]/li[@class="next-page"]')
    nstatus = next_page.extract_first()
    print(nstatus)
    return True if next_page.xpath('.//@class') else False

def goto_next_page(driver):
    next_button = driver.find_element_by_xpath('//*[@id="comments"]/div/div[4]/ul/li[7]/a')
    next_button.click()

def wait_page_return(driver, page):
    print('wait start {}'.format(page))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
        )
    )
    print('wait end {}'.format(page))

def spider():
    driver = webdriver.PhantomJS()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1
    while True:
        wait_page_return(driver, page)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)
        if not has_next_page(response):
            break
        page += 1
        goto_next_page(driver)
    with open('/home/shiyanlou/comments.json', 'w') as f:
        f.write(json.dumps(results))


if __name__ == '__main__':
    spider()
