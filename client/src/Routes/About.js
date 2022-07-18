import React from 'react'
import { Link } from 'react-router-dom';
import './About.css'

const About = () => {
    return (
        <div >
            <div className="return-home"> 
                <Link to="/"> Back to Home </Link>
            </div>
            <div className="About">
                <h1> Learn more about this project </h1>
                <p> This is a work in progress. </p>
                <p> Currently under development is a frontend interface for a Python application/tool that aggregates and analyzes financial data of S&P500 companies.</p>
            </div>
        </div>
    )
}

export default About
