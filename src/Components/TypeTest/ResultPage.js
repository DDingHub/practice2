import axios from "axios";
import { useState, useEffect } from "react";
import "./ResultPage.css";
import { Link } from "react-router-dom";

const ResultPage = ({ type }) => {
  const [typeResult, setTypeResult] = useState();
  const [username, setUsername] = useState();
  window.scrollTo(0, 0);
  const handleRefresh = () => {
    window.location.reload();

    window.scrollTo(0, 0);
  };
  useEffect(() => {
    async function getData() {
      try {
        const request = await axios.get("url");
        setTypeResult(request.data);
      } catch {}
    }
    getData();
  }, []);

  return (
    <>
      <div className="ResultPage-title">{`${username}님의 테스트 결과는`}</div>
      <img className="ResultPage-img" />
      <div className="ResultPage-typeMessage">나를 따르라</div>
      <div className="ResultPage-type">컨트롤타워</div>

      <div className="ResultPage-explainContainer">
        <div className="ResultPage-explainContainer-hashtag">
          #자신감 #결단력 #지배력
        </div>
        <div className="ResultPage-explainContainer-explain">
          <div>
            프로젝트를 이끌며 팀원들의 열정까지 이끌어내는 사람 끈기를 가지고
            팀원들을 다독이며 원하는 목표를 달성해내요. 자신의 주장을 단호하게
            밀고 나갈 수 있는 결단력이 있고, 사람들을 설득해나가는 능력이
            있어요. 가끔 반대 의견에 대해서는 감정적인 면모를 보이는 편이에요.
          </div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
      <div className="ResultPage-relation">
        <div className="ResultPage-best">
          <div className="ResultPage-title">환상의 케미</div>
          <img className="ResultPage-img"></img>
          <div className="ResultPage-typeMessage">
            내가 집중하면 모두가 놀랄걸?
          </div>
          <div className="ResultPage-type">애널리스트</div>
        </div>
        <div className="ResultPage-worst">
          <div className="ResultPage-title">환장의 케미</div>
          <img className="ResultPage-img"></img>
          <div className="ResultPage-typeMessage">꼼꼼함이 나의 무기!</div>
          <div className="ResultPage-type">디테일리스트</div>
        </div>
      </div>
      <div className="ResultPage-buttonContainer">
        <div className="ResultPage-buttonContainer-re" onClick={handleRefresh}>
          <div className="ResultPage-buttonContainer-re-text">
            테스트 다시하기
          </div>
        </div>
        <div className="ResultPage-buttonContainer-save">
          <Link to={"/"} className="ResultPage-buttonContainer-save-text">
            대표 유형으로 설정하기
          </Link>
        </div>
      </div>
    </>
  );
};

export default ResultPage;
