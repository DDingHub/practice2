import "../UI/OutComp.css";
import "../UI/defaultItem.css";
import { useState } from "react";
const OutCompCard = (props) => {
  const [teamMatchingClicked, setTeamMatchingClicked] = useState(false);
  const getAddress = () => {
    props.onClick(props.id, teamMatchingClicked);
  };
  const teamMatchingHandle = () => {
    setTeamMatchingClicked(true);
    getAddress();
  };
  console.log("teamMatchingClicked1" + teamMatchingClicked);
  return (
    <div className="OutComp-card">
      <div className="OutComp-card-top ">
        <img
          className="OutComp-card-top-img"
          src={props.imgSrc}
          onClick={getAddress}
        />
        <div className="OutComp-card-top-main">
          {/* <img
            className="OutComp-card-top-bookmark"
            src="img/bookmark.svg"
          ></img> */}
          <div className="OutComp-card-top-main-bold" onClick={getAddress}>
            <div className="OutComp-card-top-main-bold-font">{props.title}</div>
          </div>
          <div className="OutComp-card-top-main-thin">
            <div className="OutComp-card-top-main-thin-font">
              {props.auspice}
            </div>
          </div>
          <div className="OutComp-card-top-main-dday">
            <div className="OutComp-card-top-main-dday-font">{props.day}</div>
          </div>
        </div>
      </div>
      <div className="OutComp-card-bottom">
        <div className="OutComp-card-bottom-left">
          <button
            className="wordButton OutComp-card-bottom-text"
            onClick={getAddress}
          >
            상세정보
          </button>
        </div>
        <div className="OutComp-card-bottom-right">
          <button
            className="wordButton OutComp-card-bottom-text"
            onClick={teamMatchingHandle}
          >
            팀원 구해요(0)
          </button>
        </div>
      </div>
    </div>
  );
};
export default OutCompCard;
