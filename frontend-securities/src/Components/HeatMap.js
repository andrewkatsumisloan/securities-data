import React, { useState, useEffect } from 'react'
import { Group } from '@visx/group';

import { scaleLinear } from '@visx/scale';
import { HeatmapCircle, HeatmapRect } from '@visx/heatmap';

import './HeatMap.css'

const HeatMap = () => {
    const [heatMapInput, setHeatMapInput] = useState([]);
    const [heatMapData, setHeatMapData] = useState([1])

    const handleInputChange = (e) => {
        const { id, value } = e.target;
        setHeatMapInput(prevState => ({
            ...prevState,
            [id]: value
        }))
        console.log(heatMapInput)
    }

    useEffect(() => {
        if (heatMapData !== [1]) {
            drawAll(heatMapData)
        }
    }, [heatMapData])

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

    function drawAll(heatmapArray) {
        var cnvs = document.getElementById("myCanvas");
        var cnv_width = cnvs.width;
        var cnv_height = cnvs.height;
        var ctx = cnvs.getContext("2d");
        ctx.font = '16px Arial';
    
        var low_r = 0;
        var low_g = 0;
        var low_b = 0;
    
        var high_r = 255;
        var high_g = 0;
        var high_b = 0;
    
        var topMargin = 32;
        var leftMargin = 64;
    
        var blockSizeH = (cnv_width - topMargin) / heatmapArray[0].length
        var blockSizeV = (cnv_height - leftMargin) / heatmapArray[0].length
    
        ctx.fillStyle = '#fff0d3';
        ctx.fillRect(0, 0, cnv_width, cnv_height);
    
        ctx.fillStyle = 'black';
        for(var col = 0; col < heatmapArray[0].length; col++) {
            ctx.fillText(heatmapArray[0][col], leftMargin + col * blockSizeH + blockSizeH/2, 16)
        }
    
        for(var row = 1; row < heatmapArray.length; row++){
            ctx.fillStyle = 'black';
            ctx.fillText(heatmapArray[0][row-1], 0, topMargin + (row - 1) * blockSizeV + blockSizeV/2)
            for(col = 0; col < heatmapArray[row].length; col++){
                var scale = heatmapArray[row][col];
                // console.log(Math.floor(low_r * (1-scale) + high_r * scale))
                ctx.fillStyle = `rgb(
                                    ${Math.floor(low_r * (1-scale) + high_r * scale)}, 
                                    ${Math.floor(low_g * (1-scale) + high_g * scale)}, 
                                    ${Math.floor(low_b * (1-scale) + high_b * scale)}
                                )`
                ctx.fillRect(leftMargin + col * blockSizeH, topMargin + (row - 1) * blockSizeV, blockSizeH, blockSizeV)
                ctx.fillStyle = 'white';
                ctx.fillText(heatmapArray[row][col].toFixed(3), leftMargin + col * blockSizeH + blockSizeH/2, topMargin + (row - 1) * blockSizeV + blockSizeV/2)
            }
        }
    }
    
    return (
        <div className='heatmap-box'>
            <h2> Find Correlations — Heat Map </h2>
            <p> Enter the ticker symbol of three different SP500 companies, view their correlations.</p>
            <form> 
                <input id='1' className='input-field' onChange={handleInputChange} 
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
                <input id='2' className='input-field' onChange={handleInputChange} 
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
                <input id='3' className='input-field' onChange={handleInputChange}
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
                <input id='4' className='input-field' onChange={handleInputChange}
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
                <input id='5' className='input-field' onChange={handleInputChange}
                onInput={(e) => e.target.value = (e.target.value).toUpperCase()}/>
            </form>
            <button onClick={() => getHeatMapData(heatMapInput)}> Generate Heat Map </button>
            {/* <div> {console.log('This is heatMapData: ', heatMapData)} </div> */}
            <div className='heatmap-canvas'> 
                {<canvas id="myCanvas" width="1024" height="512"> </canvas>} 
            </div>  
            
            {/* {heatMapData ? <div> 
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
            </div> : null} */}
            
        </div>
    )
}

export default HeatMap