import React, { useState } from "react";
import { NavLink } from "react-router-dom";
// import ".../public/css/SideBar.css";
import '../css/SideBar.css';
 

const Sidebar = () => {
  const [selectedTab, setSelectedTab] = useState(0);

  const handleTabSelect = (index) => {
    setSelectedTab(index);
  };

  return (
    <div className="sidebar-container">
      <ul className="sidebar">
        <li
          className={`sidebar-item ${selectedTab === 0 ? "active" : ""}`}
          onClick={() => handleTabSelect(0)}
        >
          <NavLink to="/patient-form">Patient Form</NavLink>
        </li>
        <li
          className={`sidebar-item ${selectedTab === 1 ? "active" : ""}`}
          onClick={() => handleTabSelect(1)}
        >
          <NavLink to="/possible-diseases">Possible Diseases</NavLink>
        </li>
        <li
          className={`sidebar-item ${selectedTab === 2 ? "active" : ""}`}
          onClick={() => handleTabSelect(2)}
        >
          <NavLink to="/diagnosis-tree">Diagnosis Tree</NavLink>
        </li>
        <li
          className={`sidebar-item ${selectedTab === 2 ? "active" : ""}`}
          onClick={() => handleTabSelect(2)}
        >
          <NavLink to="/history-record">History Record</NavLink>
        </li>
        <li
          className={`sidebar-item ${selectedTab === 2 ? "active" : ""}`}
          onClick={() => handleTabSelect(2)}
        >
          <NavLink to="/edit-knowledge">修改诊断路径</NavLink>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
