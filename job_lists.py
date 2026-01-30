from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
import time
import csv
import sys

def main():
    try:
        print('Select the serial number, based on your priority')
        print('1. All India Govt Jobs\n' \
        '2. State Govt Jobs\n' \
        '3. Bank Jobs\n' \
        '4. Teaching Jobs\n' \
        '5. Engineering Jobs\n' \
        '6. Railway Jobs\n' \
        '7. Police/Defence Jobs\n')
        n = int(input('\n'))
    except:
        sys.exit('Improper input. Please try again')
    scrap(n)
    print('Successfully completed, you can check job_info.csv .')

def scrap(n):

    # blocking any logging or permission notification
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")

    website = 'https://www.freejobalert.com/'
    path = 'C:\Scrapping_j\chromedriver.exe'

    states = ['andaman and nicobar', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh',
              'dadra and nagar haveli', 'daman and diu', 'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 
              'jammu and kashmir', 'jharkhand', 'karnataka', 'kerala', 'lakshadweep', 'madhya pradesh', 'maharashtra', 'manipur', 
              'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil nadu',
              'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']

    # central govt jobs
    if n == 1 :
        headers = []
        root = 'government-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[4]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)
        
        # storing the job info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # state govt jobs
    elif n == 2 :
        try:
            state = input('Please enter the state: ').lower().strip()
            headers = []
            root = f'{state}-government-jobs/'
            driver = webdriver.Chrome(path, options=options)
            driver.get(website + root)
        except:
            sys.exit('Improper state name. PLease try again.')
        time.sleep(4)
        content = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[3]/tbody')

        # getting the header
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)

        # storing the info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting the number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # bank jobs
    elif n == 3 :
        headers = []
        root = 'bank-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[2]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)

        # getting the job info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting the number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # teaching jobs
    elif n == 4 :
        headers = []
        state = input('The state you want to work in? ').lower().strip()
        if state not in states:
            sys.exit("Either the state spelling is wrong or we don't have data about that state")
        root = 'teaching-faculty-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, f'/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[{states.index(state)+3}]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)
        

        # getting the job content
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting the number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # engineering jobs
    elif n == 5 :
        headers = []
        state = input('The state you want to work in? ').lower().strip()
        if state not in states:
            sys.exit("Either the state spelling is wrong or we don't have data about that state")
        root = 'engineering-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, f'/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[{states.index(state)+4}]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)
        
        # getting the job info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            time.sleep(20)
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # railway jobs
    elif n == 6 :
        headers = []
        root = 'railway-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[2]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)
        
        # getting the job info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            # getting the number of rows
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')
            
    # police/ defence jobs
    elif n == 7 :
        headers = []
        root = 'police-defence-jobs/'
        driver = webdriver.Chrome(path, options=options)
        driver.get(website + root)
        time.sleep(4)
        content = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/main/article/div/div[3]/table[2]/tbody')

        # getting the headers
        header = content.find_elements(By.XPATH, '//tr[1]/th')
        for heading in header:
            if heading not in headers:
                headers.append(heading.text)
        
        # getting the job info
        with open('job_info.csv', 'a', encoding='utf-8') as file:
            job_info = csv.DictWriter(file, fieldnames=headers)
            job_info.writeheader()
            no = len(content.find_elements(By.XPATH, '//tr'))
            try:
                for row in range(2, no+1):
                    job_content = []
                    jobs = content.find_elements(By.XPATH, f'//tr[{row}]/td')
                    for job in jobs:
                        if job not in job_content:
                            job_content.append(job.text)
                    job_info.writerow({headers[0]: job_content[0], headers[1]: job_content[1], headers[2]: job_content[2], headers[3]: job_content[3], headers[4]: job_content[4], headers[5]: job_content[5]})
            except:
                sys.exit('Sorry for the inconvenience. Thats all we can scrape')

    # out of options
    else:
        sys.exit('Incorect serial number')
    
    driver.quit()

if __name__ == '__main__':
    main()