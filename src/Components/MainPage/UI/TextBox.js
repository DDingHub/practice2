import "./TextBox.css";
export const GrayTag = ({ text }) => {
  return (
    <div className="GrayTag">
      <div className="GrayTag-text">{text}</div>
    </div>
  );
};

export const GrayBox = ({ text }) => {
  return (
    <div className="GrayBox">
      <div className="GrayBox-text">{text}</div>
    </div>
  );
};
