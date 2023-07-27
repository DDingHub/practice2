from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
from .models import Contest

url = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=20&gp="

def save_contest_data():
    for pageNum in range(1, 2):
        response = requests.get(url + str(pageNum))
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        wholeHtml = soup.find_all(class_="list")

        for tag in wholeHtml:
            for a_tag in tag:
                match = re.search(r'href="([^"]+)"', str(a_tag))
                if match:
                    href = "https://www.wevity.com/" + match.group(1)
                    href = href[-5:]
                    pageUrl = 'https://www.wevity.com/?c=find&s=1&gub=1&cidx=20&gbn=viewok&gp=1&ix=' + href

                    response2 = requests.get(pageUrl)
                    html_content2 = response2.text
                    soup2 = BeautifulSoup(html_content2, "html.parser")
                    dicttt = {}

                    h6_element = soup2.find("h6", class_="tit")
                    if h6_element:
                        dicttt['제목'] = h6_element.text

                    div_element = soup2.find(class_='thumb')
                    if div_element:
                        img_element = div_element.find('img')
                        if img_element:
                            src = img_element['src']
                            dicttt['사진'] = "https://www.wevity.com/" + src
                  
                    ul = soup2.find("ul", {"class": "cd-info-list"})
                    li = ul.select('li')

                    for i in range(8):
                        soup3 = BeautifulSoup(str(li[i]), 'html.parser')
                        span_element3 = soup3.find('span', class_='tit')
                        li_element3 = soup3.find('li')
                        if span_element3 and li_element3:
                            keyy = span_element3.text
                            field_text3 = li_element3.get_text(strip=True)
                            field_list3 = field_text3.split(keyy)[1].split(',')
                            fields4 = ', '.join([field.strip() for field in field_list3])
                            dicttt[keyy] = fields4

                    # 상세정보 추가
                    comm_desc_element = soup2.find("div", class_="comm-desc")
                    if comm_desc_element:
                        comm_desc_text = comm_desc_element.text.strip()
                        if isinstance(comm_desc_text, list):
                            comm_desc_text = ' '.join(comm_desc_text)
                        dicttt['상세정보'] = comm_desc_text

                    contest = Contest.objects.create(
                        title=dicttt.get('제목'),
                        photo=dicttt.get('사진'),
                        field=dicttt.get('분야'),
                        eligibility=dicttt.get('응모대상'),
                        organizer=dicttt.get('주최/주관'),
                        sponsorship=dicttt.get('후원/협찬'),
                        application_period=dicttt.get('접수기간'),
                        prize_total=dicttt.get('총 상금'),
                        prize_first=dicttt.get('1등 상금'),
                        website=dicttt.get('홈페이지'),
                        details=dicttt.get('상세정보')
                    )
                    contest.save()
                    

def contest_list(request):
    save_contest_data()  # 크롤링 데이터 저장
    contests = Contest.objects.all()
    return render(request, 'contest_list.html', {'contests': contests})
