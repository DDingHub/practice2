import { useState } from "react";
// import Page1 from "./Page1";
import { Link, useNavigate } from "react-router-dom";
import "./SignInPage.css";
import axios from "axios";
import Select from "./Select";

const OPTIONS = [
  { value: "", name: "선택해주세요." },
  { value: "", name: "------인문대------" },
  { value: "국어국문학과", name: "국어국문학과" },
  { value: "중어중문학과", name: "중어중문학과" },
  { value: "일어일문학과", name: "일어일문학과" },
  { value: "영어영문학과", name: "영어영문학과" },
  { value: "사학과", name: "사학과" },
  { value: "문헌정보학과", name: "문헌정보학과" },
  { value: "아랍지역학과", name: "아랍지역학과" },
  { value: "미술사학과", name: "미술사학과" },
  { value: "철학과", name: "철학과" },
  { value: "문예창작학과", name: "문예창작학과" },
  { value: "글로벌한국어학과", name: "글로벌한국어학과" },
  { value: "글로벌아시아문화학과", name: "글로벌아시아문화학과" },
  { value: "", name: "------사회과학대학------" },
  { value: "행정학과", name: "행정학과" },
  { value: "경제학과", name: "경제학과" },
  { value: "정치외교학과", name: "정치외교학과" },
  { value: "디지털미디어학과", name: "디지털미디어학과" },
  { value: "아동학과", name: "아동학과" },
  { value: "청소년지도학과", name: "청소년지도학과" },
  { value: "", name: "------경영대학------" },
  { value: "경영학과", name: "경영학과" },
  { value: "국제통상학과", name: "국제통상학과" },
  { value: "경영정보학과", name: "경영정보학과" },
  { value: "부동산학과", name: "부동산학과" },
  { value: "", name: "------법과대학------" },
  { value: "법학과", name: "법학과" },
  { value: "법무정책학과", name: "법무정책학과" },
  { value: "", name: "------ICT융합대학------" },
  { value: "디지털콘텐츠디자인학과", name: "디지털콘텐츠디자인학과" },
  { value: "융합소프트웨어학부", name: "융합소프트웨어학부" },
  { value: "정보통신공학과", name: "정보통신공학과" },
  { value: "", name: "------자연과학대학------" },
  { value: "수학과", name: "수학과" },
  { value: "물리학과", name: "물리학과" },
  { value: "화학과", name: "화학과" },
  { value: "식품영양학과", name: "식품영양학과" },
  { value: "생명과학정보학과", name: "생명과학정보학과" },
  { value: "", name: "------공과대학------" },
  { value: "전기공학과", name: "전기공학과" },
  { value: "전자공학과", name: "전자공학과" },
  { value: "반도체공학과", name: "반도체공학과" },
  { value: "화학공학과", name: "화학공학과" },
  { value: "신소재공학과", name: "신소재공학과" },
  { value: "환경에너지공학과", name: "환경에너지공학과" },
  { value: "컴퓨터공학과", name: "컴퓨터공학과" },
  { value: "토목환경공학과", name: "토목환경공학과" },
  { value: "교통공학과", name: "교통공학과" },
  { value: "기계공학과", name: "기계공학과" },
  { value: "산업경영공학과", name: "산업경영공학과" },
];
// const OPTIONS = ["Option 1", "Option 2", "Option 3"];

const SelectBox = (props) => {
  return (
    <select
      name={props.name}
      value={props.value}
      onChange={props.onChange}
      className="container-form-inputID selectBox-placeHolder"
    >
      {props.options.map((option) => (
        <option
          className="selectBox-option"
          value={option.value}
          defaultValue={props.defaultValue === option.value}
        >
          {option.name}
        </option>
      ))}
    </select>
  );
};

//선택형으로 업글 시 활성화 할것
const Page1 = () => {
  const goMain = useNavigate();
  const [formData, setFormData] = useState({});
  const [isSignUp, setIsSignUp] = useState(false);
  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };
  const handleSubmit = (event) => {
    event.preventDefault();

    axios
      .post(
        `http://127.0.0.1:8000/signup/`,
        // name: "asdf",
        // teamname: "asdf",
        // call: "asdfasdf",
        // detail: "asdf",
        // plan_capacity: "3",
        // dev_capacity: "12",

        // design_capacity: "1",
        formData
      )
      .then((response) => {
        // 요청 성공 시 수행할 작업
        console.log(response.data);
        setIsSignUp(true); // 서버 응답 데이터 출력
      })
      .catch((error) => {
        // 요청 실패 시 수행할 작업
        console.error(error);
      });

    // 여기서 폼 데이터를 백엔드로 전송합니다 (Axios 또는 다른 네트워크 요청 라이브러리 사용).
    console.log("폼 데이터:", formData);

    // 제출 후에 필요하다면 폼을 초기화합니다.
  };
  const signUpHandler = () => {
    if (isSignUp) {
      goMain();
    }
  };
  return (
    <div className="background">
      <div className="container">
        <div className="container-head">
          <Link to={"/LogInPage"} className="container-head-cancel">
            취소
          </Link>
          <div className="container-head-text">회원가입</div>
        </div>

        <form className="container-form" onSubmit={handleSubmit}>
          <div className="container-form-input-text1">이메일</div>
          <input
            className="container-form-inputID"
            placeholder=" 학교 이메일을 입력해주세요."
            name="username"
            value={formData.username}
            onChange={handleChange}
          ></input>
          <div className="container-form-input-text2">비밀번호</div>
          <input
            className="container-form-inputPW"
            placeholder=" 비밀번호를 입력해주세요."
            name="password"
            value={formData.password}
            onChange={handleChange}
          ></input>
          <div className="container-form-input-text2">비밀번호 확인</div>
          <input
            className="container-form-inputID"
            placeholder=" 비밀번호를 다시 한번 입력해주세요."
            name="password-re"
            value={formData.passwordRe}
            onChange={handleChange}
          ></input>
          <div className="container-form-input-text2">이름</div>
          <input
            className="container-form-inputID"
            placeholder=" 이름을 입력해주세요."
            name="name"
            value={formData.name}
            onChange={handleChange}
          ></input>
          <div className="container-form-input-text2">닉네임</div>
          <input
            className="container-form-inputID"
            placeholder=" 닉네임을 입력해주세요."
            name="nickname"
            value={formData.nickname}
            onChange={handleChange}
          ></input>
          <div className="container-form-input-text2">학과</div>
          <SelectBox
            name="major"
            value={formData.major}
            onChange={handleChange}
            options={OPTIONS}
          ></SelectBox>
          {/* <Select options={OPTIONS} /> */}
          <button
            to={"/SignInPage2"}
            type="submit"
            className="container-form-logInButton"
          >
            <div
              className="container-form-logInButton-text"
              onClick={signUpHandler}
            >
              가입하기
            </div>
          </button>
        </form>
      </div>
    </div>
  );
};

const Page2 = () => {};
const SignInPage = () => {
  const [page, setPage] = useState(1);

  if (page == 2) return <Page2 />;
  else return <Page1 setPage={setPage} />;
};
export default SignInPage;
