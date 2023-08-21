import "./NVbar.css";
import "../UI/margin.css";
import "../UI/defaultItem.css";
import "../UI/logo.css";
import { Link } from "react-router-dom";
import Alarm from "./Alarm";

const NVbar = (props) => {
  console.log("getinfo: " + props.getInfo);
  console.log("getmyprofile: " + props.getMyProfile);
  const callSetMain = () => {
    props.setMain();
  };
  // const logout = () => {
  //   props.logout();
  // };
  //로그아웃 사용시 활성화
  // const profilePage = () => {};
  const goProfile = () => {
    props.goProfile();
  };
  const DDingHub = () => {
    return (
      <>
        {props.getInfo || props.getMyProfile ? (
          <>
            <img
              className="logo"
              src="img/logo.svg"
              alt="logo"
              onClick={callSetMain}
            ></img>
            <Link className="wordLink ml-10 ddingHub" onClick={callSetMain}>
              띵Hub
            </Link>
          </>
        ) : (
          <>
            <img className="logo" src="img/logo.svg" alt="logo"></img>
            <Link className="wordLink ml-10 ddingHub">띵Hub</Link>
          </>
        )}
      </>
    );
  };
  const Profile = () => {
    if (!props.loginState) {
      return (
        <Link to={"/LogInPage"} className="nvb-wordButtonFont wordLink">
          회원가입/로그인
        </Link>
      );
    } else {
      return (
        <>
          <Alarm />
          <img
            src="img/profile.svg"
            className="profile"
            // onClick={logout}
            //로그아웃 사용시 활성화
            // onClick={profilePage}
            onClick={goProfile}
          ></img>
        </>
      );
    }
  };
  return (
    <div className="nvb" style={{ position: "relative" }}>
      <div className="nvb-container">
        <div className="nvb-containerLeft">
          <DDingHub />
        </div>
        <div className="nvb-containerRight">
          {
            //검색기능
            /* <form className="nvb-searchForm">
            <input
              type="text"
              className="nvb-searchForm-input"
              placeholder="어떤 공모전을 찾으시나요?"
            ></input>
            <button type="submit" className="nvb-searchForm-submit">
              <img
                src="img/search.svg"
                alt="Submit Icon"
                className="nvb-searchForm-submit-icon"
              />
            </button>
          </form> */
          }
          <Profile />
        </div>
      </div>
    </div>
  );
};
export default NVbar;
