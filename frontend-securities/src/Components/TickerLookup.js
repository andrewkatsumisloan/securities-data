import React from 'react'
import { Link } from "react-router-dom";
import { useState } from 'react';

import './TickerLookup.css'

const TickerLookup = () => {
    const [ticker, setTicker] = useState('');
    const [tickerData, setTickerData] = useState(null);

    const getHistoricalData = async () => {
        console.log('Get Historical Data')
    }

    const handleInputChange = (e) => {
        setTicker(e.target.value)
        console.log(ticker)
    }

    return (
        <div > 
                <div className='ticker-search'>
                    <h1> Enter Ticker Symbol </h1>
                        <input 
                            className="input-ticker" 
                            type="text" 
                            placeholder="Ex: AAPL"
                            onChange={handleInputChange} 
                            onInput={(e) => e.target.value = ("" + e.target.value).toUpperCase()} />
                        <input 
                            type="submit" 
                            value="Submit" 
                            onClick={() => getHistoricalData(ticker)} />
                </div>
        </div>
    )
}

export default TickerLookup
