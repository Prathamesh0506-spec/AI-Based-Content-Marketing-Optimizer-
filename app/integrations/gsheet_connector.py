import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SERVICE_ACCOUNT_FILE = "credentials/service_account.json"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

def write_to_sheet(sheet_name, data):
    """Appends data to the specified Google Sheet."""
    sheet = client.open(sheet_name).sheet1
    sheet.append_row(data)
    print("Data written successfully!")

if __name__ == "__main__":
    sample_data = ["Eco Water Bottle", "Great caption for eco-lovers", "High Engagement", 0.95]
    write_to_sheet("MarketingCampaignData", sample_data)
