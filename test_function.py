import argparse
from modules.genimi import Gemini
from utils import load_env, set_env

def test_gemini():
    parser = argparse.ArgumentParser(description="Google Generative AI client.")
    subparsers = parser.add_subparsers(dest='command')

    setenv_parser = subparsers.add_parser('setenv', help='Set environment variables')
    setenv_parser.add_argument('--api_key', required=True, help='Google API key')
    setenv_parser.add_argument('--project_id', required=True, help='Google Project ID')
    setenv_parser.add_argument('--region_id', required=True, help='Google Region ID')

    prompt_parser = subparsers.add_parser('prompt', help='Generate response from prompt')
    prompt_parser.add_argument('prompt', help='Text prompt')

    image_parser = subparsers.add_parser('image', help='Generate response from image')
    image_parser.add_argument('path_or_url', help='Path or URL to image')
    image_parser.add_argument('prompt', help='Text prompt')

    chat_parser = subparsers.add_parser('chat', help='Generate response from chat')
    chat_parser.add_argument('chat', help='Chat message')

    video_parser = subparsers.add_parser('video', help='Generate response from video')
    video_parser.add_argument('path_or_url', help='Path or URL to video')
    video_parser.add_argument('prompt', help='Text prompt')

    args = parser.parse_args()

    if args.command == 'setenv':
        set_env(args.api_key, args.project_id, args.region_id)
    else:
        project_id, region_id = load_env()
        gemini = Gemini(project_id, region_id)

        if args.command == 'prompt':
            response = gemini.get_response(args.prompt)
            print(response)
        elif args.command == 'image':
            response = gemini.text_from_image(args.path_or_url, args.prompt)
            print(response)
        elif args.command == 'chat':
            response = gemini.text_from_chat(args.chat)
            print(response)
        elif args.command == 'video':
            response = gemini.text_from_video(args.path_or_url, args.prompt)
            print(response)

if __name__ == '__main__':
    test_gemini()
