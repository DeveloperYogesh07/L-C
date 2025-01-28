import requests
import json
import time


class BlogInfo:
    def __init__(self, blog_url):
        self.blog_url = blog_url
        self.blog_title = None
        self.blog_name = None
        self.blog_description = None
        self.total_posts = None

    def fetch_blog_info(self):
        api_url = f"https://{self.blog_url}.tumblr.com/api/read/json"
        response = self._make_request(
            api_url, params={"num": 1}
        )  # Fetch one post to retrieve blog details
        if response:
            response_data = self._parse_response(response.text)
            if response_data:
                self._extract_info(response_data)

    def _make_request(self, api_url, params):
        for attempt in range(5):
            try:
                response = requests.get(api_url, params=params)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException:
                if attempt == 4:
                    raise
                continue

    def _parse_response(self, response_text):
        if response_text.strip():
            try:
                json_data = response_text[response_text.find("{") : -2]
                return json.loads(json_data)
            except ValueError as e:
                print(f"Error parsing JSON: {e}")
        else:
            print("Empty response received from the server.")
        return None

    def _extract_info(self, json_data):
        blog_details = json_data.get("tumblelog", {})
        self.blog_title = blog_details.get("title", "No Title")
        self.blog_name = blog_details.get("name", "No Name")
        self.blog_description = blog_details.get("description", "No Description")
        self.total_posts = json_data.get("posts-total", 0)

    def display_blog_info(self):
        print(f"Blog Title: {self.blog_title}")
        print(f"Blog Name: {self.blog_name}")
        print(f"Description: {self.blog_description}")
        print(f"Total Posts: {self.total_posts}")


class ImageExtractor:
    def __init__(self, blog_url):
        self.blog_url = blog_url

    def build_image_url(self, photo_data, resolution="1280"):
        """Build and return the image URL for a specific resolution."""
        if f"photo-url-{resolution}" in photo_data:
            key = f"photo-url-{resolution}"
        return photo_data.get(key)

    def extract_images_from_post(self, post_data, post_id):
        image_list = []
        if "photos" in post_data:
            for photo in post_data["photos"]:
                image_url = self.build_image_url(photo)
                if image_url:
                    image_list.append((post_id, image_url))
        return image_list

    def fetch_images_in_range(self, start_post, end_post):
        images_collected = []
        for post_id in range(start_post, end_post + 1):
            api_start_index = post_id - 1
            api_url = f"https://{self.blog_url}.tumblr.com/api/read/json"
            response = self._make_request(
                api_url, params={"num": 1, "start": api_start_index}
            )
            print(f"Fetching post {post_id}")

            if response:
                response_data = self._parse_response(response.text)
                if response_data:
                    posts = response_data.get("posts", [])
                    if not posts:
                        print(f"No posts found at post {post_id}.")
                    for post in posts:
                        images = self.extract_images_from_post(post, post_id)
                        if images:
                            images_collected.extend(images)
                        else:
                            print(f"No images found in post {post_id}.")
        return images_collected

    def _make_request(self, api_url, params):
        for attempt in range(5):
            try:
                response = requests.get(api_url, params=params)
                response.raise_for_status()
                return response
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:  # Handle rate limit
                    retry_after = int(response.headers.get("Retry-After", 1))
                    print(
                        f"Rate limit reached. Retrying after {retry_after} seconds..."
                    )
                    time.sleep(retry_after)
                else:
                    print(f"HTTP Error: {e}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                break
        return None

    def _parse_response(self, response_text):
        if response_text.strip():
            try:
                json_data = response_text[response_text.find("{") : -2]
                return json.loads(json_data)
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("Empty response received from the server.")
        return None


class TumblrClient:
    def __init__(self, blog_url):
        self.blog_info = BlogInfo(blog_url)
        self.image_extractor = ImageExtractor(blog_url)

    def fetch_and_display_blog_info(self):
        self.blog_info.fetch_blog_info()
        self.blog_info.display_blog_info()

    def fetch_and_display_images(self, start, end):
        images = self.image_extractor.fetch_images_in_range(start, end)
        self._print_images(images)

    def _print_images(self, images):
        if images:
            for post_id, img_url in images:
                print(f"{post_id}. {img_url}")
        else:
            print("No images found in the specified range.")

    def validate_post_range(self, input_range):
        try:
            start_post, end_post = map(int, input_range.split("-"))
            if start_post < 1 or end_post < start_post:
                raise ValueError("Invalid post range.")
            return start_post, end_post
        except ValueError as e:
            print(f"Range validation error: {e}")
            return None, None


def main():
    blog_url = input("Enter the Tumblr blog name: ").strip()
    post_range = input("Enter the range (start-end): ").strip()

    tumblr_client = TumblrClient(blog_url)

    start, end = tumblr_client.validate_post_range(post_range)
    if start is None or end is None:
        return

    tumblr_client.fetch_and_display_blog_info()
    tumblr_client.fetch_and_display_images(start, end)


if __name__ == "__main__":
    main()
