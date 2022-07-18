import { Link } from 'react-router-dom';
import './App.css';
import TickerLookup from './Components/TickerLookup';
import HeatMap from './Components/HeatMap';

function App() {
  return (
    <div className="App">
      <h1> <i> S&P500 Securities Data Application </i></h1>
      <h2> Currently Under Construction </h2>
      <p> <i> A basic frontend for Python financial data analysis application </i>  </p>
      <TickerLookup />
      <HeatMap > </HeatMap>
      <div className='about-link'> 
        <Link to="/About"> Learn more about this project. </Link> 
      </div>
      <div className='TickerLookup'> 
      </div>
    </div>
  );
}

export default App;
