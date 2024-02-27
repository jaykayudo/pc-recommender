// Header.js

import React from "react";

const Header = () => {
  return (
    <div className="bg-blue-500 p-4 flex justify-between items-center">
      <h1 className="text-white text-xl sm:text-2xl  font-bold cursor-pointer" onClick={() => window.location.reload()}>PC Recommender</h1>
      <nav className="text-sm sm:text-xl">
        <ul className="flex space-x-4 text-white">
          <li>
            <a href="#" className="text-white">
              Home
            </a>
          </li>
          <li>
            <a href="#" className="text-white">
              Sign In
            </a>
          </li>
         
         
        </ul>
      </nav>
    </div>
  );
};

export default Header;
