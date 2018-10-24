import time
from .config import SLEEP
from .config import VERBOSE
from .utils import get_soup

def get_petition_links(begin_page=1, end_page=10):

    def parse_link(li):
        category = li.select('div[class^=bl_category]')[0].text[2:].strip() # remove '분류'
        petition_num = int(li.select('div[class=bl_no]')[0].text[2:].strip()) # remove '번호'
        title = li.select('a')[0].text[2:].strip() # remove '제목'
        url = 'https://www1.president.go.kr/petitions/%d' % petition_num
        return (category, title, url)

    links = []
    for p in range(begin_page, end_page + 1):
        url = 'https://www1.president.go.kr/petitions?page={}'.format(p)

        try:
            soup = get_soup(url)
        except:
            print('\nException while getting soup page=%d' % p)

        div = soup.select('div[class^=board]')
        for li in soup.select('div[class^=b_list] div[class=bl_body] li'):
            try:
                link = parse_link(li)
                links.append(link)
            except:
                continue

        if p % 50 == 0:
            time.sleep(SLEEP)
        time.sleep(0.8) # default sleep

        if VERBOSE:
            print('\rget petitions links from {} in ({} - {}) pages'.format(
                p, begin_page, end_page), end='')
            if p % 100 == 0:
                print()

    print('\ngetting petition links was done')
    return links