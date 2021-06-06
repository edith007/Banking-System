import React, { useState, useEffect } from "react";
import axios from "axios";
import DropdownButton from "react-bootstrap/DropdownButton";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";

import "./App.css";

function App() {
  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
  axios.defaults.xsrfCookieName = "csrftoken";

  const [value, setValue] = useState("Select Branch");
  const [bankData, setBankData] = useState([]);
  const [limit] = useState(1);

  console.log(limit);

  const handleSelect = (e) => {
  console.log(e);
  setValue(e);
};

const getBankData = async () => {
const res = await axios.get(
  `http://127.0.0.1:8000/api/branches/?q=${value}&limit=${limit}`
);

if (res.data.branches.length === 0) {
  setBankData([]);
} else {
  setBankData(res.data.branches);
}
};
useEffect(() => {
    getBankData();
  }, [value, limit]);


  const renderHeader = () => {
    let headerElement = [
      "ifsc",
      "bank id",
      "address",
      "city",
      "branch",
      "state",
      "bank name",
    ];

    return headerElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  const renderBody = () => {
    return bankData
      .reverse()
      .map(
        ({
          ifsc,
          bank_id,
          branch,
          address,
          city,
          district,
          state,
          bank_name,
        }) => {
          return (
            <tr key={bankData.id}>
              <td>{ifsc}</td>
              <td>{bank_id}</td>
              <td>{address}</td>
              <td>{city}</td>
              <td>{branch}</td>
              <td>{state}</td>
              <td>{bank_name}</td>
            </tr>
          );
        }
      );
  };

  return (
    <div className="App">
      <h1>Bank Branches</h1>
        <div>
          <DropdownButton
            alignRight
            title={value}
            id="dropdown-menu"
            onSelect={handleSelect}
          >
            <Dropdown.Item eventKey="Bangalore">Lucknow</Dropdown.Item>
            <Dropdown.Item eventKey="Mumbai">Bangalore</Dropdown.Item>
            <Dropdown.Item eventKey="Delhi">Delhi</Dropdown.Item>
            <Dropdown.Item eventKey="Nagpur">RTGS</Dropdown.Item>
            <Dropdown.Item eventKey="Bhopal">Bhopal</Dropdown.Item>
          </DropdownButton>
        </div>
      <div className="tracking-table">
        <table id="employee">
          <thead>
            <tr>{renderHeader()}</tr>
          </thead>
          <tbody>{renderBody()}</tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
