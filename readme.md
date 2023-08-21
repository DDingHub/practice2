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
