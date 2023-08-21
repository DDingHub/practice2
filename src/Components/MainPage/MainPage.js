import BaseCard from "./BaseCard/BaseCard";
import Footer from "./Footer/Footer";
import NVbar from "./NVbar/NVbar";
import InfiniteSlider from "./Carousel/InfiniteSlider";
import { useEffect, useState } from "react";
import InfoBody from "./InfoBody/InfoBody";
import ProfileBody from "./ProfileBody/ProfileBody";

const MainPage = ({ loginState, user }) => {
  const [teamMatchingClicked, setTeamMatchingClicked] = useState(false);
  const [getInfo, setGetInfo] = useState(false);
  const [getMyProfile, setGetMyProfile] = useState(false);
  const [pageID, setPageID] = useState(0);
  window.scrollTo(0, 0);
  const info = (id, teamMatchingClicked) => {
    setGetInfo(true);
    setPageID(id - 1);
    setTeamMatchingClicked(teamMatchingClicked);
  };

  const setMain = () => {
    setGetInfo(false);
    setGetMyProfile(false);
  };
  // const logout = () => {
  //   props.setLoginState(false);
  //   //loginstate를 false로 변경
  // };
  //로그아웃 사용시 활성화

  useEffect(() => {
    console.log("페이지아이디임", pageID);
  }, [pageID]); // pageID가 변경될 때마다 로그 출력
  const goProfile = () => {
    setGetMyProfile(true);
    console.log("프로필 호출됨");
  };
  console.log("teamMatchingClicked4" + teamMatchingClicked);
  return (
    <>
      <NVbar
        getInfo={getInfo}
        setMain={setMain}
        loginState={loginState}
        // logout={logout}
        //로그아웃 사용시 활성화
        goProfile={goProfile}
        getMyProfile={getMyProfile}
      />
      {!getInfo && !getMyProfile ? <InfiniteSlider /> : null}
      {!getInfo && !getMyProfile ? <BaseCard info={info} /> : null}
      {!getInfo ? null : (
        <InfoBody
          pageID={pageID}
          user={user}
          teamMatchingClicked={teamMatchingClicked}
        />
      )}
      {getMyProfile ? <ProfileBody user={user} /> : null}
      <Footer />
    </>
  );
};

export default MainPage;
