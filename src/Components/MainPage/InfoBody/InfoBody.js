import "./InfoBody.css";
import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import React from "react";
import Teams from "./Teams";

const InfoBody = ({ pageID, user, teamMatchingClicked }) => {
  // const [teamData, setTeamData] = useState([]);

  const [data, setData] = useState(null);
  const [teamMatching, setTeamMatching] = useState(false);
  // const [modal, setModal] = useState(false);
  // const handleModalShow = (status) => {
  //   setModal(status);
  // };
  useEffect(() => {
    async function getData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/acontest-list/"
        );
        setData(response.data[pageID]);
      } catch (error) {
        throw new Error("Error fetching data:", error);
      }
    }
    getData();
  }, [pageID]);

  // console.log("데이터임:" + JSON.stringify(data));
  console.log("인포의 페이지아이디임" + pageID);
  // console.log("로그인된 유저" + user.id);
  if (data === null) {
    return <div>Loading...</div>;
  }
  const day = data.application_period.substring(
    data.application_period.indexOf("D")
  );
  const detailsArr = data.details.split(/(!|\?|\■|\*|\-|\※)/).filter(Boolean);
  const formattedDetails = detailsArr.map((item, index) => {
    if (
      item === "!" ||
      item === "?" ||
      // item === "." ||
      item === "■" ||
      item === "*"
    ) {
      return (
        <React.Fragment key={index}>
          {/* <br /> */}
          <span>{item}</span>
        </React.Fragment>
      );
    } else {
      return <div key={index}>{item}</div>;
    }
  });
  const FormattedDetails = () => {
    return <>{formattedDetails}</>;
  };

  const ClickLeft = () => {
    setTeamMatching(false);
  };
  const ClickRight = () => {
    setTeamMatching(true);
  };
  console.log("teamMatchingClicked5" + teamMatchingClicked);
  return (
    <div className="InfoBody">
      <div className="InfoBody-bar">
        <div className="InfoBody-bar-dday">
          <div className="InfoBody-bar-dday-text">{day}</div>
        </div>
        <div className="InfoBody-bar-title">{data.title}</div>
      </div>
      <div className="InfoBody-container">
        <div className="InfoBody-container-top">
          <img src={data.photo} className="InfoBody-container-img"></img>
          <div className="InfoBody-container-infoCard">
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                공모분야
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.field}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                응모대상
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.eligibility}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                주최주관
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.organizer}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                후원/협찬
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.sponsorship}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                접수기간
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.application_period.slice(0, -4)}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                총 상금
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.prize_total}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                1등 상금
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.prize_first}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock">
              <div className="InfoBody-container-infoCard-textBlock-Bold">
                홈페이지
              </div>
              <div className="InfoBody-container-infoCard-textBlock-thin">
                {data.website}
              </div>
            </div>
            <div className="InfoBody-container-infoCard-textBlock-Bold">
              공유하기
            </div>
            <Link
              to={"https://url.kr/xjoaiz"}
              className="InfoBody-container-infoCard-button"
              style={{ textDecoration: "none" }}
            >
              <div className="InfoBody-container-infoCard-button-text">
                홈페이지 지원
              </div>
            </Link>
          </div>
        </div>
        <div className="InfoBody-container-bottom">
          <div className="InfoBody-container-bottom-bar">
            <div
              className={`InfoBody-container-bottom-bar-moreInfo ${
                !teamMatching ? "IB-blue" : "IB-gray"
              }`}
              onClick={ClickLeft}
            >
              <div className="InfoBody-container-bottom-bar-moreInfo-text">
                상세내용
              </div>
            </div>
            <div
              className={`InfoBody-container-bottom-bar-moreInfo ${
                teamMatching ? "IB-blue" : "IB-gray"
              }`}
              onClick={ClickRight}
            >
              <div className="InfoBody-container-bottom-bar-team-text">
                팀원 구해요
              </div>
            </div>
          </div>
          <div className="InfoBody-container-bottom-deepInfo">
            {!teamMatching && !teamMatchingClicked ? (
              <FormattedDetails />
            ) : (
              <Teams pageID={pageID} user={user} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
export default InfoBody;
