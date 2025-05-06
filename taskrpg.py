# taskrpg.py

# Imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3
import json
from datetime import datetime

# Config
# Load secrets and config from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DB_PATH = os.getenv("DB_PATH", "xp.db")
ACTIVITY_CONFIG = "activities.json"

# Database Setup
# Connect to SQLite DB and initialize, if needed
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    last_activity TEXT,
    total_logs INTEGER DEFAULT 0
)
''')
conn.commit()

# Bot Setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Helper Functions
def get_user_data(user_id):
    pass  # Load user row or insert default if missing

def add_xp(user_id, amount):
    pass  # Add XP and update total_logs, last_activity

def check_level_up(user_id):
    pass  # Increase level if XP exceeds threshold

def load_activities():
    with open(ACTIVITY_CONFIG) as f:
        return json.load(f)

# Commands
@bot.command(name="log")
async def log_activity(ctx, *, activity):
    pass  # Add XP for activity, respond with gains

@bot.command(name="xp")
async def show_xp(ctx):
    pass  # Show current XP and level

@bot.command(name="profile")
async def profile(ctx):
    pass  # Show stats like last activity, logs

@bot.command(name="leaderboard")
async def leaderboard(ctx):
    pass  # Show top 5 users

@bot.command(name="activities")
async def show_activities(ctx):
    pass  # List all activities and XP values

# Start
bot.run(TOKEN)
