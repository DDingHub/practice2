import { useEffect, useRef } from "react";
import "./Modal.css";

export default function Modal({ show, handleModalShow, contents }) {
  const modalContentRef = useRef(null);

  useEffect(() => {
    if (show) {
      document.body.style.overflow = "hidden";

      // 모달의 스크롤 위치를 맨 위로 설정
      if (modalContentRef.current) {
        modalContentRef.current.scrollTop = 0;
      }
    } else {
      document.body.style.overflow = "unset";
    }
  }, [show]);

  return (
    <div className={"modal-wrap " + (show ? "active" : "")}>
      <div
        className="overlay"
        onClick={() => {
          handleModalShow(false);
        }}
      ></div>
      <div
        className="modal-con"
        style={{ overflowY: "auto" }}
        ref={modalContentRef}
      >
        <img
          src="img/x.svg"
          className="x"
          onClick={() => {
            handleModalShow(false);
          }}
        ></img>
        <div className="contents">{contents}</div>
      </div>
    </div>
  );
}
