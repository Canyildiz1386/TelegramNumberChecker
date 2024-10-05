
# 📞 TelegramNumberChecker

🔍 **TelegramNumberChecker** is a Python tool that checks the status of phone numbers on Telegram! It helps you determine if a phone number is valid, banned, or requires additional login information such as a password.

🚀 **Features**:
- ✅ Check if a phone number is **valid** on Telegram.
- 🚫 Detect if a phone number is **banned**.
- 🔐 Handle cases where a **password** is required for login.
- 🕒 Automatically handles Telegram's rate limits with a wait and retry mechanism.

## 🛠️ Installation

1. First, clone the repo:

```bash
git clone https://github.com/Canyildiz1386/TelegramNumberChecker.git
```

2. Install the required packages:

```bash
pip install telethon
```

3. You also need to get your own **API ID** and **API Hash** from [my.telegram.org](https://my.telegram.org).

## 🔧 Configuration

1. Open the `main.py` file.
2. Replace the `api_id` and `api_hash` with your own values:
   ```python
   api_id = 'your_api_id'
   api_hash = 'your_api_hash'
   ```

## 🚀 Usage

1. Create a text file called `phone_numbers.txt` in the same directory as the script.
2. Add the phone numbers you want to check, one per line, in this format:
   ```
   +1234567890
   +9876543210
   ```
3. Run the script:

```bash
python3 main.py
```

4. The results will be saved in:
   - `ok_numbers.txt` for valid numbers. ✅
   - `not_ok_numbers.txt` for banned or invalid numbers. 🚫

## 🔄 Handling Rate Limits
This script automatically handles Telegram's rate-limiting with the `FloodWaitError` exception. If Telegram asks you to wait, the script will pause and retry after the specified time. ⏳

## 📂 File Structure

```bash
TelegramNumberChecker/
├── main.py          # The main script
├── phone_numbers.txt # Input file with phone numbers
├── ok_numbers.txt    # Output file for valid numbers
├── not_ok_numbers.txt # Output file for banned or invalid numbers
```

## 🤝 Contributing

Contributions are welcome! 🎉 If you find any bugs 🐛 or have any suggestions 💡, feel free to open an issue or submit a pull request.

## 🛡️ License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Happy checking! 🎉🔍
