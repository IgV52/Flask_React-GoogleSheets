import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from "axios";
import TableData from './components/TableData'
import OnLoadingTableData from './components/LoadingTableData'

function App() {

  const DataLoading =  OnLoadingTableData(TableData);

  const [appState, setAppState] = useState(
    {
      loading: false,
      rows: null,
    }
  )

 useEffect(() => {
    setAppState({loading: true})
    const apiUrl = 'http://localhost:5000/api/gs';

    axios.get(apiUrl).then((resp) => {
      const allRows = resp.data;
      setAppState({
      loading: false,
      rows: allRows
       });
    });
  }, [setAppState]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        <DataLoading isLoading={appState.loading} rows={appState.rows} />
        </p>
      </header>
    </div>
  );
}

export default App;
