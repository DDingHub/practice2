import "./TeamCard.css";
import { useState } from "react";
import React from "react";

const TeamCard = React.memo((props) => {
  // const [dev, setDev] = useState(props.dev);
  // const [plan, setPlan] = useState(props.plan);
  // const [design, setDesign] = useState(props.design);
  // const [dev_capacity, setDev_capacity] = useState(props.dev_capacity);
  // const [plan_capacity, setPlan_capacity] = useState(props.plan_capacity);
  // const [design_capacity, setDesign_capacity] = useState(props.design_capacity);

  const onClick = () => {
    props.handleTeamModalShow(true);
  };
  const Capacity = ({ status }) => {
    if (status === "dev") {
      return (
        <>
          {Array.from({ length: props.dev_capacity }, (_, index) => (
            <img key={index} src="img/voidFace.png" />
          ))}
        </>
      );
    } else if (status === "plan") {
      return (
        <>
          {Array.from({ length: props.plan_capacity }, (_, index) => (
            <img key={index} src="img/voidFace.png" />
          ))}
        </>
      );
    } else if (status === "design") {
      return (
        <>
          {Array.from({ length: props.design_capacity }, (_, index) => (
            <img key={index} src="img/voidFace.png" />
          ))}
        </>
      );
    }
    return null;
  };

  return (
    <div className="TeamCard" onClick={onClick}>
      <div className="TeamCard-text">
        <div className="TeamCard-text-bold">{props.name}</div>
        <div className="TeamCard-text-thin">Team {props.teamname}</div>
        {/* <img src="img/♡.svg"></img> 찜하기 버튼*/}
      </div>
      <div className="TeamCard-jobArea">
        <div className="TeamCard-jobArea-container">
          <div className="TeamCard-jobArea-container-name">개발</div>
          <div className="TeamCard-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              <Capacity status="dev" />
            </div>
          </div>
        </div>

        <div className="TeamCard-jobArea-container">
          <div className="TeamCard-jobArea-container-name">기획</div>
          <div className="TeamCard-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              <Capacity status="plan" />
            </div>
          </div>
        </div>

        <div className="TeamCard-jobArea-container">
          <div className="TeamCard-jobArea-container-name">디자인</div>
          <div className="TeamCard-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              <Capacity status="design" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
});

export default TeamCard;
