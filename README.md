# Ghost-Jobs-Research
Ghost jobs are becoming increasingly prevalent on digital labor platforms (e.g. Linkedin, Glassdoor, Indeed). One report released by career website ResumeUp.AI suggests that [27.4% of US job listings on Linkedin are ghost jobs, while hiring platform, Greenhouse, disclosed that 18-22% of listings on their site]([url](https://www.entrepreneur.com/business-news/one-quarter-of-jobs-posted-online-are-fake-ghost-jobs-study/496683)) were likely ghost jobs. The Congressional Research Service (CRS) defines ghost jobs as online postings by legitimate firms without any intention to hire in the foreseeable future. Such practices directly harm job-seekers, resulting in not just lost time and energy, but potential psychological distress. Previous studies estimate that 20% of job postings on digital labor platforms are ghost jobs, creating distortions that impact the accuracy of economic measures. As a result, this reduces the effectiveness of policy-makers due to misallocated policy attention and resources. Despite growing evidence of ghost jobs, there is no research examining whether labor market conditions impact their pervasiveness on digital labor platforms. This project investigates the impact of labor market conditions on suspected ghost job posting prevalence on digital labor platforms, proposing that firms strategically deploy ghost jobs during periods of high unemployment. 

## Repository Structure
The current version only has one root folder, Jobscraper. However, as the project evolves, there will be a second folder for the fine-tuned BERT model once it's developed and a separate folder containing code for running regressions. 

### Jobscraper
This folder contains two sub-folders: bls_data and data files. 

#### bls_data
The bls_data contains a jupyter notebook file that loaded 2024 BLS OEWS data and then determined the top five most common occupations for the following sectors: Professional, Scientific, and Technical Services; Information; Retail Trade; Healthcare & Social Assistance; Finance & Insurance. For occupations that are cross-sector, the sector that had greater total employment retained that occupation, while the other sector had it replaced with the next highest ranked occupation. 

#### data files
The data files folder contains two additional sub-folders named midterm and pilot. The midterm is a preliminary data exploration of data collected for three sectors (Professional, Scientific, and Technical Services; Finance & Insurance; Retail Trade) for job postings scraped for one day (February 23, 2026). The pilot folder contains a jupyter notebook script used to test and finalize the data pipeline script, with the final code transferred to webscrape_script.py for automation through Windows Task Scheduler. 

## Data Sources
- Bureau of Labor Statistics (BLS) OEWS
- Digital Labor Platforms (Linkedin, Glassdoor, Indeed)
- [JobSpy]([url](https://github.com/speedyapply/JobSpy))

## Setup and Installation 

## How to Run

## Planned Updates
- Cleaning and operationalizing all variables from data collected via constructed pipeline
- Training and deploying a fine-tuned BERT model using HuggingFace
- Finalizing dataset by adding BLS measures for March 2026 and performing regressions with Stata

