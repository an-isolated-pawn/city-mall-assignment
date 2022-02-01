import React, { useState, useEffect } from 'react';
import './App.css';
import {AgGridColumn, AgGridReact} from 'ag-grid-react';
import axios from "axios";

import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';



function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8000/profile/')
    .then((res) => {
      if(res.data && res.data.results && res.data.results.length > 0 ) {
        const response = (res.data.results).map(profile => ({
          "id": profile.id,
          "name": profile.name,
          "email": profile.email,
          "gender": profile.gender,
          "country": profile.country,
          "city": profile.city,
          "dob": profile.date_of_birth,
        }))
        setData(response);
      }
    })
  }, []);

  return (
    <div className="ag-theme-alpine" style={{height: 800, width: 2000}}>
    <AgGridReact
        rowData={data}>
        <AgGridColumn field="id"></AgGridColumn>
        <AgGridColumn field="name"></AgGridColumn>
        <AgGridColumn field="email"></AgGridColumn>
        <AgGridColumn field="gender"></AgGridColumn>
        <AgGridColumn field="dob"></AgGridColumn>
        <AgGridColumn field="country"></AgGridColumn>
        <AgGridColumn field="city"></AgGridColumn>
    </AgGridReact>
  </div>
  );
}

export default App;
