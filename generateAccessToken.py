import requests
import json
import getpass

# Get username and password for Victon Energy API
print("Please login with your Victron Energy Credentials")

user = input("Username: ")
pw = getpass.getpass()

result = requests.post('https://vrmapi.victronenergy.com/v2/auth/login' ,json = { 'username': user, 'password': pw })

if result.status_code == 200:

	response_json = result.json()
	userId = response_json["idUser"]
	authToken = response_json["token"]
	print('Authenticated, generating user token for user ', userId)

	result2 = requests.post('https://vrmapi.victronenergy.com/v2/users/{userId}/accesstokens/create'.format(userId = userId),
		headers = { 'X-Authorization': "Bearer %s" %authToken},
		json = { 'name': 'Access token 3'}
	)

	if result2.status_code == 200:

		response_json = result2.json()
		token = response_json["token"]

		print('Generated AUTH Token ', token)

	else:
		print("Problem with API request:%s  text:%s"%(result2.status_code, result2.text))

elif result.status_code == 401:
	print("Unable to authenticate")

else:
	print("Problem authenticating status code:%s  text:%s"%(result.status_code, result.text))
