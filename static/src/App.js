import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

import "./App.css";

function App() {
  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
  axios.defaults.xsrfCookieName = "csrftoken";

  const [bankData] = useState([]);
  const [limit] = useState(1);

  console.log(limit);

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
      <h1>Bank Detail</h1>
      <div className="app_top">
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
