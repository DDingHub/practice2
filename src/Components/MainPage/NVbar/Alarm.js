import "./NVbar.css";
import { useState } from "react";

const Alarm = () => {
  const [isToggle, setIsToggle] = useState(false);
  return (
    <>
      {isToggle ? (
        <div>
          <img
            src="img/alarm.svg"
            className="alarm"
            onClick={() => setIsToggle(!isToggle)}
          ></img>
        </div>
      ) : (
        <div className="blueCircle">
          <img
            src="img/whiteAlarm.svg"
            className="alarm-act"
            onClick={() => setIsToggle(!isToggle)}
          ></img>
        </div>
      )}
    </>
  );
};
export default Alarm;
