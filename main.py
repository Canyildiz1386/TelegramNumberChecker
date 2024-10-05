import time
from telethon.sync import TelegramClient
from telethon.errors import PhoneNumberBannedError, SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError, FloodWaitError
import uuid

api_id = '23262291'
api_hash = '77c460c8142ca13f32c27ac389db2e35'

# Function to generate a unique session name using UUID
def generate_session_name():
    return 'session_' + str(uuid.uuid4())

def check_telegram_number(phone_number):
    session_name = generate_session_name()  # Create a unique session name
    client = TelegramClient(session_name, api_id, api_hash)

    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            print(f"The phone number {phone_number} is okay!")
            return "OK"
    except PhoneNumberBannedError:
        print(f"The phone number {phone_number} is banned.")
        return "Not OK"
    except PhoneNumberInvalidError:
        print(f"The phone number {phone_number} is invalid.")
        return "Not OK"
    except SessionPasswordNeededError:
        print(f"Password needed for the account with {phone_number}.")
        return "OK"
    except FloodWaitError as e:
        wait_time = e.seconds
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
        return check_telegram_number(phone_number)  # Retry after waiting
    finally:
        client.disconnect()

def process_numbers(input_file, ok_file, not_ok_file):
    with open(input_file, 'r') as f:
        phone_numbers = f.readlines()

    with open(ok_file, 'w') as ok_f, open(not_ok_file, 'w') as not_ok_f:
        for number in phone_numbers:
            phone_number = number.strip()
            result = check_telegram_number(phone_number)
            
            if result == "OK":
                ok_f.write(phone_number + '\n')
            else:
                not_ok_f.write(phone_number + '\n')

input_file = 'phone_numbers.txt'
ok_file = 'ok_numbers.txt'
not_ok_file = 'not_ok_numbers.txt'

process_numbers(input_file, ok_file, not_ok_file)
