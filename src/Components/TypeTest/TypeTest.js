import TypeTestCard from "./TypeTestCard";
import "./TypeTest.css";
import { useState, useEffect } from "react";
import ResultPage from "./ResultPage";
import NVbar from "../MainPage/NVbar/NVbar";
import axios from "axios";
import { Link } from "react-router-dom";

export default function TypeTest() {
  const [type, setType] = useState();
  const [testResult, setTestResult] = useState();
  const [testEnd, setTestEnd] = useState(false);
  //테스트의 결과 합쳐서 post
  //   const pageSetting = (num) => {
  //     setPageNum(num);
  //   };

  const TestEndHandler = (data, type) => {
    setTestEnd(data);
    setType(type);
  };

  //type post하고 테스트 결과 보여주는 데이터 받아와서 testresult로 저장

  //타입을 유저1대1대응 시키는 post 구현 clicked로 useeffect사용
  return (
    <>
      {!testEnd ? (
        <div className="TypeTest">
          <div className="TypeTest-bar">
            <div className="TypeTest-bar-container">
              <Link to={"/"}>
                <img src="img/logo.svg" />
              </Link>

              <div className="TypeTest-bar-text">팀플 성향 테스트</div>
            </div>
          </div>
          <div className="TypeTest-background">
            <TypeTestCard onTestEnd={TestEndHandler} />
          </div>
        </div>
      ) : (
        <>
          <NVbar />
          <ResultPage />
        </>
      )}
    </>
  );
}
