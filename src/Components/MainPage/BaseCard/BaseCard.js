import "./BaseCard.css";
import CompCard from "./CompCard";
import { useState, useEffect } from "react";
import OutComp from "./OutComp";
import Slider from "react-slick";
import axios from "axios";

const BaseCard = (props) => {
  const [teamMatchingClicked, setTeamMatchingClicked] = useState();
  const [data, setData] = useState([]);
  const [mgData, setmgData] = useState([]);
  useEffect(() => {
    async function getData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/acontest-list/"
        );
        setData(response.data);
      } catch (error) {
        throw new Error("Error fetching data:", error);
      }
    }
    getData();
    // console.log("받아온데이터" + JSON.stringify(data));
  }, []);
  useEffect(() => {
    async function getMGData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/dding-contest-list/"
        );
        setmgData(response.data);
      } catch (error) {
        throw new Error("Error fetching data:", error);
      }
    }
    getMGData();
    // console.log("받아온데이터" + JSON.stringify(data));
  }, []);
  const makePost = () => {
    const posts = [];
    if (!data) {
      return posts;
    }

    console.log("데이터임@@@@@@@@@" + JSON.stringify(data));
    data.forEach((item) => {
      let day = item.application_period;
      day = day.substring(day.indexOf("D"));

      let post = {
        day: day,
        title: item.title,
        auspice: item.organizer,
        imgSrc: item.photo,
        id: item.id,
      };
      // console.log(post);
      posts.push(post);
    });

    return posts;
  };
  const posts = makePost();
  const makeMGposts = () => {
    const Mgposts = [];
    if (!mgData) {
      return MGposts;
    }

    console.log("교내데이터임@@@@@@@@@" + JSON.stringify(mgData));
    mgData.forEach((item) => {
      let day = item.application_period;
      day = day.substring(day.indexOf("D"));

      let post = {
        day: day,
        title: item.title,
        auspice: item.organizer,
        imgSrc: item.photo,
        id: item.id,
      };
      // console.log(post);
      Mgposts.push(post);
    });

    return Mgposts;
  };
  const MGposts = makeMGposts();
  // {
  //   day: "D-40",
  //   title: "MJU 기업분석 경진대회",
  //   auspice: "용인지역대학일자리협회",
  //   imgSrc: "img/교내2.png",
  //   application_period: "",
  //   eligibility: "",
  //   field: "",
  //   organizer: "",
  //   sponsorship: "",
  //   prize_total: "",
  //   prize_first: "",
  //   website: "",
  //   details: "",
  // },
  // {
  //   day: "D-30",
  //   title: "창의적 SW프로그램 경진대회",
  //   auspice: "ict융합대학",
  //   imgSrc: "img/경진대회 표지.jpg",
  // },
  // {
  //   day: "D-36",
  //   title: "제2회 명지대학교 공식 YOUTUBE 영상공모전",
  //   auspice: "대외협력·홍보팀",
  //   imgSrc: "img/교내3.jpg",
  // },
  // {
  //   day: "D-Day",
  //   title: "나만의 學UP비법",
  //   auspice: "대학교육혁신원 교육개발센터",
  //   imgSrc: "img/교내4.png",
  // },
  // {
  //   day: "D-Day",
  //   title: "제9회 명지C.C 창의·융합 아이디어 공모전",
  //   auspice: "대학교육혁신원 교육개발센터",
  //   imgSrc: "img/교내5.png",
  // },
  // {
  //   day: "D-Day",
  //   title: "IDEA공모전",
  //   auspice: "대학교육혁신지원사업운영팀",
  //   imgSrc: "img/교내6.jpg",
  // },

  const setINfo = (id, teamMatchingClicked) => {
    props.info(id, teamMatchingClicked);
    setTeamMatchingClicked(teamMatchingClicked);
  };
  const settings = {
    className: "center centerMode",
    infinite: true,
    slidesToShow: 4,
    slidesPerRow: 1,
    speed: 500,
    prevArrow: (
      <div style={{ position: "relative" }}>
        <img
          style={{
            position: "absolute",
            top: "-315px",
            filter: `drop-shadow(0px 1px 3px rgba(0,0,0,0.25))`,
          }}
          src="img/chevron-button-left.svg"
          className="comp-slider-chevron"
        ></img>
      </div>
    ),
    nextArrow: (
      <div style={{ position: "relative" }}>
        <img
          style={{
            position: "absolute",
            top: "-315px",
            left: "-54px",
            filter: `drop-shadow(0px 1px 3px rgba(0,0,0,0.25))`,
          }}
          src="img/chevron-button-right.svg"
          className="comp-slider-chevron"
        ></img>
      </div>
    ),
  };
  console.log("teamMatchingClicked3" + teamMatchingClicked);
  return (
    <div className="BaseCard">
      <div className="comp-slider">
        <div className="comp-slider-bar">
          <div className="comp-slider-bar-text">
            <div className="comp-slider-bar-text-bold">
              팀원 모집 중인 공모전
            </div>
            <div className="comp-slider-bar-text-thin">을 소개합니다</div>
          </div>
        </div>
        <div className="comp-slider-main">
          {/* <CompCard props={CompCard1} /> */}
          {/* {CompCards.map((Card, index) => (
            <CompCard key={index} {...Card} />
          ))} */}
          <div style={{ width: "1079px" }}>
            <Slider {...settings}>
              {posts.map((post, index) => (
                <CompCard key={index} {...post} onClick={setINfo} />
              ))}
            </Slider>
          </div>
        </div>
      </div>
      <div className="comp-slider" style={{ marginTop: "80px" }}>
        <div className="comp-slider-bar">
          <div className="comp-slider-bar-text">
            <div className="comp-slider-bar-text-bold">교내 공모전</div>
            <div className="comp-slider-bar-text-thin">을 소개합니다</div>
          </div>
        </div>
        <div className="comp-slider-main">
          <div style={{ width: "1079px" }}>
            <Slider {...settings}>
              {MGposts.map((post, index) => (
                <CompCard key={index} {...post} onClick={setINfo} />
              ))}
            </Slider>
          </div>
        </div>
      </div>
      <OutComp data={data} onClick={setINfo} />
    </div>
  );
};

export default BaseCard;
