import vertexai
from vertexai.generative_models import GenerativeModel, Image, Part
import google.auth
from google.auth.exceptions import DefaultCredentialsError

class Gemini:
    def __init__(self, project_id: str, region: str):
        vertexai.init(project=project_id, location=region)
        self.model = GenerativeModel('gemini-1.5-pro')
        self._initialize_vertex_ai()

    def _initialize_vertex_ai(self):
        try:
            _, project = google.auth.default()
            if project is None:
                raise DefaultCredentialsError("No Google Cloud project ID found. Please set up your credentials.")
            vertexai.init(project=self.project_id, location=self.region)
            self.model = GenerativeModel('gemini-1.5-flash')
        except DefaultCredentialsError as e:
            print(f"Error initializing Vertex AI: {e}")
            raise

    def get_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    def text_from_image(self, path_or_url: str, prompt: str) -> str:
        if path_or_url.startswith('http'):
            image = Image.load_from_url(path_or_url)
        else:
            image = Image.load_from_file(path_or_url)
        response = self.model.generate_content([prompt, image])
        return response.text

    def text_from_chat(self, chat: str) -> str:
        chat_session = self.model.start_chat()
        response = chat_session.send_message(chat)
        return response.text

    def text_from_video(self, path_or_url: str, prompt: str) -> str:
        if path_or_url.startswith('http'):
            video_file = Part.from_url(path_or_url, mime_type="video/mp4")
        else:
            video_file = Part.from_uri(path_or_url, mime_type="video/mp4")
        contents = [video_file, prompt]
        response = self.model.generate_content(contents)
        return response.text
