from scripts.bronze.layer import BronzeLayerETL


def main():
    bronzeLayerETL = BronzeLayerETL()
    df = bronzeLayerETL.fetch_cust_info()
    df.show()
    bronzeLayerETL.write_to_postgres(df, table_name="crm_cust_info", schema="bronze")

if __name__ == "__main__":
    main()
