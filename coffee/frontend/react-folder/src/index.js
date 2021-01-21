import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
// import NavigationBar from "./components/Navbar";
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
      {/*<NavigationBar/>*/}
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a functio
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();