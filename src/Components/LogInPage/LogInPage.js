import { Link, useNavigate } from "react-router-dom";
import "./LogInPage.css";
import axios from "axios";
import { useState } from "react";
import { Navigate } from "react-router-dom";

const LogInPage = (props) => {
  const navigator = useNavigate();
  const [formData, setFormData] = useState({});
  const [loginError, setLoginError] = useState();
  const [isFormValid, setIsFormValid] = useState(false);
  //   const ifInput = (e) => {
  //     e.target;
  //   };

  const login = () => {
    props.login();
    if (isFormValid) {
      navigator("/");
    }
  };
  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((prevData) => ({ ...prevData, [name]: value }));
    const isEmailValid = /^[A-Za-z0-9._%+-]+@mju\.ac\.kr$/i.test(
      formData.username
    );
    setIsFormValid(isEmailValid);
  };
  const handleSubmit = (event) => {
    event.preventDefault();

    axios
      .post(`http://127.0.0.1:8000/login/`, formData)
      .then((response) => {
        props.getUserId(response.data.user.id);
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
        setLoginError(true);
      });
    console.log("폼 데이터:", formData);
  };

  return (
    <div className="LP-background">
      <div className="LP-container">
        <Link to={"/"} className="LP-container-logo">
          띵Hub
        </Link>
        <div className="LP-container-text-bold">
          명지대학교 이메일로 더욱 편리하게
        </div>
        <div className="LP-container-text-thin1">
          띵허브가 제공하는 서비스를
        </div>
        <div className="LP-container-text-thin2">
          학교 이메일로 간편하게 이용할 수 있습니다.
        </div>
        <form className="LP-container-form" onSubmit={handleSubmit}>
          <div className="LP-container-form-input-text1">이메일</div>
          <input
            className="LP-container-form-inputID"
            placeholder=" 학교 이메일을 입력해주세요."
            name="username"
            value={formData.username}
            onChange={handleChange}
          ></input>
          <div className="LP-container-form-input-text2">비밀번호</div>
          <input
            className="LP-container-form-inputPW"
            placeholder=" 비밀번호를 입력해주세요."
            name="password"
            value={formData.password}
            onChange={handleChange}
          ></input>
          <div
            className={`LP-container-form-error ${
              !loginError
                ? "LP-container-form-error-unact"
                : "LP-container-form-error-act"
            }`}
          >
            {`아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.`}
          </div>
          <button
            // to={"/"}
            type="submit"
            className={`LP-container-form-logInButton ${
              !isFormValid
                ? "LP-container-form-logInButton-unActive "
                : "LP-container-form-logInButton-active"
            }`}
            onClick={login}
          >
            <div
              className={`LP-container-form-logInButton-text ${
                !isFormValid
                  ? "LP-container-form-logInButton-text-unActive"
                  : "LP-container-form-logInButton-text-active"
              }`}
            >
              로그인
            </div>
          </button>
        </form>
        <div className="LP-container-footer">
          <div className="LP-container-footer-text1">
            아직 회원이 아니신가요?
          </div>
          <Link to={"/SignInPage"} className="LP-container-footer-text2">
            회원가입
          </Link>
        </div>
      </div>
    </div>
  );
};
export default LogInPage;
