# How to start project for development?

## Make `.env` file
- Copy `.env.example` to `.env` and configure it if you need.

## Set USPS_USER_ID for USPS provider
- Get USER_ID (Username) from [registration.shippingapis.com](https://registration.shippingapis.com/)
- Replace env `USPS_USER_ID=YOUR_USPS_USER_ID` in .env file.

## Set USPS_PROXY_SERVER for USPS provider
- Get credentials for proxy server kind of `http://user:pass@host:port`
- Replace env `USPS_PROXY_SERVER=http://user:pass@host:port` in .env file.

## Run docker
- Run from root directory `docker compose up`

## Use backend
- Open [http://127.0.0.1:8003/](http://127.0.0.1:8003/)


<br>
<br>
<br>


# How to deploy project for production?

## Turns off debug mode
> **Warning**
> Never deploy a site into production with DEBUG turned on.
- Replace env `DEBUG=false` in .env file.

## Set secret key
> **Warning**
> This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
- Generate secret key `python manage.py generate_secret_key`
- Replace env `SECRET_KEY=UNIQUE_SECRET_KEY` in .env file.

## Synchronizes database
- Run `python manage.py migrate`
