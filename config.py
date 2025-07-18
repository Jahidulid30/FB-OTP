import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")

SOURCE_GROUPS = os.getenv("SOURCE_GROUPS").split(",")  # একাধিক গ্রুপ থাকলে কমা দিয়ে দাও
TARGET_GROUP = int(os.getenv("TARGET_GROUP"))
