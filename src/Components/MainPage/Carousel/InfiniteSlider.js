import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "./Carousel.css";

const CenterMode = () => {
  const [centerPadding, setCenterPadding] = useState("300px");

  const settings = {
    className: "center centerMode",
    centerMode: true,
    infinite: true,
    centerPadding: centerPadding,
    slidesToShow: 1,
    slidesPerRow: 1,
    speed: 1000,
    autoplay: false,
    adaptiveHeight: false,
    autoplaySpeed: 3000,
    pauseOnHover: true,
  };

  // Update centerPadding when window size changes
  useEffect(() => {
    const updateCenterPadding = () => {
      const windowWidth = window.innerWidth;
      // Calculate centerPadding based on window width or any other criteria
      let newCenterPadding = "300px"; // Default value
      if (windowWidth <= 768) {
        newCenterPadding = "100px"; // Update for smaller screens
      }
      setCenterPadding(newCenterPadding);
    };

    // Initial centerPadding calculation
    updateCenterPadding();

    // Add event listener for window resize
    window.addEventListener("resize", updateCenterPadding);

    // Clean up event listener on unmount
    return () => {
      window.removeEventListener("resize", updateCenterPadding);
    };
  }, []);

  return (
    <div
      style={{
        position: "relative",
        height: "300px",
        width: "100vw",
        margin: "43px 0px 61px 0px",
        maxWidth: "100vw",
        minWidth: "100vw",
        minHeight: "300px",
      }}
    >
      <Slider {...settings}>
        <div>
          <img src="img/banner-award.svg" className="img" alt="Banner 1"></img>
        </div>
        <div>
          <img
            src="img/banner-contest.svg"
            className="img"
            alt="Banner 2"
          ></img>
        </div>
        <div>
          <img
            src="img/banner-typetest.svg"
            className="img"
            alt="Banner 3"
          ></img>
        </div>
      </Slider>
    </div>
  );
};

export default CenterMode;
