import React from 'react';
import './TickerGraph.css';

import {
    AnimatedAxis,
    AnimatedGrid,
    AnimatedLineSeries,
    XYChart,
    Tooltip
} from "@visx/xychart";

const accessors = {
    xAccessor: (d) => d.date,
    yAccessor: (d) => d.value
  };

const TickerGraph = (props) => {
    console.log(props.tickerData)
  return (
    <div className="ticker-data" >
        {props.tickerSymbol ? 
            <h1> Historical Price Chart for {props.tickerSymbol} </h1> : <h1> Graph </h1>}
                <XYChart height={300} xScale={{ type: "band" }} yScale={{ type: "linear" }}>
                    <AnimatedAxis orientation="bottom" />
                    <AnimatedAxis orientation="left" />
                    <AnimatedGrid columns={false} numTicks={12} />
                    <AnimatedLineSeries dataKey="Line 1" data={props.tickerData} {...accessors} />
                    <Tooltip
                        snapTooltipToDatumX
                        snapTooltipToDatumY
                        showVerticalCrosshair
                        showSeriesGlyphs
                        renderTooltip={({ tooltipData, colorScale }) => (
                        <div>
                            <div 
                                style={{ color: colorScale(tooltipData.nearestDatum.key) }}>
                                {tooltipData.nearestDatum.key}
                            </div>
                            {accessors.xAccessor(tooltipData.nearestDatum.datum)}
                            {", "}
                            {accessors.yAccessor(tooltipData.nearestDatum.datum)}
                        </div>
                     )}
                    />
                </XYChart>
    </div>
  );
};

export default TickerGraph;
