import TextButton from "./TextButton";
import React from "react";
import "./TypeTestCard.css";
import { useState } from "react";

const TypeTestCard = ({ onTestEnd }) => {
  //테스트의 내용저장 파일분리?pagenum로 내용 찾기

  const [testEnd, setTestEnd] = useState(false);
  const [type, setType] = useState();
  const [pageNum, setPageNum] = useState(0);
  const [C, setC] = useState();
  const [S, setS] = useState();
  const [W, setW] = useState();
  const [H, setH] = useState();
  const [R, setR] = useState();
  const [P, setP] = useState();
  const [statArray, setStatArray] = useState([]);
  let text1, text2, text3, text4, Q1, Q2, Q3, buttonStat1, buttonStat2;

  //둘 중에서 강한 특성 찾기
  const chooseStrong = () => {
    let firstIndicator, secondIndicator, ThirdIndicator;

    if (C > S) {
      firstIndicator = "C";
    } else {
      firstIndicator = "S";
    }
    if (W > H) {
      secondIndicator = "W";
    } else {
      secondIndicator = "H";
    }
    if (R > P) {
      ThirdIndicator = "R";
    } else {
      ThirdIndicator = "P";
    }

    console.log(firstIndicator + secondIndicator + ThirdIndicator);
    return firstIndicator + secondIndicator + ThirdIndicator;
  };
  //스탯배열에서 마지막스탯 삭제
  const popLastElement = () => {
    let recentStat = statArray[statArray.length - 1];
    setStatArray((prevData) => prevData.slice(0, -1));
    console.log("삭제한 스탯" + recentStat);
    return recentStat;
  };

  const removeStat = (statToRemove) => {
    if (statToRemove === "C") {
      setC(C - 1);
    } else if (statToRemove === "S") {
      setS(S - 1);
    } else if (statToRemove === "W") {
      setW(W - 1);
    } else if (statToRemove === "H") {
      setH(H - 1);
    } else if (statToRemove === "R") {
      setR(R - 1);
    } else if (statToRemove === "P") {
      setP(P - 1);
    }
  };

  //이전으로 버튼 눌렸을 때 실행
  const setPrev = () => {
    removeStat(popLastElement());

    //스탯배열에서 스탯삭
  };

  //pageNum값에 따라 값 업데이트
  if (pageNum === 0) {
  } else if (pageNum === 1) {
    text1 = "전체를 훑어보면서";
    text2 = "필요한 내용만 집중해서 본다.";
    buttonStat1 = "C";
    text3 = "시간이 걸리더라도 순서대로";
    text4 = "하나하나 꼼꼼히 살펴본다.";
    buttonStat2 = "S";
    Q1 = "팀플의 첫 단계! 리서치 도중";
    Q2 = "공모전 관련 자료를 읽을 때 나는";
  } else if (pageNum === 2) {
    text1 = "나의 전문성만으로도";
    text2 = "성과를 낼 수 있는 일";
    buttonStat1 = "W";
    text3 = "팀원들과 협업하며";
    text4 = "시너지를 내는 일";
    buttonStat2 = "H";
    Q1 = "내가 더 선호하는 일은?";
  } else if (pageNum === 3) {
    text1 = "연봉과 명예";
    text2 = "";
    buttonStat1 = "R";
    text3 = "도전과 성장";
    text4 = "";
    buttonStat2 = "P";
    Q1 = "나에게 더 중요한 것은?";
  } else if (pageNum === 4) {
    text1 = "결과는 만족스럽지만";
    text2 = "팀원들과 충돌이 잦았던 팀플";
    buttonStat1 = "P";
    text3 = "팀원들과 사이와 분위기가 좋지만";
    text4 = "결과가 아쉬운 팀플";
    buttonStat2 = "R";
    Q1 = "내가 더 참을 수 없는 팀플은?";
  } else if (pageNum === 5) {
    text1 = "래퍼런스? 없으면 오히려 좋아~";
    text2 = "필요한 내용만 집중해서 본다.";
    buttonStat1 = "C";
    text3 = "시간이 걸리더라도 순서대로";
    text4 = "하나하나 꼼꼼히 살펴본다.";
    buttonStat2 = "S";
    Q1 = "프로젝트 주제를 정하고";
    Q2 = "관련 래퍼런스를 찾는데";
    Q3 = "별로 없는 것 같다.";
  } else if (pageNum === 6) {
    text1 = "팀원의 감정을 살피는 것이 우선!";
    text2 = "사소한 의견이라면 넘어간다.";
    buttonStat1 = "H";
    text3 = "내 생각과 다른 부분은";
    text4 = "명확히 짚고 넘어간다.";
    buttonStat2 = "W";
    Q1 = "팀원이 의견을 냈는데";
    Q2 = "생각이 다를 때 나는?";
    Q3 = "";
  } else if (pageNum === 7) {
    text1 = "당황했을 동료를 달래주고";
    text2 = "함께 해결할 방법을 찾아본다.";
    buttonStat1 = "H";
    text3 = "언제까지 필요한 파일인지 물어보며,";
    text4 = "복구 방법을 검색한다.";
    buttonStat2 = "W";
    Q1 = "팀원의 실수로 중요한 파일이 날아갔다.";
    Q2 = "나의 반응은?";
    Q3 = "";
  } else if (pageNum === 8) {
    text1 = "내일 회의 때 얘기하자고 한다.";
    text2 = "";
    buttonStat1 = "S";
    text3 = "바로 회의에 임한다.";
    text4 = "";
    buttonStat2 = "C";
    Q1 = "팀플 회의 전날 밤,";
    Q2 = "팀원이 상의할 내용이 있다며";
    Q3 = "갑자기 회의를 하자고 한다. 나는";
  } else if (pageNum === 9) {
    text1 = "내가 낸 결과물에 대한";
    text2 = "구체적인 칭찬";
    buttonStat1 = "R";
    text3 = "협업하기 좋은 팀원이라는 칭찬";
    text4 = "";
    buttonStat2 = "P";
    Q1 = "팀원에게 더 듣고 싶은 칭찬은?";
    Q2 = "";
    Q3 = "";
  } else if (pageNum === 10) {
    let result = chooseStrong();
    setType(result);
    setPageNum(11);
    setTestEnd(true);
  }

  //페이지 넘기기
  const pageSet = () => {
    setPageNum(pageNum + 1);

    // setTypeForm((prevData) => ({ ...prevData, stat }));
    // console.log("타입폼임" + typeForm);
  };
  //   const setTypeForm = (stat) => {
  //     typeForm.push(stat);

  //     console.log("타입폼저장호출" + typeForm);
  //   };

  //눌린 스탯 저장,statArray에도 순서대로 저장
  const handleStat = (stat) => {
    setStatArray((prevStatArray) => [...prevStatArray, stat]);
    console.log("받아온 스탯임" + stat);
    if (stat === "C") {
      if (C === undefined) {
        setC(1);
      } else {
        setC(C + 1);
      }
    } else if (stat === "S") {
      if (S === undefined) {
        setS(1);
      } else {
        setS(S + 1);
      }
    } else if (stat === "W") {
      if (W === undefined) {
        setW(1);
      } else {
        setW(W + 1);
      }
    } else if (stat === "H") {
      if (H === undefined) {
        setH(1);
      } else {
        setH(H + 1);
      }
    } else if (stat === "R") {
      if (R === undefined) {
        setR(1);
      } else {
        setR(R + 1);
      }
    } else if (stat === "P") {
      if (P === undefined) {
        setP(1);
      } else {
        setP(P + 1);
      }
    }
  };
  //테스트 종료시 testEnd true로 설정, 테스트 결과값 type으로 끌올
  if (testEnd) {
    onTestEnd(testEnd, type);
  }
  //이전 버튼 눌렸을 때
  const prevButtonClicked = () => {
    setPageNum(pageNum - 1);
    console.log("이전으로 되돌려진 페이지" + pageNum);
    setPrev();
    console.log("프리브 이후 스탯어레이" + statArray);
  };

  console.log("리턴 직전 상태" + C, S, W, H, R, P);

  //pageNum에 따라 다른 리턴값
  if (pageNum === 0) {
    return (
      <div className="TypeTestCard">
        <img src="img/typeTestImg.png" className="typeTestImg" />
        <div className="startCard-text-bold">팀플에서 나의 포지션은?</div>
        <div className="startCard-text-thin">띵Hub의 팀플 성향 테스트로</div>
        <div className="startCard-text-thin">
          나도 몰랐던 나의 팀플 성향을 확인하세요!
        </div>
        <div className="TestStartButton" onClick={() => setPageNum(1)}>
          <div className="TestStartButton-text">테스트 시작하기</div>
        </div>
      </div>
    );
  } else if (pageNum < 11 && !testEnd) {
    return (
      <div className="TypeTestCard">
        <div className="TypeTestCard-pageNum">{pageNum}/9</div>
        <img src={`img/progress${pageNum}.svg`}></img>
        <img
          className="TypeTestCard-prevPageButton"
          src="img/chevron-button-left.svg"
          onClick={prevButtonClicked}
        ></img>
        <img src="img/thinking.png" className="thingkingImg" />
        <div className="TypeTestCard-question">
          <div>{Q1}</div>
          <div>{Q2}</div>
          <div>{Q3}</div>
        </div>
        <TextButton
          statChange={handleStat}
          onClick={pageSet}
          text1={text1}
          text2={text2}
          buttonStat={buttonStat1}
        />
        <TextButton
          statChange={handleStat}
          onClick={pageSet}
          text1={text3}
          text2={text4}
          buttonStat={buttonStat2}
        />
      </div>
    );
  }
};

export default TypeTestCard;
