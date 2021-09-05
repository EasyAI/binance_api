# binance_api
Contains all currently availible api endpoints found at the binanace docs.

## Description
This api is written with the endpoint reference of the docs found here: https://binance-docs.github.io/apidocs/spot/en/#change-log,
I decided to re-do the api to as the one I was using was dated and I will update projects to use this one as well as implementing it in future projects

### Repository Contains:
- binance_api
  - api_master_rest_caller.py : This is where the main rest api object is created "Binance_REST".
  - api_master_socket_caller.py : This is where the main socket api object is created "Binance_SOCK".
  - api_support_tools.py : Holds logic to create custom candle intervals/limits/other support toold.
  - formatter.py : this is used for standerdizing formats when combinding rest data with socket data to combined update and live data together.
  - blvt_api.py : Holds blvt api endpoint objects.
  - bswap_api.py : Holds bswap api endpoint objects.
  - futures_api.py : Holds futures api endpoint objects.
  - margin_api.py : Holds margin api endpoint objects.
  - marketData_api.py : Holds market data api endpoint objects.
  - mining_api.py : Holds margin api endpoint objects.
  - savings_api.py : Holds savings api endpoint objects.
  - spot_api.py : Holds spot api endpoint objects.
  - subAccount_api.py : Holds sub account api endpoint objects.
  - userDataStream_api.py : Holds user data stream api endpoint objects.
  - wallet_api.py : Holds wallet api endpoint objects.
  - websocket_api.py : Holds websocket api endpoint objects.

## Usage
To quickly install all the required modules use 'pip3 install -r requirements', this should install the modules for you.

### Rest Master:
To create a rest connection you need to initilise a rest object, you can do so with or without giving your api keys however some rest calls will be unavailable unlesss you provide the keys.

### Socket Master:
To create a socket connection you must only create a socket obejct and it will handle everything for you, you just need to access "Binance_SOCK.socketBuffer" for the data collected.

### Contact
Please if you find any bugs or issues contact me so I can improve.
EMAIL: jlennie1996@gmail.com
