# utility_operations.py

class UtilityOperations:
    def __init__(self, erp_data):
        self.erp_data = erp_data

    # Function to view AUD currency conversion table data
    def view_currency_conversion_table(self):
        table_headers = ["Country", "Curr Code", "Rate to AUD"]
        table_data = [
            {
                "Country": each_currency["Country"],
                "Curr Code": each_currency["Curr Code"],
                "Rate to AUD": str(each_currency["Rate to AUD"])
            }
            for each_currency in self.erp_data.currency_conversion_table
        ]
        col_widths_currency = self.erp_data.col_widths['currency_conversion_table']
        self.display_table(table_data, table_headers, col_widths_currency)