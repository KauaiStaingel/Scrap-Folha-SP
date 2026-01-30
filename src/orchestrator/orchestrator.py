from services.driver import SeleniumDriver
from services.folha_search import FolhaSearchService
from services.search_query import SearchQueryBuilder
from services.excel import CsvNewsSaver


def orchestrator_main():

    query_builder = SearchQueryBuilder()
    encoded_query = query_builder.ask()

    search_url = f"https://search.folha.uol.com.br/?q={encoded_query}&site=todos"

    context = {
        "search_url": search_url,
        "headless": True,
        "timeout_seconds": 15,
    }


    driver_builder = SeleniumDriver(
        headless=context.get("headless", True)
    )

    driver = driver_builder.create()

    try:
        service = FolhaSearchService(
            driver,
            timeout_seconds=context.get("timeout_seconds", 15),
        )

        noticias = service.scrape_first_page(context["search_url"])
        context["noticias"] = noticias

        saver = CsvNewsSaver(noticias)
        saver.save("noticias.csv")

        

        return context

    finally:
        driver.quit()
