import "./Buttons.css";
export const BlueButton = ({ width, height, onClick, text }) => {
  return (
    <div
      className="BlueButton"
      style={{ width: `${width}px`, height: `${height}px` }}
      onClick={onClick}
    >
      <div className="BlueButton-text">{text}</div>
    </div>
  );
};
export const BlueXButton = ({ width, height, onClick, text }) => {
  return (
    <div
      className="BlueXButton"
      style={{ width: `${width}px`, height: `${height}px` }}
      onClick={onClick}
    >
      <div className="BlueXButton-text">{text}</div>
      <img src="img/blueX.svg" className="BlueXButton-x" />
    </div>
  );
};
