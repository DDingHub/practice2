import "./SignInPage2.css";
import "../MainPage/UI/defaultItem.css";
import "../MainPage/UI/logo.css";
import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import DynamicButton from "./DynamicButton";
import axios from "axios";

const Head = ({ page }) => {
  if (page === 1) {
    return (
      <div className="p2-container-head dis-row">
        <div className="p2-container-head-num">
          <div className="p2-container-head-num-text">{page}</div>
        </div>
        <div>
          <div className="p2-container-head-title">전문분야 설정</div>
          <div className="p2-container-head-nextNum">
            <div className="p2-container-head-nextNum-text">{page + 1}</div>
          </div>
        </div>
      </div>
    );
  } else if (page === 2) {
    return (
      <div className="p2-container-head dis-row">
        <img src="img/check.svg" className="p2-container-head-num-check" />
        <div className="p2-container-head-num" style={{ marginLeft: "0px" }}>
          <div className="p2-container-head-num-text">{page}</div>
        </div>
        <div className="p2-container-head-title">관심태그 설정</div>
        <div className="p2-container-head-nextNum">
          <div className="p2-container-head-nextNum-text">{page + 1}</div>
        </div>
      </div>
    );
  } else if (page === 3) {
    return (
      <div className="p2-container-head dis-row">
        <img src="img/check.svg" className="p2-container-head-num-check" />
        <img
          src="img/check.svg"
          className="p2-container-head-num-check"
          style={{ marginLeft: "0px" }}
        />
        <div className="p2-container-head-num" style={{ marginLeft: "0px" }}>
          <div className="p2-container-head-num-text">{page}</div>
        </div>
        <div className="p2-container-head-title">성향태그 설정</div>
      </div>
    );
  }
};
const Body = ({ page, setNextPage }) => {
  if (page === 1) {
    return (
      <div className="p2-container-body ">
        <div className="p2-container-body-que">어떤 직군을 희망하시나요?</div>
        <div className="p2-container-body-que-title">직군</div>
        <div className="p2-container-body-ButtonContainer">
          <DynamicButton size="middle" text="기획" />
          <DynamicButton size="middle" text="개발" />
          <DynamicButton size="middle" text="디자인" />
        </div>
        <DynamicButton size="big" text="다음" onClick={setNextPage} />
      </div>
    );
  } else if (page === 2) {
    return (
      <div className="p2-container-body ">
        <div className="p2-container-body-que">어떤 직군을 희망하시나요?</div>
        <div className="p2-container-body-que-title">직군</div>
        <div className="p2-container-body-ButtonContainer">
          <DynamicButton size="middle" text="기획" />
          <DynamicButton size="middle" text="개발" />
          <DynamicButton size="middle" text="디자인" />
        </div>
        <DynamicButton size="big" text="다음" onClick={setNextPage} />
      </div>
    );
  } else if (page === 3) {
    return <div className="p2-container-bigBody"></div>;
  }
};

const SignInPage2 = () => {
  async function getData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/review/");

      console.log("success!", response.data[0].id);
    } catch (error) {
      console.log("some errors", error);
    }
  }
  const [page, setPage] = useState(1);
  const nv = useNavigate();
  getData();
  const setNextPage = () => {
    if (page === 3) {
      nv("/");
    }
    setPage(page + 1);

    console.log("page2");
  };

  return (
    <div className="p2-background">
      <div className="p2-container-logo">
        <img className="logo" src="img/logo.svg" alt="logo"></img>
        <Link to={"/"} className="wordLink ddingHub">
          띵Hub
        </Link>
      </div>
      <div className="p2-container">
        <Head page={page} />
        <Body page={page} setNextPage={setNextPage} />
      </div>
    </div>
  );
};
export default SignInPage2;
