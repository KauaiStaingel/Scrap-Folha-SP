from services.driver import SeleniumDriver
from services.folha_search import FolhaSearchService
from services.search_query import SearchQueryBuilder
from services.excel import CsvNewsSaver
import time


def orchestrator_main():
    max_retries = 3
    attempt = 0

    query_builder = SearchQueryBuilder()
    encoded_query = query_builder.ask()

    search_url = f"https://search.folha.uol.com.br/?q={encoded_query}&site=todos"

    context = {
        "search_url": search_url,
        "headless": True,
        "timeout_seconds": 15,
    }

    while attempt < max_retries:
        driver = None
        try:
            attempt += 1
            print(f"Tentativa {attempt} de {max_retries}")

            driver_builder = SeleniumDriver(
                headless=context.get("headless", True)
            )

            driver = driver_builder.create()

            service = FolhaSearchService(
                driver,
                timeout_seconds=context.get("timeout_seconds", 15),
            )

            noticias = service.scrape_first_page(context["search_url"])
            context["noticias"] = noticias

            saver = CsvNewsSaver(noticias)
            saver.save("noticias.csv")

            return context

        except Exception as e:
            print(f"Erro na tentativa {attempt}: {e}")

            if attempt >= max_retries:
                print("Número máximo de tentativas atingido")
                raise

            time.sleep(2)

        finally:
            if driver:
                driver.quit()
