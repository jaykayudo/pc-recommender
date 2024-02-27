import React, { useState } from "react";
import { data } from "../assets/data";
import dellxps from '../images/dell xps.jpg';
import inspirion from '../images/dell inspirion.jpg';
import spectre from '../images/spectre.jpg';

// Define an array of laptop details
const laptopDetails = [
  {
    image: dellxps,
    name: "Dell XPS 14",
    price: "$1000",
  },
  {
    image: inspirion,
    name: "Dell Inspirion",
    price: "$1200",
  },
  {
    image: spectre,
    name: "HP Spectre",
    price: "$1500",
  },
];

const Recommendation = ({ index, setIndex, totalQuestions }) => {
  const [question, setQuestion] = useState(data[index]);
  const [selectedOptions, setSelectedOptions] = useState(
    new Array(data.length).fill(null)
  );
  const [showImages, setShowImages] = useState(false);

  const next = () => {
    if (index < data.length - 1) {
      setIndex((prevIndex) => {
        setQuestion(data[prevIndex + 1]);
        return prevIndex + 1;
      });
    } else {
      // If on the last question, show images
      setShowImages(true);
    }
  };

  const previous = () => {
    if (index > 0) {
      setIndex((prevIndex) => {
        setQuestion(data[prevIndex - 1]);
        return prevIndex - 1;
      });
    }
  };

  const handleCheckboxChange = (optionIndex) => {
    const newSelectedOptions = [...selectedOptions];
    newSelectedOptions[index] = optionIndex;
    setSelectedOptions(newSelectedOptions);
  };

  return (
    <div className="container mx-auto sm:px-12 px-6">
      <h2 className="font-semibold text-xl md:text-center mb-4 md:text-5xl text-center sm:pb-6">
        {question.question}
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-8">
        {question.options.map((option, optionIndex) => (
          <label
            key={optionIndex}
            className={`flex items-center text-sm border p-4 md:p-8 cursor-pointer rounded-md mb-2 ${
              selectedOptions[index] === optionIndex
                ? "border-blue-600"
                : "border-gray-200"
            }`}
          >
            <input
              type="checkbox"
              className="mr-2 bg-blue-600"
              value={optionIndex}
              checked={selectedOptions[index] === optionIndex}
              onChange={() => handleCheckboxChange(optionIndex)}
            />
            <div className="flex-grow">
              <h3 className="font-semibold text-lg text-blue-600">
                {option.title}
              </h3>
              <p className="text-gray-600">{option.description}</p>
            </div>
          </label>
        ))}
      </div>
      <div className="flex justify-between items-center mt-4">
        {index > 0 && (
          <button
            onClick={previous}
            className="bg-gray-400 text-white px-4 py-2 rounded-md hover:bg-gray-500"
            disabled={index === 0}
          >
            Previous
          </button>
        )}
        <button
          onClick={next}
          className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
          disabled={!selectedOptions[index] && selectedOptions[index] !== 0}
        >
          {index === data.length - 1 ? "Get PC Recommendations" : "Next"}
        </button>
      </div>
      {showImages && (
        <div className="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {/* Render laptop details here */}
          {laptopDetails.map((laptop, laptopIndex) => (
            <div key={laptopIndex} className="flex flex-col items-center">
              <img
                src={laptop.image}
                alt={laptop.name}
                className="w-full md:w-48 lg:w-56 h-auto mb-2"
              />
              <p className="text-lg font-semibold mb-1">{laptop.name}</p>
              <p className="text-gray-600">{laptop.price}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Recommendation;
