import requests
import json
import logging
from typing import Any


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ZalandoCollector:
    SCRAPE_URL = "https://api.brightdata.com/datasets/v3/scrape"
    DATASET_ID = "gd_lbqj6l5s28ofha6mlk"

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def collect_data(
        self, inputs: list[dict]
    ) -> list[dict] | None:
        logging.info(
            f"Scraping {len(inputs)} url(s)..."
        )
        try:
            response = requests.post(
                self.SCRAPE_URL,
                headers=self.headers,
                params={"dataset_id": self.DATASET_ID, "format": "json"},
                json=inputs,
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            logging.info(f"Received {len(data)} records")
            self._save_data(data)
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Scrape request failed: {str(e)}")
            return None

    def _save_data(
        self, data: list[dict[str, Any]], filename: str = "zalando_data.json"
    ) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving data: {str(e)}")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    scraper = ZalandoCollector(api_token)

    inputs = [
        {"url": "https://www.zalando.de/nike-air-max-90-sneaker-low-ni112n1sp-a11.html"},
        {"url": "https://www.zalando.de/adidas-originals-stan-smith-sneaker-low-ad116d0oc-a11.html"},
    ]

    scraper.collect_data(inputs)


if __name__ == "__main__":
    main()
