import { useEffect, useState } from "react";
import "./ProfileBody.css";
import axios from "axios";
const ProfileBody = (props) => {
  const [profile, setProfile] = useState();
  console.log("유저아이디임" + props.user);
  axios
    .post(`http://127.0.0.1:8000/api/user-profiles/`, props.user)
    .then((response) => {
      setProfile(response.data);
      console.log("프로필데이터" + JSON.stringify(profile));
    })
    .catch((error) => {});

  useEffect(() => {
    async function getProfile() {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/user-profiles/"
      );
      setProfile(response.data);
    }
    getProfile();
    console.log("프로필데이터" + JSON.stringify(profile));
  }, []);

  return (
    <div className="pb-background">
      <div className="pb-container">
        <div className="pb-container-left">
          <strong>{`${profile.name}님의 프로필`} </strong>
          <img src="img/face.svg"></img>
          <div className="pb-container-left-name">{profile.name} </div>
          <div className="pb-container-left-major">{profile.department}</div>
        </div>
        <div className="pb-container-right">
          <div className="pb-container-right-selfIntroduce">
            <strong>이런 사람이에요</strong>
            <div className="pb-container-right-selfIntroduce-line"></div>
            <div className="pb-container-right-selfIntroduce-text">
              간단 소개글 칸에 쓴 내용 <br></br>프론트앤드 개발자
              누구누구입니당~ 어떤어떤 공모전에서 어떤 활약을 했고~~
            </div>
          </div>
          <div className="pb-container-right-testResult">
            <img src="img/애널리스트.png"></img>
          </div>
          <div className="pb-container-right-portfolio">
            {profile.introduction}
          </div>
          <div className="pb-container-right-contact">
            <strong>여기로 연락주세요!</strong>
            <div className="pb-container-right-contact-text">
              {profile.contact_info}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default ProfileBody;
