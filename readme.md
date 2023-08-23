pip install requests

# 회원가입 /signup

{
"username": "e",
"password": "e",
"job":["응"],
"hobby":["응응"],
"dream":["응응응"],
"tendency_worktime":"응응응",
"tendency_personality": ["응"],
"tendency_MBTI": "응",
"email":"e@mju.ac.kr",
"major":"데이터테크놀로지"
}

# 로그인 /login

{
"username": "a",
"password": "a"
}

# 로그아웃 /logout

그냥 post하기

# 팀생성 /contest_id

{"name":"팀","teamname":"1","call":"1","detail":"1",
"dev_capacity": 1,"plan_capacity": 1,"design_capacity": 1,"leaderJickgoon":"dev"}

# 팀 가입 /contest_id/team_id

{"jickgoon_type" : "dev"} #dev외에 plan 또는 design도 가능

# 팀원 수락또는 거절하기 /teamManagement/팀장user_id

{"application_id":1,"is_approved":"true"} #지원번호id, true or false

# 멤버 내보내기 /teamManagement/팀장user_id

{"team_id":1,"user_id":2}

# 교내 공모전 모음

{
"title": "MJU 기업분석 경진대회",
"photo": "img/교내2.jpg",
"field": "취업,분석",
"eligibility": "재학생",
"organizer": "용인지역대학일자리협회",
"sponsorship": "자연진로취업지원팀,대학혁신지원사업",
"application_period": "2023-06-21 ~ 2023-08-07D+17",
"prize_total": ".",
"prize_first": ".",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

{
"title": "창의적 SW프로그램 경진대회",
"photo": "img/경진대회표지.jpg",
"field": "IT/기획/디자인/개발",
"eligibility": "ICT소속 재학생",
"organizer": "ict융합대학",
"sponsorship": ".",
"application_period": "2023-06-07 ~ 2023-06-16D+69",
"prize_total": "100만원",
"prize_first": "100만원",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

{
"title": "명지대학교 YOUTUBE 영상 공모전",
"photo": "img/교내3.jpg",
"field": ".",
"eligibility": ".",
"organizer": "대외협력 홍보팀",
"sponsorship": ".",
"application_period": "2023-07-10 ~ 2023-08-31D-7",
"prize_total": ".",
"prize_first": ".",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

{
"title": "나만의 학UP비법",
"photo": "img/교내4.jpg",
"field": ".",
"eligibility": ".",
"organizer": "대학교육혁신원 교육개발센터",
"sponsorship": ".",
"application_period": "2023-06-15 ~ 2023-06-25D+60",
"prize_total": ".",
"prize_first": ".",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

{
"title": "명지C.C",
"photo": "img/교내5.jpg",
"field": ".",
"eligibility": ".",
"organizer": "대학교육혁신원 교육개발센터",
"sponsorship": ".",
"application_period": "2023-04-27 ~ 2023-05-07D+109",
"prize_total": ".",
"prize_first": ".",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

{
"title": "IDEA공모전",
"photo": "img/교내6.jpg",
"field": ".",
"eligibility": ".",
"organizer": "대학교육혁신원 교육개발센터",
"sponsorship": ".",
"application_period": "2023-04-05 ~ 2023-04-19D+127",
"prize_total": ".",
"prize_first": ".",
"website": "https://www.mju.ac.kr/bbs/mjukr/146/200413/artclView.do",
"details": ".",
"isSchool": true,
"viewCount": 0
}

# 유형 모음

{
"type": "애널리스트",
"type_src": "url",
"type_message": "내가 집중하면 모두가 놀랄걸?",
"type_hashtag": "#혁신적 #지각 능력 #독창적 연구 #4차원",
"type_explain1": "고도의 집중력과 문제 해결 능력이 뛰어난 사람",
"type_explain2": "독립적으로 문제를 해결할 때 만족감을 느끼며, 다양한 정보를 통해 호기심을 해결하려고 해요.",
"type_explain3": "새로운 시각으로 문제를 바라보며 해결할 수 있는 능력을 가지고 있어요.",
"type_explain4": "팀 내 경쟁보다 새로운 길을 찾는데 더 많은 관심을 갖고 있어 가끔 현실과 동떨어진 결과를 내기도 해요.",
"type_best": "컨트롤타워",
"type_best_message": "나를 따르라!",
"type_best_src": "url",
"type_worst": "커뮤니케이터",
"type_worst_message": "우리 팀의 소통은 내가 책임진다!",
"type_worst_src": "url"
}

{
"type": "애널리스트",
"type_src": "img/애널리스트.png",
"type_message": "내가 집중하면 모두가 놀랄걸?",
"type_hashtag": "#혁신적 #지각 능력 #독창적 연구 #4차원",
"type_explain1": "고도의 집중력과 문제 해결 능력이 뛰어난 사람",
"type_explain2": "독립적으로 문제를 해결할 때 만족감을 느끼며, 다양한 정보를 통해 호기심을 해결하려고 해요.",
"type_explain3": "새로운 시각으로 문제를 바라보며 해결할 수 있는 능력을 가지고 있어요.",
"type_explain4": "팀 내 경쟁보다 새로운 길을 찾는데 더 많은 관심을 갖고 있어 가끔 현실과 동떨어진 결과를 내기도 해요.",
"type_best": "컨트롤타워",
"type_best_message": "나를 따르라!",
"type_best_src": "img/컨트롤타워.png",
"type_worst": "커뮤니케이터",
"type_worst_message": "우리 팀의 소통은 내가 책임진다!",
"type_worst_src": "img/커뮤니케티어.png"
}
