import click

from scraper import scrape_it


@click.command()
@click.option("-j", "--job-title", "job_title")
@click.option("-l", "--location", "location")
def main(job_title, location):
    print(job_title, location)
    scrape_it(job_title, location)


if __name__ == "__main__":
    main()
