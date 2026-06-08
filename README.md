# Using job posting characteristics to identify ghost jobs on digital labor platforms
The Congressional Research Service (CRS) defines ghost jobs as online postings by legitimate firms without any intention to hire in the foreseeable future. Such practices directly harm job-seekers, resulting in not just lost time and energy, but potential psychological distress. Previous studies estimate that 20% of job postings on digital labor platforms are ghost jobs, creating distortions that impact the accuracy of economic measures. This project investigates the the connection between job posting characteristics and suspected ghost job posting prevalence on digital labor platforms, using listing age as a proxy for ghost job probability

### Features
- Real-time web-scraping based of user-defined occupations and platforms (i.e. Linkedin, Glassdoor, Indeed) in New York and Boston metropolitan statisitcal areas (MSAs) into CSV files 
- Sample data exploration files using Matplotlib to show dataset distribution across markets, sectors, platforms
- Variable selection methods (i.e. Ridge and LASSO) to find the strongest determinants of  listing age

### Technologies Used
- JobSpy (open-source library that webscrapes job posting data from digital labor platforms)
- Python 3.12
- Pandas (data cleaning and transformation)
- Matplotlib (data visualization)
- Playwright (used to determine if a job listing is still active autonomously)

### Limitations
- Existing pipeline is set according to pre-defined BLS sectors and occupations that I used for this project, so it will require manual changes to the classification in the webscrape_script.py in their respective data structures
- Raw data cannot be made accessible through the repository due to sheer volume (100,000+ raw observations) and due to webscraping operting within a legal grey area, a synthetic dataset is provided instead
- Due to time and budget constraints, the calculation of listing age was done by the day a listing was checked subtracted by the day it was posted. For more accurate listing age variables, rotating proxies will need to be utilized to bypass anti-bot measures, allowing Playwright to determine listing age accurately and efficiently.

### Known Issues


## Setup and Installation 

### How to Run
1. Clone the repository:
```
git clone https://github.com/maggiechua/Ghost-Jobs-Research.git
```
2. Install [JobSpy]([url](https://github.com/speedyapply/JobSpy)) using the setup instructions listed on the repository

3. Create a folder called rawdata in your environment, so that when the webscrape_script.py is run, it will populate the folder with the collected job posting data

## Repository Structure



## Planned Updates
- Cleaning and operationalizing all variables from data collected via constructed pipeline
- Training and deploying a fine-tuned BERT model using HuggingFace
- Finalizing dataset by adding BLS measures for March 2026 and performing regressions with Stata

