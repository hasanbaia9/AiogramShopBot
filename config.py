import os
from dotenv import load_dotenv
from enums.currency import Currency
from enums.runtime_environment import RuntimeEnvironment
from utils.utils import hash_password

# load_dotenv()  # Render-এ env vars সরাসরি থাকে, তাই এই লাইন কমেন্ট করলেও চলে

# ========== রেন্ডারের জন্য ওভাররাইড ==========
# RUNTIME_ENVIRONMENT: Render-এ 'prod' দিলে সেটা Enum-এর সাথে মিলিয়ে নিন।
# আপনার enum-এ 'PRODUCTION' থাকলে 'PRODUCTION' লিখুন, 'prod' থাকলে 'prod' লিখুন।
# আমি ধরে নিচ্ছি 'PRODUCTION' আছে – আপনার ফাইল চেক করে নিন।
RUNTIME_ENVIRONMENT_STR = os.environ.get("RUNTIME_ENVIRONMENT", "PRODUCTION")
try:
    RUNTIME_ENVIRONMENT = RuntimeEnvironment(RUNTIME_ENVIRONMENT_STR)
except ValueError:
    # যদি ভুল হয়, তাহলে ডিফল্ট প্রোডাকশন সেট করুন
    RUNTIME_ENVIRONMENT = RuntimeEnvironment.PRODUCTION

# WEBHOOK_HOST সরাসরি এনভায়রনমেন্ট থেকে নিন, কোনো ফাংশন কল করবেন না
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
if not WEBHOOK_HOST:
    # Render-এর স্বয়ংক্রিয় URL ব্যবহার করতে চাইলে এখানে সেট করুন
    WEBHOOK_HOST = "https://your-app-name.onrender.com"  # পরিবর্তন করুন

WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/webhook")
WEBAPP_HOST = os.environ.get("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(os.environ.get("WEBAPP_PORT", "10000"))  # Render ডিফল্ট 10000
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN environment variable is required")

ADMIN_ID_LIST_STR = os.environ.get("ADMIN_ID_LIST")
if not ADMIN_ID_LIST_STR:
    raise ValueError("ADMIN_ID_LIST is required")
ADMIN_ID_LIST = [int(admin_id.strip()) for admin_id in ADMIN_ID_LIST_STR.split(',') if admin_id.strip()]

SUPPORT_LINK = os.environ.get("SUPPORT_LINK", "")

# ========== ডাটাবেস (PostgreSQL) ==========
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_HOST = os.environ.get("DB_HOST", "postgres")
DB_NAME = os.environ.get("POSTGRES_DB", "aiogram-shop-bot")

PAGE_ENTRIES = int(os.environ.get("PAGE_ENTRIES", "8"))
MULTIBOT = os.environ.get("MULTIBOT", "false").lower() == 'true'

CURRENCY_STR = os.environ.get("CURRENCY", "USD")
try:
    CURRENCY = Currency(CURRENCY_STR)
except ValueError:
    CURRENCY = Currency.USD  # ডিফল্ট

KRYPTO_EXPRESS_API_KEY = os.environ.get("KRYPTO_EXPRESS_API_KEY")
KRYPTO_EXPRESS_API_URL = os.environ.get("KRYPTO_EXPRESS_API_URL")
KRYPTO_EXPRESS_API_SECRET = os.environ.get("KRYPTO_EXPRESS_API_SECRET")
WEBHOOK_SECRET_TOKEN = os.environ.get("WEBHOOK_SECRET_TOKEN")

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
TELEGRAM_PROXY_URL = os.environ.get("TELEGRAM_PROXY_URL")

# ক্রিপ্টো ফরওয়ার্ডিং (BDT ম্যানুয়াল ব্যবহার করলে বন্ধ রাখুন)
CRYPTO_FORWARDING_MODE = os.environ.get("CRYPTO_FORWARDING_MODE", "false").lower() == 'true'
BTC_FORWARDING_ADDRESS = os.environ.get("BTC_FORWARDING_ADDRESS")
LTC_FORWARDING_ADDRESS = os.environ.get("LTC_FORWARDING_ADDRESS")
ETH_FORWARDING_ADDRESS = os.environ.get("ETH_FORWARDING_ADDRESS")
SOL_FORWARDING_ADDRESS = os.environ.get("SOL_FORWARDING_ADDRESS")
BNB_FORWARDING_ADDRESS = os.environ.get("BNB_FORWARDING_ADDRESS")
DOGE_FORWARDING_ADDRESS = os.environ.get("DOGE_FORWARDING_ADDRESS")

# রেফারেল সিস্টেম (ডিফল্ট মান)
MIN_REFERRER_TOTAL_DEPOSIT = int(os.environ.get("MIN_REFERRER_TOTAL_DEPOSIT", "500"))
REFERRAL_BONUS_PERCENT = float(os.environ.get("REFERRAL_BONUS_PERCENT", "5"))
REFERRAL_BONUS_DEPOSIT_LIMIT = int(os.environ.get("REFERRAL_BONUS_DEPOSIT_LIMIT", "3"))
REFERRER_BONUS_PERCENT = float(os.environ.get("REFERRER_BONUS_PERCENT", "3"))
REFERRER_BONUS_DEPOSIT_LIMIT = int(os.environ.get("REFERRER_BONUS_DEPOSIT_LIMIT", "5"))
REFERRAL_BONUS_CAP_PERCENT = float(os.environ.get("REFERRAL_BONUS_CAP_PERCENT", "7"))
REFERRER_BONUS_CAP_PERCENT = float(os.environ.get("REFERRER_BONUS_CAP_PERCENT", "7"))
TOTAL_BONUS_CAP_PERCENT = float(os.environ.get("TOTAL_BONUS_CAP_PERCENT", "12"))

SQLADMIN_RAW_PASSWORD = os.environ.get("SQLADMIN_RAW_PASSWORD")
SQLADMIN_HASHED_PASSWORD = hash_password(SQLADMIN_RAW_PASSWORD) if SQLADMIN_RAW_PASSWORD else None

JWT_EXPIRE_MINUTES = int(os.environ.get("JWT_EXPIRE_MINUTES", "30"))
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is required for security")
