import math

from .utils import get_soup
from .utils import now
from .utils import normalize_text

def parse_page(url, include_replies=False):
    """Parse a petition page

    It return parsed informations which is JSON format.
    It contains
      - 데이터 수집 시각
      - 상태 : [청원시작, 청원진행중, 청원종료, 브리핑]
      - 청원 개요
      - 청원 동의 수
      - 댓글

    :param url: str format html url
        for example, 'https://www1.president.go.kr/petitions/407329'
    :param include_replies: Boolean.
        If True, replies are included in return value.
        Default is False.
    """

    soup = get_soup(url)
    if not soup:
        raise ValueError('Exception: parse_page. soup is None')

    crawled_at = now()
    category, begin, end = parse_meta(soup)
    content = parse_content(soup)
    num_agree = parse_number_of_agree(soup)
    status = parse_status(soup)
    if include_replies:
        replies = get_replies(soup, url, num_agree)
    else:
        replies = None

    json_format = _as_json(crawled_at, category, begin,
        end, content, num_agree, status, replies)

    return json_format

def _as_json(crawled_at, category, begin, end,
    content, num_agree, status, replies):

    json_format = {
        'crawled_at' : crawled_at,
        'category' : category,
        'begin' : begin,
        'end' : end,
        'content' : content,
        'num_agree' : num_agree,
        'status' : status
    }

    if replies is None:
        return json_format

    json_format['replies'] = replies
    return json_format

def parse_meta(soup):
    meta = soup.select('ul[class=petitionsView_info_list] li')
    if not meta or len(meta) != 4:
        raise ValueError('Exception: parse_meta')
    category = meta[0].text.strip()[4:]
    begin = meta[1].text.strip()[4:]
    end = meta[2].text.strip()[4:]
    return category, begin, end

def parse_content(soup):
    content = soup.select('div[class=petitionsView_write] div[class=View_write]')
    if not content:
        return ''
    return normalize_text(content[0].text)

def parse_number_of_agree(soup):
    agree = soup.select('div[class=Reply_area_head] span')
    if not agree:
        return -1
    return int(agree[0].text)

def parse_status(soup):
    stage_names = '청원시작 청원진행중 청원종료 브리핑'.split()
    stages = soup.select('div[class=petitionsView_grapy] li')
    for stage, name in zip(stages, stage_names):
        if '현재 상태' in stage.text:
            return name
    return 'Exception'

def get_replies(soup, url, num_replies=0):
    replies = []
    num_pages = math.ceil(num_replies/10)
    for p in range(1, num_pages + 1):
        url_ = url + '?page=%d' % p
        soup_replies = get_soup(url_)
        replies += _parse_replies(soup_replies)
    return replies

def _parse_replies(soup):
    replies = soup.select('div[class=petitionsReply_Reply] li')
    if not replies:
        return []
    replies = [reply.select('div[class=R_R_contents_txt]') for reply in replies]
    replies = [reply[0].text.strip() for reply in replies if reply]
    return replies