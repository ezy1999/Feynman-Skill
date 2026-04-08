"""Fetch Feynman historical data from online sources."""
from feynman_taste.data.fetcher import FeynmanDataFetcher

def main():
    fetcher = FeynmanDataFetcher()
    records = fetcher.fetch_all()
    print(f"\nDone! {len(records)} evidence records.")

if __name__ == "__main__":
    main()
