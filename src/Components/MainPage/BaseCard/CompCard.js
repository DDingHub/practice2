import "./BaseCard.css";

const CompCard = (props) => {
  // props.defaultProps = {
  //   dday: dayjs("2023-07-18"),
  //   title: "sw경진대회",
  //   auspice: "ict융합대학",
  // };
  // const ddayCalculator = () => {
  //   const isFutureDate = props.day.isAfter(dayjs());
  //   const daysDiff = props.day.diff(dayjs(), "day");
  //   return <div>{isFutureDate ? daysDiff.toString() : "d-day"}</div>;
  // };

  const getAddress = () => {
    props.onClick(props.id);
  };
  return (
    <div className="comp-slider-main-card">
      <div className="comp-slider-main-card-img-container">
        <img
          className="comp-slider-main-card-img"
          src={props.imgSrc}
          onClick={getAddress}
        />
        <div className="comp-slider-main-card-img-dday">
          <div className="comp-slider-main-card-img-dday-text">{props.day}</div>
        </div>
      </div>

      <div className="comp-slider-main-card-text">
        <div className="comp-slider-main-card-text-bold" onClick={getAddress}>
          {props.title}
        </div>
        <div className="comp-slider-main-card-text-thin">{props.auspice}</div>
      </div>
    </div>
  );
};
export default CompCard;
