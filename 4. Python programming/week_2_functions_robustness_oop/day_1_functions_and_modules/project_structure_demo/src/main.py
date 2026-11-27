from data_transformations import fetch_data, clean_data, save_data


def main():
    data = fetch_data()
    cleaned_data = clean_data()
    save_data()
    print("Data processing complete.")


main()
