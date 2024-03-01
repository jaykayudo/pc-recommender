import React, { useState } from "react";
import Header from "./components/Header";
import Progress from "./components/Progress";
import Recommendation from "./components/Recommendation";
import './App.css';

import { data } from "./assets/data";

function App() {
  const [index, setIndex] = useState(0);
  const totalQuestions = data.length;

  return (
    <>
      <div>
        <Header />
      </div>
      <div className={"page-container"}>
        <div className="mt-2 flex flex-row items-center justify-center w-full">
          <h3 className="font-bold lg:ml-[80px]">Progress:</h3>
          <div className="w-[100%] md:w-[70%] ml-2">
            <Progress
              totalQuestions={totalQuestions}
              currentQuestion={index + 1}
            />
          </div>
        </div>
        <div>
          <Recommendation
            index={index}
            setIndex={setIndex}
            totalQuestions={totalQuestions}
          />
          <div className="flex justify-between mt-4"></div>
        </div>
      </div>
    </>
  );
}

export default App;
