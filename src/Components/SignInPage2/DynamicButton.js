import React, { useState } from "react";
import "./DynamicButton.css";

const DynamicButton = ({ size, text, onClick }) => {
  const [buttonClicked, setButtonClicked] = useState(false);

  const onButtonClicked = () => {
    setButtonClicked(!buttonClicked);
    if (onClick) {
      onClick(!buttonClicked); // 클릭 이벤트 발생 시, 상위 컴포넌트로 전달
    }
  };

  let buttonClass = buttonClicked ? "default-blue" : "default-gray";
  if (size === "big") {
    buttonClass = buttonClicked ? "big-blue" : "big-gray";
  }
  return (
    <div className={`DB-${size} ${buttonClass}`} onClick={onButtonClicked}>
      <div className={`DB-${size}-text`}>{text}</div>
    </div>
  );
};

export default DynamicButton;
