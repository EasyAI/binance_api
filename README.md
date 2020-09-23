# binance_api
Contains the following binance apis: MARGIN, SPOT (normal), WEBSOCKET, WAPI, USER DATA STREAM

## Description
This api is written with the endpoint reference of the docs found here: https://github.com/binance-exchange/binance-official-api-docs,
I decided to re-do the api to as the one I was using was dated and I will update projects to use this one as well as implementing it in future projects

### Repository Contains:
- binance_api
  - rest_master.py : This is where the main rest api object is created "Binance_REST".
  - socket_master.py : This is where the main socket api object is created "Binance_SOCK".
  - custom_data_formatter.py : Holds logic to create custom candle intervals/limits.
  - margin_api.py : This contains object datasets for each margin api endpoint.
  - spot_api.py : This contains object datasets for each spot (normal) api endpoint.
  - wapi_api.py : This contains object datasets for each wapi api endpoint.
  - userDataStream_api.py : This contains object datasets for each user data stream api endpoint.
  - websocket_api.py : This contains object datasets for each websocket api stream.
  - formatter.py : this is used for standerdizing formats when combinding rest data with socket data to combined update and live data together.

## Usage
To quickly install all the required modules use 'pip3 install -r requirements', this should install the modules for you.

### Rest Master:
To create a rest connection you need to initilise a rest object, you can do so with or without giving your api keys however some rest calls will be unavailable unlesss you provide the keys.

### Socket Master:
To create a socket connection you must only create a socket obejct and it will handle everything for you, you just need to access "Binance_SOCK.socketBuffer" for the data collected.

### Contact
Please if you find any bugs or issues contact me so I can improve.
EMAIL: jlennie1996@gmail.com
