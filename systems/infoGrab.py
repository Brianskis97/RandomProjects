from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1IFzAfmEv-TOPfevdE1Lmmt89ewotMY5-MES8MdLtFKI'
SAMPLE_RANGE_NAME = 'Sheet1!A8:T77'

def main():
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	creds = None
				       # The file token.pickle stores the user's access and refresh tokens, and is
				       # created automatically when the authorization flow completes for the first
				       # time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
       		# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server()
			# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('sheets', 'v4', credentials=creds)

	#Call the Sheets API
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
	values = result.get('values', [])
	"""
	if not values:
		print('No data')
	else:
		print('Name, Major')
		for row in values:
			print(row[1] +" " + row[9])
	"""
	output = []
	prevName = ''
	if not values:
		print('No data')
	else: 
		tempoutput = ''
		for row in values:
			name = row[1]
			if prevName == '' or name != prevName:
				if tempoutput != '':
					output.append(tempoutput)
					tempoutput = ""
				tempoutput += row[0] + " " + row[1] + " Network Inventory\n"
				tempoutput += "MAC: [" + row[9] + "]\n"
			else:
				tempoutput += "MAC: [" + row[9] + "]\n"
			prevName = name
		output.append(tempoutput)
	for data in output:
		print(data)



main()
