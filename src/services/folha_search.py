from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FolhaSearchService:
    def __init__(self, driver, timeout_seconds=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout_seconds)

    def scrape_first_page(self, url):
        self.driver.get(url)

        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "li.c-headline--newslist")
            )
        )

        items = []
        seen = set()

        cards = self.driver.find_elements(
            By.CSS_SELECTOR, "li.c-headline--newslist"
        )

        for card in cards:
            link_el = card.find_element(
                By.CSS_SELECTOR, "div.c-headline__wrapper a"
            )
            article_url = link_el.get_attribute("href")

            title = (
                card.find_element(By.CSS_SELECTOR, "h2.c-headline__title")
                .text.strip()
            )

            desc_els = card.find_elements(
                By.CSS_SELECTOR, "p.c-headline__standfirst"
            )
            description = desc_els[0].text.strip() if desc_els else ""

            time_els = card.find_elements(
                By.CSS_SELECTOR, "time.c-headline__dateline"
            )
            date_text = time_els[0].text.strip() if time_els else ""

            img_els = card.find_elements(
                By.CSS_SELECTOR, "div.c-headline__media-wrapper img"
            )
            image_url = img_els[0].get_attribute("src") if img_els else ""

            if not article_url or not title:
                continue
            if article_url in seen:
                continue
            seen.add(article_url)

            items.append(
                {
                    "title": title,
                    "description": description,
                    "date": date_text,
                    "url": article_url,
                    "image_url": image_url,
                }
            )

        return items
