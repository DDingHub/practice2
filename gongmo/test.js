import axios from "axios";
import MakeTeamButton from "./MakeTeamButton";
import TeamCard from "./TeamCard";
import { useState, useEffect } from "react";
import Modal from "../../../Modal";
import ModalPortals from "../../../ModalPortals";
import "./Teams.css";
import JobCard from "./JobCard";

const Teams = ({ pageID, user }) => {
  const [teamData, setTeamData] = useState([]);
  const [contestData, setContestData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState(false);
  //초기폼 생성
  const [formData, setFormData] = useState({
    dev_capacity: "",
    plan_capacity: "",
    design_capacity: "",
    name: "",
    teamname: "",
    call: "",
    detail: "",
    dev: "",
    plan: "",
    design: "",
    contest: "",
  });
  //팝업 보여줌
  const handleModalShow = (status) => {
    setModal(status);
  };

  useEffect(() => {
    async function getTeamData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/${pageID + 1}/`
        );
        setTeamData(response.data.teams);
        setContestData(response.data.contest);
        setLoading(false);
      } catch (error) {
        throw new Error("Error fetching data:", error);
      }
    }
    if (loading) {
      getTeamData();
    }
  }, [loading]);

  const makePost = () => {
    const posts = [];
    if (!teamData) {
      return posts;
    }
    //나열해서 보여주기 위한 foreach
    teamData.forEach((item) => {
      //   let day = item.application_period;
      //   day = day.substring(day.indexOf("D"));
      console.log("아이템임" + JSON.stringify(item));
      let post = {
        dev_capacity: item.dev_capacity,
        plan_capacity: item.plan_capacity,
        design_capacity: item.design_capacity,
        name: item.name,
        teamname: item.teamname,
        call: item.call,
        detail: item.detail,
        // dev: item.dev,
        // plan: item.plan,
        // design: item.design,
        // contest: item.contest,
        // user: item.user,
      };
      console.log("team낱개로보여주기" + JSON.stringify(post));
      console.log("받아온 팀데이터입니다" + JSON.stringify(teamData));
      console.log("받아온 콘테스트데이터입니다" + JSON.stringify(contestData));
      posts.push(post);
    });

    return posts;
  };
  const teams = makePost();
  if (loading) {
    return <div>Loading...</div>;
  }

  const MakeTeam = () => {
    // const [foamData, setFormData] = useState({
    //   name: "",
    //   teamname: "",
    //   call: "",
    //   detail: "",
    //   dev_capacity: "",
    //   plan_capacity: "",
    //   design_capacity: "",
    // });
    const modalClose = () => {
      handleModalShow(false);
    };
    const handleChange = (event) => {
      const { name, value } = event.target;
      setFormData((prevData) => ({ ...prevData, [name]: value }));
    };
    const handleSubmit = (event) => {
      event.preventDefault();

      const requestData = {
        ...formData,
        contest: pageID + 1,
        created_by: user.id, // 로그인한 사용자의 ID를 전달
      };

      axios
        .post(
          `http://127.0.0.1:8000/${pageID + 1}/`,
          // name: "asdf",
          // teamname: "asdf",
          // call: "asdfasdf",
          // detail: "asdf",
          // plan_capacity: "3",
          // dev_capacity: "12",

          // design_capacity: "1",
          requestData
        )
        .then((response) => {
          setFormData({
            dev_capacity: "",
            plan_capacity: "",
            design_capacity: "",
            name: "",
            teamname: "",
            call: "",
            detail: "",
            // dev: "",
            // plan: "",
            // design: "",
            // contest: "",
            // created_by: "",
          });

          // 요청 성공 시 수행할 작업
          console.log(response.data); // 서버 응답 데이터 출력
        })
        .catch((error) => {
          // 요청 실패 시 수행할 작업
          console.error(error);
        });

      // 여기서 폼 데이터를 백엔드로 전송합니다 (Axios 또는 다른 네트워크 요청 라이브러리 사용).
      console.log("폼 데이터:", requestData);

      // 제출 후에 필요하다면 폼을 초기화합니다.
    };

    console.log("로그인된 유저" + user);
    return (
      <div className="mT-container">
        <div className="mT-container-bar">
          <img src="img/greenface.svg"></img>
          <div className="mT-container-bar-text">
            <img src="img/crown.svg" className="mT-container-bar-img" />
            <div className="mT-container-bar-text-bold">닉네임</div>
            <div className="mT-container-bar-text-thin">디지털콘텐츠학과</div>
          </div>
        </div>
        <div className="mT-container-line"></div>
        <form onSubmit={handleSubmit}>
          <div className="mT-container-title">제목</div>
          <input
            className="mT-container-input"
            placeholder="제목"
            name="name"
            value={formData.name}
            onChange={handleChange}
          ></input>
          <div className="mT-container-title">팀명</div>
          <input
            className="mT-container-input"
            placeholder="팀명"
            name="teamname"
            value={formData.teamname}
            onChange={handleChange}
          ></input>
          <div className="mT-container-title">연락 수단</div>
          <input
            className="mT-container-input "
            placeholder="예) 인스타 아이디 / 메일 / 오픈 채팅 "
            name="call"
            value={formData.call}
            onChange={handleChange}
          ></input>
          <div className="mT-container-title">팀 소개 글</div>
          <input
            className="mT-container-input-big"
            placeholder="우리 팀에 대한 자세한 설명을 작성해 주세요.&#10;
                &#10;- 프로젝트 시기&#10;- 공통 목표&#10;- 주 회의 장소&#10;- 구하는 팀원 포지션"
            name="detail"
            value={formData.detail}
            onChange={handleChange}
          ></input>
          <div className="mT-container-title">직군 별 모집 인원</div>
          <div className="mT-container-title-explain">
            팀장 자신의 직군을 선택하고 직군 별 모집 인원을 입력해주세요.
          </div>
          <div className="mT-container-jobContainer">
            <JobCard
              text="개발"
              onChange={handleChange}
              formData={formData}
            ></JobCard>
            <JobCard
              text="기획"
              onChange={handleChange}
              formData={formData}
            ></JobCard>
            <JobCard
              text="디자인"
              onChange={handleChange}
              formData={formData}
            ></JobCard>
          </div>
          <div className="mT-container-submit-container">
            <button
              className="mT-container-submit"
              typeOf="submit"
              onClick={modalClose}
            >
              팀 생성하기
            </button>
          </div>
        </form>
      </div>
    );
  };

  return (
    <div className="teamContainer">
      {teams.map((team) => (
        <TeamCard key={team.id} {...team} />
      ))}
      <MakeTeamButton handleModalShow={handleModalShow} />
      <ModalPortals>
        <Modal
          contents={MakeTeam()}
          show={modal}
          k
          handleModalShow={handleModalShow}
        />
      </ModalPortals>
    </div>
  );
};

export default Teams;
