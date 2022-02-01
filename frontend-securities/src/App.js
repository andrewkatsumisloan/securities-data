import { Link } from 'react-router-dom';

import './App.css';
import LoginButton from './Components/LoginButton';
import LogoutButton from './Components/LogoutButton';
import Profile from './Components/Profile';
import TickerLookup from './Components/TickerLookup';

import './App.css'

function App() {
  return (
    <div className="App">
      <h1> Quantitativus </h1>
      <h2> Currently Under Construction </h2>
      <p> <i> A basic frontend for Python financial data analysis application </i>  </p>
      <TickerLookup />
      <div className='about-link'> 
        <Link to="/About"> Learn more about this project. </Link> </div>
      <div className='TickerLookup'> 
      </div>
    </div>
  );
}

export default App;