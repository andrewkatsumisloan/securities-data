Work in progress. 

Application that compiles time series data for all of the S&P500 companies from the TDA API, uploads them to a AWS PostgreSQL database, and allows users to conduct basic analysis. 

Eventually will have a frontend interface that gets company data from RDS and renders time series data to user.



TO DO: 
1) Develop Frontend/API
2) Docker-ize application 
3) Automate updates to server (run one script that grabs new data from the TDA API, saves it locally, then updates it on the RDS instance), possibly find a more efficient way to do this (TDA API directly to RDS instance, remove intermediate step?)
4) Clean-up
5) Allow users to perform basic analysis and ML operations on company datasets.



