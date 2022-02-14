import React, { useState, useEffect } from 'react'

import './HeatMap.css'

const HeatMap = () => {
    const [heatMapInput, setHeatMapInput] = useState([]);
    const [heatMapData, setHeatMapData] = useState()

    const handleInputChange = (e) => {
        const { id, value } = e.target;
        setHeatMapInput(prevState => ({
            ...prevState,
            [id]: value
        }))
        console.log(heatMapInput)
    }

    async function getHeatMapData(heatMapInput) {
        const response = await fetch("http://localhost:5000/get_heatmap", {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(heatMapInput)
        })
            .then(response => response.json())
                .then(result => {
                    setHeatMapData(result)
                })
    }
    
    return (
        <div className='heatmap-box'>
            <h2> Find Correlations — Heat Map </h2>
            <p> Enter the ticker symbol of three different SP500 companies, view their correlations.</p>
            <form> 
                <input id='1' className='input-field' onChange={handleInputChange} 
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()} />
                <input id='2' className='input-field' onChange={handleInputChange}
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
                <input id='3' className='input-field' onChange={handleInputChange}
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
            </form>
            <button onClick={() => getHeatMapData(heatMapInput)}> Generate Heat Map </button>
            <div> {console.log('This is heatMapData: ', heatMapData)} </div>
            {heatMapData ? <div> 
                <div> {heatMapData[0].map(
                    (item, index) => {
                        return <div key={index}> {item} </div>
                    }
                )} </div> 
                <div> {heatMapData[1].map(
                    (item, index) => {
                        return <div key={index}> {item} </div>
                    }
                )} </div>
                <div> {heatMapData[2].map(
                    (item, index) => {
                        return <div key={index}> {item} </div>
                    }
                )} </div>
            </div> : null}
            
        </div>
    )
}

export default HeatMap