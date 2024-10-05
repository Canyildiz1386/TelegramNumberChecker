from telethon.sync import TelegramClient
from telethon.errors import PhoneNumberBannedError, SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

api_id = '23262291'
api_hash = '77c460c8142ca13f32c27ac389db2e35'

def check_telegram_number(phone_number):
    client = TelegramClient('anon', api_id, api_hash)

    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            print("The phone number is okay!")
            return "OK"
    except PhoneNumberBannedError:
        print("The phone number is banned.")
        return "Not OK"
    except PhoneNumberInvalidError:
        print("The phone number is invalid.")
        return "Not OK"
    except SessionPasswordNeededError:
        print("Password needed for the account.")
        return "OK"
    finally:
        client.disconnect()

phone_number = input("Enter the phone number with country code (e.g., +123456789): ")
check_telegram_number(phone_number)
