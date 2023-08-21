import "./TextButton.css";

export default function TextButton({
  onClick,
  text1,
  text2,
  buttonStat,
  statChange,
}) {
  let C = 0,
    S = 0,
    W = 0,
    H = 0,
    R = 0,
    P = 0;

  const countStat = (stat) => {
    if (stat === "C") {
      return (C += 1), stat;
    } else if (stat === "S") {
      return (S += 1), stat;
    } else if (stat === "W") {
      return (W += 1), stat;
    } else if (stat === "H") {
      return (H += 1), stat;
    } else if (stat === "R") {
      return (R += 1), stat;
    } else if (stat === "P") {
      return (P += 1), stat;
    }
  };

  const clickHandler = () => {
    onClick();
    statChange(buttonStat);
    // console.log(C, S, W, H, R, P);
  };
  return (
    <div className="TextButton" onClick={clickHandler}>
      <div className="TextButton-text">
        <div>{text1}</div>
        <div>{text2}</div>
      </div>
      <img src="img/rightArrow.svg" />
    </div>
  );
}
