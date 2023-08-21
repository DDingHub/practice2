import "./App.css";
import "./Modal.css";
import { Route, Routes } from "react-router";
import LogInPage from "./Components/LogInPage/LogInPage";
import MainPage from "./Components/MainPage/MainPage";
import SignInPage from "./Components/SignInPage/SignInPage";
import SignInPage2 from "./Components/SignInPage2/SignInPage2";
import { useState } from "react";
import ModalPortals from "./ModalPortals";
import Modal from "./Modal";
import TypeTest from "./Components/TypeTest/TypeTest";

function App() {
  const [modal, setModal] = useState(false);
  const [loginState, setLoginState] = useState(false);
  const [user, setUser] = useState();
  // const LoginHandler = ()={
  const handleModalShow = (status) => {
    setModal(status);
  };
  const MoveToTop = () => {
    // top:0 >> 맨위로  behavior:smooth >> 부드럽게 이동할수 있게 설정하는 속성
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
  const login = () => {
    setLoginState(true);
  };
  const getUserId = (id) => {
    setUser(id);
    console.log("로그인된 유저" + JSON.stringify(id));
  };

  // }
  return (
    <div className="App">
      <Routes>
        <Route
          path="/"
          element={
            <MainPage
              loginState={loginState}
              user={user}
              // setLoginState={setLoginState}
              //로그아웃 사용시 활성화
            />
          }
        />
        <Route
          path="/logInPage"
          element={<LogInPage login={login} getUserId={getUserId} />}
        />
        <Route path="/SignInPage" element={<SignInPage />} />

        <Route path="/TypeTest" element={<TypeTest />} />
      </Routes>
      <div
        style={{
          position: "fixed",
          bottom: "100px",
          right: "100px",
          alignSelf: "end",
          cursor: "pointer",
        }}
      >
        <img src="img/goTop.svg" onClick={MoveToTop}></img>
      </div>

      <ModalPortals>
        <Modal show={modal} handleModalShow={handleModalShow} />
      </ModalPortals>
    </div>
  );
}

export default App;
