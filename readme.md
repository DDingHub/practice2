pip install requests

# 로그인, 회원가입 /login /signup

{"username":"","password":""}

# 로그아웃 /logout

그냥 post하기

# 팀생성 /contest_id

{"name":"팀","teamname":"1","call":"1","detail":"1",
"dev_capacity": 1,"plan_capacity": 1,"design_capacity": 1}

# 팀 가입 /contest_id/team_id

{"jickgoon_type" : "dev"} #dev외에 plan 또는 design도 가능

# 팀원 수락또는 거절하기 /teamManagement/팀장user_id

{"application_id":1,"is_approved":"true"} #지원번호id, true or false

# 멤버 내보내기 /teamManagement/팀장user_id

{"team_id":1,"user_id":2}

# 교내 공모전 생성

{
"title": "",
"photo": "",
"field": "",
"eligibility": "",
"organizer": "",
"sponsorship": "",
"application_period": "",
"prize_total": "3",
"prize_first": "",
"website": "",
"details": "",
"isSchool":"true" #false로 할 시 교외 공모전으로 생성 됨
}

# userInfo/ -> 회원가입때 정보 받기 위한 곳

# mypage/ -> 팀 만들었을 때!

# 유형 모음

{
"nickname": "상경",
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
