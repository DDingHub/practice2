import "./MakeTeamButton.css";

const MakeTeamButton = (props) => {
  const onClick = () => {
    props.handleModalShow(true);
  };

  //   const onClick = () => {

  //   };
  return (
    <div className="MakeTeamButton" onClick={onClick}>
      <img src="img/+.svg" />
      <div className="MakeTeamButton-text">팀 생성하기</div>
    </div>
  );
};
export default MakeTeamButton;
