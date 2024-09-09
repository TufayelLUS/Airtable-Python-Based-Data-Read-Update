from pyairtable import Api
import os

# Airtable credentials
AIRTABLE_API_KEY = ""
BASE_ID = ''
TABLE_NAME = ''


api = Api(AIRTABLE_API_KEY)
table = api.table(BASE_ID, TABLE_NAME)


# Function to fetch all records from the table
def fetch_records():
    try:
        records = table.all()  # Fetch all records from Airtable
        print("Fetched records:")
        for record in records:
            print(record['fields'])  # Print each record's fields
        return records
    except Exception as e:
        print(f"Error fetching records: {e}")

# Function to update a specific record by its ID
def update_record(record_id, updated_fields):
    try:
        updated_record = table.update(record_id, updated_fields)  # Update the record with new fields
        print(f"Record updated: {updated_record['fields']}")
        return updated_record
    except Exception as e:
        print(f"Error updating record: {e}")

# Fetch all records
records = fetch_records()

# Example: Update the first record with new data
if records:
    record_id = records[0]['id']  # Get the ID of the first record
    updated_data = {'Name': 'Updated Name'}  # Example fields to update
    update_record(record_id, updated_data)
