# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
from tqdm import tqdm
import click
from datetime import datetime


def scrape_it(job_key_arg, location_arg):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        # chrome_options=options
    )

    driver.get(
        "https://www.linkedin.com/jobs/jobs-in-curitiba-pr?trk=homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0"
    )
    sleep(2)

    job_title = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input"
    )
    job_title.click()

    job_title.send_keys(job_key_arg)

    job_location = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input"
    )
    job_location.click()
    sleep(4)
    job_location.clear()
    sleep(2)
    job_location.send_keys(location_arg)

    sleep(2)
    # actions.send_keys(Keys.ARROW_DOWN.perform())
    job_location.send_keys(Keys.ARROW_DOWN)
    sleep(3)
    job_location.send_keys(Keys.RETURN)
    # sleep(2)
    sleep(4)

    while True:
        height = driver.execute_script("return document.body.scrollHeight")
        sleep(1)
        driver.execute_script("window.scrollTo(0, window.scrollY + 500000)")
        sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        sleep(2)
        if new_height == height:
            break

    job_box = driver.find_elements_by_class_name("base-card")

    # CREATES THE DATAFRAME
    try:
        jobs_table = pd.read_csv("data/jobs_table.csv", index_col=0)
    except:
        jobs_table = pd.DataFrame(
            columns=[
                "job_title",
                "company",
                "location",
                "description",
                "level",
                "updated_at",
            ]
        )

    for job in tqdm(range(len(job_box))):
        try:

            job_box[job].click()
            sleep(3)
            # SCRAPING THE JOB PAGE

            job_title = driver.find_element_by_class_name("topcard__title").text
            print(job_title)

            sleep(1)
            company_name = driver.find_element_by_class_name(
                "topcard__org-name-link"
            ).text
            sleep(1)

            location = driver.find_element_by_class_name("topcard__flavor--bullet").text

            location
            sleep(1)

            description = driver.find_element_by_class_name(
                "show-more-less-html__markup--clamp-after-5"
            ).text

            level = driver.find_element_by_class_name(
                "description__job-criteria-text"
            ).text

            if level:
                level = level
            else:
                level = "Undefined"
            sleep(1)

            if description:
                description = description
            else:
                description = "Undefined"
            sleep(1)

            current_time = datetime.now()

            job_row = [
                job_title,
                company_name,
                location,
                description,
                level,
                current_time,
            ]

            job_row

            jobs_table = jobs_table.append(
                pd.DataFrame([job_row], columns=list(jobs_table.columns))
            )
            jobs_table
        except:
            pass

    jobs_table.to_csv("data/jobs_table.csv")

    driver.close()
