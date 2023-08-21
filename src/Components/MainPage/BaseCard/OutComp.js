import OutCompCard from "./OutCompCard";
import "../UI/OutComp.css";
import { useState, useEffect } from "react";
import axios from "axios";

const OutComp = (props) => {
  const [data, setData] = useState([]);
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
  }, []);
  const makePost = () => {
    const posts = [];
    let posts2 = []; // 추가 배열
    if (!data) {
      return posts;
    }
    data.forEach((item, index) => {
      let day = item.application_period;
      day = day.substring(day.indexOf("D"));

      let post = {
        day: day,
        title: item.title,
        auspice: item.organizer,
        imgSrc: item.photo,
        id: item.id,
      };

      if (index < 12) {
        posts.push(post);
      } else {
        posts2.push(post); // index가 12 이상이면 추가 배열에 push
      }
    });
    posts2 = [...posts, ...posts2];
    // console.log("post배열임" + JSON.stringify(posts)); // 처음 12개의 데이터를 담은 배열
    // console.log("posts2배열전체임: " + JSON.stringify(posts2)); // 12개 이후의 데이터를 담은 배열

    return { posts, posts2 };
  };

  const { posts, posts2 } = makePost();
  const [showMore, setShowMore] = useState(false);

  const handleShowMore = () => {
    setShowMore(true);
  };
  const callSetINfo = (id, teamMatchingClicked) => {
    props.onClick(id, teamMatchingClicked);
    console.log("teamMatchingClicked2" + teamMatchingClicked);
  };
  return (
    <div className="OutComp">
      <div className="OutComp-bar">
        <div className="OutComp-bar-text-bold">교외 공모전</div>
        <div className="OutComp-bar-text-thin">을 소개합니다</div>
      </div>
      <div className="OutComp-container">
        {showMore
          ? posts2.map((post, index) => (
              <OutCompCard key={index} {...post} onClick={callSetINfo} />
            ))
          : posts.map((post, index) => (
              <OutCompCard key={index} {...post} onClick={callSetINfo} />
            ))}
      </div>
      {!showMore && (
        <div className="OutComp-more">
          <button
            className="wordButton OutComp-more-font"
            onClick={handleShowMore}
            style={{ cursor: "pointer" }}
          >
            더보기
          </button>
          <img
            src="img/Polygon-bottom.svg"
            className="wordButton OutComp-more-poly"
          />
        </div>
      )}
    </div>
  );
};

export default OutComp;
