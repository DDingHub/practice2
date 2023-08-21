import "./Teams.css";
import JobCard from "./JobCard";
import axios from "axios";
import { useState, useRef, useEffect } from "react";
import { GrayBox } from "../UI/TextBox";
import { BlueXButton } from "../UI/Buttons";
import { FlexBox } from "../UI/FlexBox";

const MakeTeam = ({ handleModalShow, user, pageID }) => {
  const [tendencyList, setTendencyList] = useState([]);
  const tendencyRef = useRef();
  // const [tendencyListState, setTendencyListState] = useState(true);
  const [formData, setFormData] = useState({
    dev_capacity: "",
    plan_capacity: "",
    design_capacity: "",
    name: "",
    teamname: "",
    call: "",
    detail: "",
    contest_id: pageID + 1,
    tendency: [],
    created_by: user,
  });
  // useEffect(() => {
  //   setFormData((prevData) => ({
  //     ...prevData,
  //     // tendency: JSON.stringify(tendencyList),
  //   }));
  // }, [tendencyList]);

  useEffect(() => {
    setTendencyList([]);
  }, [handleModalShow]);
  const handleButtonClick = () => {
    const inputValue = tendencyRef.current.value;

    if (inputValue.trim() !== "") {
      setTendencyList((prevList) => [...prevList, inputValue]);
      tendencyRef.current.value = ""; // tendencyRef 초기화
      // setTendencyListState(!tendencyList);
    }
  };
  const modalClose = () => {
    handleModalShow(false);
    // setTendencyListState(true);
    setTendencyList([]);
  };
  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

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
        formData
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
          created_by: "",
          tendencyList: [],
        });

        // 요청 성공 시 수행할 작업
        console.log(response.data); // 서버 응답 데이터 출력
      })
      .catch((error) => {
        // 요청 실패 시 수행할 작업
        console.error(error);
      });

    // 여기서 폼 데이터를 백엔드로 전송합니다 (Axios 또는 다른 네트워크 요청 라이브러리 사용).
    console.log("폼 데이터:", formData);

    // 제출 후에 필요하다면 폼을 초기화합니다.
  };
  // const isLeaderHandle = () => {
  //   //리더의 역할군
  //   setFormData((prevData) => ({ ...prevData, isLeader: text }));
  // };

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
        <div className="mT-container-input-big">
          <div className="mT-container-input-big-text">
            우리 팀에 대한 자세한 설명을 작성해 주세요. (- 프로젝트 시기 - 공통
            목표 - 주 회의 장소 - 구하는 팀원 포지션)
          </div>
          <textarea
            className="mT-container-input-big-input"
            name="detail"
            value={formData.detail}
            onChange={handleChange}
          ></textarea>
        </div>

        <div className="mT-container-title">직군 별 모집 인원</div>
        <div className="mT-container-title-explain">
          팀장 자신의 직군을 선택하고 직군 별 모집 인원을 입력해주세요.
        </div>
        <div className="mT-container-jobContainer">
          <input
            type="radio"
            name="leaderJob"
            className="jobCard-button"
            value={formData.leaderJob}
            onChange={handleChange}
          ></input>
          <JobCard
            text="개발"
            onChange={handleChange}
            formData={formData}
          ></JobCard>
          <input
            type="radio"
            name="leaderJob"
            className="jobCard-button"
            value={formData.leaderJob}
            onChange={handleChange}
          ></input>
          <JobCard
            text="기획"
            onChange={handleChange}
            formData={formData}
          ></JobCard>
          <input
            type="radio"
            name="leaderJob"
            className="jobCard-button"
            value={formData.leaderJob}
            onChange={handleChange}
          ></input>
          <JobCard
            text="디자인"
            onChange={handleChange}
            formData={formData}
          ></JobCard>
        </div>
        <div className="mT-container-title">
          우리 팀은 이런 성향이 모였어요!
        </div>

        <input
          className="mT-container-input-tendency"
          placeholder="성향을 입력해주세요.(최대 12자)"
          ref={tendencyRef}
        ></input>
        <button
          type="button"
          className="mT-container-input-tendency-button"
          onClick={handleButtonClick}
        >
          추가
        </button>

        <FlexBox dir="row">
          {
            // tendencyListState
            //   ? null
            //   :
            tendencyList.map((item) => (
              <BlueXButton text={item} />
            ))
          }
        </FlexBox>

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
export default MakeTeam;
