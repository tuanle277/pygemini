import os
import google.generativeai as genai
from dotenv import load_dotenv, set_key
import argparse

def load_env():
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    google_project_id = os.getenv("GOOGLE_PROJECT_ID")
    google_region_id = os.getenv("GOOGLE_REGION_ID")

    for var_name, var_value in {"GOOGLE_API_KEY": google_api_key, "GOOGLE_PROJECT_ID": google_project_id, "GOOGLE_REGION_ID": google_region_id}.items():
        if var_value is None:
            raise EnvironmentError(f"{var_name} is not set in the environment variables.")

    try:
        genai.configure(api_key=google_api_key)
        print("Google Generative AI client configured successfully.")
    except Exception as e:
        raise RuntimeError(f"Failed to configure Google Generative AI client: {e}")

    return google_project_id, google_region_id

def set_env():
    parser = argparse.ArgumentParser(description="Set environment variables for Google Generative AI client.")
    parser.add_argument('--api_key', required=True, help='Google API key')
    parser.add_argument('--project_id', required=True, help='Google Project ID')
    parser.add_argument('--region_id', required=True, help='Google Region ID')
    args = parser.parse_args()

    env_file = '.env'
    load_dotenv(env_file)
    for key, value in vars(args).items():
        set_key(env_file, key.upper(), value)
    
    print("Environment variables set successfully.")
