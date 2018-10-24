# 청와대 국민청원 수집기

청와대 국민청원 (https://www1.president.go.kr/petitions) 홈페이지에 올라온 청원의 내용 / 공감 개수 / 댓글을 수집합니다.

## Usage

### 청원 목록 가져오기

청와대 청원 게시판의 최근 청원 목록을 가져옵니다. 최근 청원 목록의 begin_page 부터 end_page 까지의 목록을 가져옵니다.

    from petitions_scrapper import get_petition_links

    links = get_petition_links(begin_page=1, end_page=3)

links 는 (카테고리, 제목, url) 의 tuple 로 이뤄져 있습니다.

    [('기타', '정유사, 주유소 특별감사해주세요', 'https://www1.president.go.kr/petitions/320810'),
     ('인권/성평등', "청주 '여중생 집단 폭행 사건'은 쌍방 폭행…10명 입건 ...", 'https://www1.president.go.kr/petitions/320809'),
     ('기타', '제발 가정내 폭력 심각하게 봐 주십시요', 'https://www1.president.go.kr/petitions/320808'),
     ('안전/환경', '정당방위 성립요건 개정 부탁드립니다.', 'https://www1.president.go.kr/petitions/320807'),
      ...
    ]

### 하나의 청원 페이지에서 정보 가져오기

parse_page 함수에 청원 페이지의 url 을 입력하면 아래의 정보들을 수집할 수 있습니다.

| 항목 | 설명 |
| --- | --- |
| begin | 청원 시작일 |
| category | 청원 카테고리 (외교, 국방, 경제 등) |
| content | 청원 내용 |
| crawled_at | 수집 시각 |
| end | 청원 종료일 |
| num_agree | 수집 시각의 청원 동의 수 |
| replies | 청원 댓글 |
| status | 현재 청원 진행 상황 (청원시작, 청원진행중, 청원종료, 브리핑) |

    from petitions_scrapper import parse_page

    url = 'https://www1.president.go.kr/petitions/407329'
    parse_page(url)

    {'begin': '2018-10-15',
     'category': '경제민주화',
     'content': '금융위원회가 공모주 개인배정 축소(폐지)로 개인의 공모주 참여를 차단하려고 합니다 이와같은 금융위원회의 공모주 개인배정 축소(폐지)는 영세 개인 사업자의 골목상권을 빼앗아 가는 횡포와 같습니다. 이같은 행위는기업의 경제적 이익을 위해 개인의 밥그릇을 빼앗는 것으로 서민의 생계를 위협하는 처사입니다. 작금의 어려운 서민경제에서 가계에 조금이라도 보탬이 되고자 하는 개인 공모주 참여를 계속할 수 있도록 공모주 개인 배정 물량을 지금과 같이 할 수 있도록 꼭꼭 지켜주십시오.',
     'crawled_at': '2018-10-15 10:27:18',
     'end': '2018-11-14',
     'num_agree': 9,
     'status': '청원진행중'}

parse_page 함수의 include_replies=True 로 설정하면 청원의 댓글을 함께 수집합니다.

    parse_page(url, include_replies=True)

    {'begin': '2018-10-15',
     'category': '경제민주화',
     'content': '금융위원회가 공모주 개인배정 축소(폐지)로 개인의 공모주 참여를 차단하려고 합니다 이와같은 금융위원회의 공모주 개인배정 축소(폐지)는 영세 개인 사업자의 골목상권을 빼앗아 가는 횡포와 같습니다. 이같은 행위는기업의 경제적 이익을 위해 개인의 밥그릇을 빼앗는 것으로 서민의 생계를 위협하는 처사입니다. 작금의 어려운 서민경제에서 가계에 조금이라도 보탬이 되고자 하는 개인 공모주 참여를 계속할 수 있도록 공모주 개인 배정 물량을 지금과 같이 할 수 있도록 꼭꼭 지켜주십시오.',
     'crawled_at': '2018-10-15 10:27:24',
     'end': '2018-11-14',
     'num_agree': 9,
     'replies': ['동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.',
      '동의합니다.'],
     'status': '청원진행중'}

### 청원 카테고리 살펴보기

현재 청원 게시판에 등록되어 있는 카테고리를 살펴볼 수 있습니다.

    from petitions_scrapper import show_categories

    show_categories()

    idx = 0  , name = 전체
    idx = 35 , name = 정치개혁
    idx = 36 , name = 외교/통일/국방
    idx = 37 , name = 일자리
    idx = 38 , name = 미래
    idx = 39 , name = 성장동력
    idx = 40 , name = 농산어촌
    idx = 41 , name = 보건복지
    idx = 42 , name = 육아/교육
    idx = 43 , name = 안전/환경
    idx = 44 , name = 저출산/고령화대책
    idx = 45 , name = 행정
    idx = 46 , name = 반려동물
    idx = 47 , name = 교통/건축/국토
    idx = 48 , name = 경제민주화
    idx = 49 , name = 인권/성평등
    idx = 50 , name = 문화/예술/체육/언론
    idx = 51 , name = 기타