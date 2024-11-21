from surf_scrap import ScrapWeather
import argparse

def main():
    # Set up argument parser
    ap = argparse.ArgumentParser(description="Scrape surf weather data and save to CSV.")
    ap.add_argument("--link", help="Enter the URL of the surf web page", type=str, required=True)
    ap.add_argument("--save_path", help="Enter the path where you want to save the CSV file", type=str, required=True)
    args = ap.parse_args()

    # Call the function to fetch and save data
    ScrapWeather.Scrap_Weather(args.link, args.save_path)

if __name__ == "__main__":
    main()