import React from "react";

const Progress = ({ totalQuestions, currentQuestion }) => {
  const progressWidth = ((currentQuestion - 1) / totalQuestions) * 100 + "%";

  return (
    <div>
      <div className="h-[2px] w-full bg-gray-200 rounded-md p-0">
        <div
          className="h-full bg-blue-500"
          style={{ width: progressWidth }}
        ></div>
      </div>
    </div>
  );
};

export default Progress;
