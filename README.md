# Job_Scraper

## Overview
A selenium based web scraper that extracts job data from 'freejobalert.com' with domain filtering and state specific job searches for some domains. Built to handle dynamic website structures that change daily.

## Features
+ Interactive domain selection.
+ State wise filtering foe specific jobs.
+ Multi page scraping
+ CSV data export and error handling.

## Tech Stack
**Language:** Python 3.9.2 </br>
**Modules:** Selenium, csv, time, sys

## How It Works
1. Runs from command line, presents 7 job domain options and for state govt jobs, teaching and engineering jobs ask for preferred state, along the way validates user inputs.
2. Initialises selenium webdriver with chrome, navigates to website based on domain preference and dynamically identifies current job listings
3. Extracts from each job: Post Date, Recruitment Board, Exam / Post Name, Qualification, Advt No and Last Date.
4. Cleans and formats extracted data and saves to csv.
5. Waits for element loading and try and except block for error handling is present in each block.

## Installation and Usage
**Installation:** selenium (pip installation) and webdriver </br>
**Usage:** To use run **python job_lists.py** in the terminal.

## Applications
+ Automate daily job hunting across multiple domains and save time on manual web browsing.
+ Useful in tracking job market trends and qualifications required over time.
+ It can be used to learn web scraping, error handling and data storage.

## What I Learned
+ Persistence and patience.
+ Handling dynamic websites that change on regular basis (as fixed element counts don't work).
+ Handling nested data, proper waits, managing browser sessions and dynamic content.
+ Ethical scraping with rate limits and delays.
+ Comprehensive error handling and proper data outputing.

## Future Modification
1. Automated scheduling with the integration of schedule library.
2. Integrate ezgmail library for email automation to users to their provided email.
3. Storage of user profile, so that user need not provide information for every use.

## Important Note
+ This project is for educational and learning experience.
+ Always check robots.txt and respect website terms of service.
+ The website may update their HTML structure.
+ The more frequently you scrape daily, the lesser the data you get due to website limitation.

## Contributions
Contributions are welcomed to enchance the scraper.

### How to Contribute
1. **Describe issue or new features:** clear description, steps taken and comparison.
2. **Make code changes:** fork the repository, create a new branch, make changes, test thoroughly and commit with clear message.
3. **Submit a pull request**
