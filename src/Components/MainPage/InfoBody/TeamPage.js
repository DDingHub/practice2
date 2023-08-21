import "./Teams.css";
import "./TeamCard.css";
import "./TeamPage.css";
import { BlueButton } from "../UI/Buttons";
import { GrayTag, GrayBox } from "../UI/TextBox";
import { FlexBox } from "../UI/FlexBox";

const TeamPage = () => {
  const handleApply = () => {};
  return (
    <div className="mT-container">
      <div className="mT-container-bar">
        <img src="img/greenface.svg"></img>
        <div className="mT-container-bar-text">
          <img src="img/crown.svg" className="mT-container-bar-img" />
          <div className="mT-container-bar-text-bold">닉네임</div>
          <div className="mT-container-bar-text-thin">디지털콘텐츠학과</div>
          <img src="img/edit.svg" className="tP-container-bar-edit"></img>
        </div>
      </div>
      <div className="mT-container-line"></div>

      <div className="tP-container-name">개발, 디자인 팀원 구해요</div>
      <div className="tP-container-teamname">Team. 띵Hub</div>
      <div className="tP-container-detail">
        저는 무슨무슨 공모전 팀장 닉네임입니다.
        팀소개글~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 111 2 33
      </div>

      <div className="mT-container-line"></div>
      <div className="tP-container-title">우리팀은 이런 성향이 모였음</div>
      <FlexBox dir="row">
        <GrayTag text="밤에 일하는 올빼미" />
        <GrayTag text="비대면 선호" />
        <GrayTag text="논리적인 팔로워" />
        <GrayTag text="목표지향적 커뮤니케이터" />
      </FlexBox>

      <div className="tP-container-title">여기로 연락주세요!</div>
      <GrayBox text="DDinghub@gmail.com" />
      <div className="tP-container-title">팀원(6명)</div>

      <div className="TeamCard-jobArea">
        <div className="TeamCard-jobArea-container">
          <div className="tP-jobArea-container-name">개발</div>
          <div className="tP-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              {/* <Capacity status="dev" /> */}
            </div>
          </div>
          <BlueButton
            width={153}
            height={40}
            onClick={handleApply}
            text="개발 지원하기"
          />
        </div>
        <div className="TeamCard-jobArea-container">
          <div className="tP-jobArea-container-name">기획</div>
          <div className="tP-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              {/* <Capacity status="plan" /> */}
            </div>
          </div>
          <BlueButton
            width={153}
            height={40}
            onClick={handleApply}
            text="기획 지원하기"
          />
        </div>

        <div className="TeamCard-jobArea-container">
          <div className="tP-jobArea-container-name">디자인</div>
          <div className="tP-jobArea-container-member">
            <div className="TeamCard-jobArea-container-member-icons">
              {/* <Capacity status="design" /> */}
            </div>
          </div>
          <BlueButton
            width={153}
            height={40}
            onClick={handleApply}
            text="디자인 지원하기"
          />
        </div>
      </div>
    </div>
  );
};
export default TeamPage;
