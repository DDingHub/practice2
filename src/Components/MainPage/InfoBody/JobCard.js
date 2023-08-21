import "./JobCard.css";
import { useState } from "react";

const JobCard = (props) => {
  const [buttonClicked, setButtonClicked] = useState();
  let job = "";
  if (props.text == "개발") {
    job = "dev";
  } else if (props.text == "기획") {
    job = "plan";
  } else if (props.text == "디자인") {
    job = "design";
  }
  const onChange = (e) => {
    props.onChange(e);
  };

  const onClick = () => {
    //색깔 변경하는 옵션
    setButtonClicked(true);
    props.isLeader(props.text);
  };
  return (
    <div className="JobCard">
      {/* <div className="JobCard-button" onClick={onClick}></div> */}
      <div className="JobCard-container">
        <div className="JobCard-container-job">{props.text} |</div>
        <input
          className="JobCard-container-input"
          name={`${job}_capacity`}
          value={props.formData[`${job}_capacity`]}
          onChange={onChange}
        ></input>
        <div className="JobCard-container-text">명</div>
      </div>
    </div>
  );
};
export default JobCard;
