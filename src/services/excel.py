import csv


class CsvNewsSaver:
    def __init__(self, noticias):
        self.noticias = noticias

    def save(self, filepath):
        fieldnames = ["title", "description", "date", "url", "image_url"]

        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for n in self.noticias:
                writer.writerow(
                    {
                        "title": n.get("title", ""),
                        "description": n.get("description", ""),
                        "date": n.get("date", ""),
                        "url": n.get("url", ""),
                        "image_url": n.get("image_url", ""),
                    }
                )
