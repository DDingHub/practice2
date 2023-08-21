import React, { useState } from "react";
import "./Select.css"; // 스타일링 파일을 import

const Select = ({ options }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState("");

  const toggleOptions = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    setSelectedOption(option);
    setIsOpen(false);
  };

  return (
    <div className={`custom-select ${isOpen ? "open" : ""}`}>
      <div className="selected-option" onClick={toggleOptions}>
        {selectedOption || "Choose an option"}
      </div>
      <ul className="options">
        {options.map((option) => (
          <li key={option} onClick={() => handleOptionClick(option)}>
            {option}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Select;
