from warehouse.etl.bronze import BronzeLayerETL


def main():
    bronze = BronzeLayerETL()
    df = bronze.fetch_cust_info()
    df.show()
    bronze.write_to_postgres(df, table_name="crm_cust_info", schema="bronze")


if __name__ == "__main__":
    main()
