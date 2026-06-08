# Evaluating ghost job probability based on web-scraped job posting data from Linkedin, Glassdoor, and Indeed
The Congressional Research Service (CRS) defines ghost jobs as online postings by legitimate firms without any intention to hire in the foreseeable future. Such practices directly harm job-seekers, resulting in not just lost time and energy, but potential psychological distress. Previous studies estimate that 20% of job postings on digital labor platforms are ghost jobs, creating distortions that impact the accuracy of economic measures. This project investigates the the connection between job posting characteristics and suspected ghost job posting prevalence on digital labor platforms, using listing age as a proxy for ghost job probability

### Features
- Real-time web-scraping based on user-defined occupations and platforms (i.e. Linkedin, Glassdoor, Indeed)
- 

### Technologies Used
- JobSpy (open-source library that webscrapes job posting data from digital labor platforms)
- Python 3.12
- Pandas (data cleaning and transformation)
- Matplotlib (data visualization)

### Limitations


### Known Issues

## Repository Structure
The current version only has one root folder, Jobscraper. However, as the project evolves, there will be a second folder for the fine-tuned BERT model once it's developed and a separate folder containing code for running regressions. 


## Setup and Installation 

## How to Run
1. Clone the repository:
```
git clone 
```
2. Install JobSpy using the setup instructions listed on the repository
3. 

## Planned Updates
- Cleaning and operationalizing all variables from data collected via constructed pipeline
- Training and deploying a fine-tuned BERT model using HuggingFace
- Finalizing dataset by adding BLS measures for March 2026 and performing regressions with Stata

