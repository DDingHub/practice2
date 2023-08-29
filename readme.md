pip install requests

# 회원가입 /signup

{
"username": "a",
"password": "a",
"job":["응"],
"hobby":["응응"],
"dream":["응응응"],
"tendency_worktime":"응응응",
"tendency_personality": ["응"],
"tendency_MBTI": "응",
"email":"a@mju.ac.kr",
"major":"데이터테크놀로지",
"nickname":"해준",
"call":"비밀",
"languages_tools":["파이썬"],
"introduce":"바보아니다",
"portfolio":"https://github.com/DDingHub/practice2",
"user_type":"커뮤니케이터",
"type_message":"우리 팀의 소통은 내가 책임진다!"
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
"type": "컨트롤타워",
"type_src": "img/컨트롤타워.png",
"type_message": "나를 따르라!",
"type_hashtag": "#자신감 #결단력 #지배력",
"type_explain1": "프로젝트를 이끌며 팀원들의 열정까지 이끌어내는 사람",
"type_explain2": "끈기를 가지고 팀원들을 다독이며 원하는 목표를 달성해내요.",
"type_explain3": "자신의 주장을 단호하게 밀고 나갈 수 있는 결단력이 있고, 사람들을 설득해나가는 능력이 있어요.",
"type_explain4": "가끔 반대 의견에 대해서는 감정적인 면모를 보이는 편이에요.",
"type_best": "애널리스트",
"type_best_message": "내가 집중하면 모두가 놀랄걸?",
"type_best_src": "img/애널리스트.png",
"type_worst": "디테일리스트",
"type_worst_message": "꼼꼼함이 나의 무기!",
"type_worst_src": "img/디테일리스트.png"
}

{
"type": "커뮤니케이터",
"type_src": "img/커뮤니케이터.png",
"type_message": "우리 팀의 소통은 내가 책임진다!",
"type_hashtag": "#남들을 보살핌 #너그러움",
"type_explain1": "팀의 분위기를 좋게 만드는 윤활유 역할을 하는 사람",
"type_explain2": "사람들의 말을 잘 듣고, 잘 전달해주는 큰 포용력을 가졌어요.",
"type_explain3": "자신보다 팀의 니즈를 우선시 하고, 조직의 유대관계를 끈끈하게 만드는 능력이 있어요.",
"type_explain4": "팀에 불화가 있어 관계가 개선되지 않을 경우 감정적으로 불안해지는 편이에요.",
"type_best": "중재가",
"type_best_message": "이 구역의 정의의 여신은 나!",
"type_best_src": "img/중재가.png",
"type_worst": "애널리스트",
"type_worst_message": "내가 집중하면 모두가 놀랄걸?",
"type_worst_src": "img/애널리스트.png"
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
"type_worst_src": "img/커뮤니케이터.png"
}

{
"type": "불도저",
"type_src": "img/불도저.png",
"type_message": "뭐든지 도전하고 봐! 재밌잖아~",
"type_hashtag": "#쾌활 #충동적 #성취 지향적",
"type_explain1": "빠르고 기만한 두뇌로 적극적으로 프로젝트를 이끌어 나가는 사람",
"type_explain2": "모험심이 강해서 리스크에 책임을 지는 것을 두려워하지 않으며, 에너지가 넘쳐 팀 분위기를 끌어올려요.",
"type_explain3": "새로운 아이디어를 생각하면서 만족감을 얻으며, 다양한 문제에 유연하게 대처할 수 있는 능력을 가지고 있어요.",
"type_explain4": "반복적인 업무를 하다 보면 스트레스를 많이 받을 수 있어 끊임없이 새로운 일을 찾는 것을 추천해요.",
"type_best": "목표 달성자",
"type_best_message": "목표한 것은 꼭 지키고야 말겠어!",
"type_best_src": "img/목표달성자.png",
"type_worst": "프로세서",
"type_worst_message": "시켜만 줘! 최강창민메타",
"type_worst_src": "img/프로세서.png"
}

{
"type": "디테일리스트",
"type_src": "img/디테일리스트.png",
"type_message": "꼼꼼함이 나의 무기!",
"type_hashtag": "#이성적 #원칙적 #자기관리",
"type_explain1": "프로젝트 맡은 일은 완벽하게 해내는 팀원들이 신뢰하고 인정하는 사람",
"type_explain2": "높은 사명감과 특별한 목적의식을 가지고 일을 진행하는 편이에요.",
"type_explain3": "문제가 생기면 원인을 찾아 스스로를 이해시키고 채찍질하며, 더 완벽한 일처리를 위해 노력해요.",
"type_explain4": "안정적인 일 처리와 깔끔한 마무리로 인정받고 싶어하는 경향이 있어요.",
"type_best": "프로세서",
"type_best_message": "시켜만 줘! 최강창민메타",
"type_best_src": "img/프로세서.png",
"type_worst": "컨트롤타워",
"type_worst_message": "나를 따르라!",
"type_worst_src": "img/컨트롤타워.png"
}

{
"type": "중재가",
"type_src": "img/중재가.png",
"type_message": "이 구역의 정의의 여신은 나!",
"type_hashtag": "#수용적 #편안 #만족",
"type_explain1": "스스로 확실한 목표를 가지고 자신만의 타임라인과 프로세스를 만들어 묵묵히 해내가는 사람",
"type_explain2": "팀원들의 긴장감을 완화시키며, 침착하게 일을 진행할 수 있는 분위기를 만들어요.",
"type_explain3": "뒤에서 팀을 서포트하면서 안정적인 팀 상태를 유지하는 능력을 가지고 있어요.",
"type_explain4": "멀리서 관망하는 것보다 조금 더 적극적인 방법을 모색하는 걸 추천해요.",
"type_best": "커뮤니케이터",
"type_best_message": "우리 팀의 소통은 내가 책임진다!",
"type_best_src": "img/커뮤니케이터.png",
"type_worst": "목표 달성자",
"type_worst_message": "목표한 것은 꼭 지키고야 말겠어!",
"type_worst_src": "img/목표달성자.png"
}

{
"type": "목표 달성자",
"type_src": "img/목표달성자.png",
"type_message": "목표한 것은 꼭 지키고야 말겠어!",
"type_hashtag": "#목표와 가치 #빠른 일 진행 #성과",
"type_explain1": "언제나 성공과 목표를 위해 힘껏 달려가는 사람",
"type_explain2": "목표 달성을 위해서라면 모든 방법을 총동원할 줄 알아요.",
"type_explain3": "팀에서 스스로 가치를 높일 수 있는 부분을 찾아내 계발하는 편이에요.",
"type_explain4": "자신의 성과에 만족하지 못하는 성향으로 자신에게 조금 더 관대해지는건 어떠세요?",
"type_best": "불도저",
"type_best_message": "뭐든지 도전하고 봐! 재밌잖아~",
"type_best_src": "img/불도저.png",
"type_worst": "중재가",
"type_worst_message": "이 구역의 정의의 여신은 나!",
"type_worst_src": "img/중재가.png"
}

{
"type": "프로세서",
"type_src": "img/프로세서.png",
"type_message": "시켜만 줘! 최강창민메타",
"type_hashtag": "#책임감 #안정감 #붙임성 있음",
"type_explain1": "전체적인 체계와 프로세스,방향성이 정해져 있을 때 최고의 아웃풋을 가지는 사람",
"type_explain2": "정해진 가이드라인이 있다면 프로젝트를 효과적으로 운영하는 편이에요.",
"type_explain3": "강한 책임감으로 팀원들에게 든든한 기둥과 같은 안정감을 줘요.
",
"type_explain4": "불확실한 부분을 스스로 결정할 때에 부담감을 느끼는 경향이 있어요.",
"type_best": "디테일리스트",
"type_best_message": "꼼꼼함이 나의 무기!",
"type_best_src": "img/디테일리스트.png",
"type_worst": "불도저",
"type_worst_message": "뭐든지 도전하고 봐! 재밌잖아~",
"type_worst_src": "img/불도저.png"
}
