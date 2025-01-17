import json
from playwright.sync_api import sync_playwright
import os
from tqdm import tqdm  # For progress bar
import time

# Load the JSON data
data = [
{
    "name": "dad-jokes",
    "path": "/components/dad-jokes",
    "url": "https://salmon-worm-461509.hostingersite.com/components/dad-jokes",
    "thumbnai": "/screenshots/dad-jokes"
  },
  {
    "name": "theme-clock",
    "path": "/components/theme-clock",
    "url": "https://salmon-worm-461509.hostingersite.com/components/theme-clock",
    "thumbnai": "/screenshots/theme-clock"
  },
  {
    "name": "sticky-navigation",
    "path": "/components/sticky-navigation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/sticky-navigation",
    "thumbnai": "/screenshots/sticky-navigation"
  },
  {
    "name": "random-choice-picker",
    "path": "/components/random-choice-picker",
    "url": "https://salmon-worm-461509.hostingersite.com/components/random-choice-picker",
    "thumbnai": "/screenshots/random-choice-picker"
  },
  {
    "name": "double-click-heart",
    "path": "/components/double-click-heart",
    "url": "https://salmon-worm-461509.hostingersite.com/components/double-click-heart",
    "thumbnai": "/screenshots/double-click-heart"
  },
  {
    "name": "live-user-filter",
    "path": "/components/live-user-filter",
    "url": "https://salmon-worm-461509.hostingersite.com/components/live-user-filter",
    "thumbnai": "/screenshots/live-user-filter"
  },
  {
    "name": "hidden-search",
    "path": "/components/hidden-search",
    "url": "https://salmon-worm-461509.hostingersite.com/components/hidden-search",
    "thumbnai": "/screenshots/hidden-search"
  },
  {
    "name": "faq-collapse",
    "path": "/components/faq-collapse",
    "url": "https://salmon-worm-461509.hostingersite.com/components/faq-collapse",
    "thumbnai": "/screenshots/faq-collapse"
  },
  {
    "name": "double-vertical-slider",
    "path": "/components/double-vertical-slider",
    "url": "https://salmon-worm-461509.hostingersite.com/components/double-vertical-slider",
    "thumbnai": "/screenshots/double-vertical-slider"
  },
  {
    "name": "incrementing-counter",
    "path": "/components/incrementing-counter",
    "url": "https://salmon-worm-461509.hostingersite.com/components/incrementing-counter",
    "thumbnai": "/screenshots/incrementing-counter"
  },
  {
    "name": "netflix-mobile-navigation",
    "path": "/components/netflix-mobile-navigation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/netflix-mobile-navigation",
    "thumbnai": "/screenshots/netflix-mobile-navigation"
  },
  {
    "name": "3d-boxes-background",
    "path": "/components/3d-boxes-background",
    "url": "https://salmon-worm-461509.hostingersite.com/components/3d-boxes-background",
    "thumbnai": "/screenshots/3d-boxes-background"
  },
  {
    "name": "feedback-ui-design",
    "path": "/components/feedback-ui-design",
    "url": "https://salmon-worm-461509.hostingersite.com/components/feedback-ui-design",
    "thumbnai": "/screenshots/feedback-ui-design"
  },
  {
    "name": "quiz-app",
    "path": "/components/quiz-app",
    "url": "https://salmon-worm-461509.hostingersite.com/components/quiz-app",
    "thumbnai": "/screenshots/quiz-app"
  },
  {
    "name": "toast-notification",
    "path": "/components/toast-notification",
    "url": "https://salmon-worm-461509.hostingersite.com/components/toast-notification",
    "thumbnai": "/screenshots/toast-notification"
  },
  {
    "name": "simple-timer",
    "path": "/components/simple-timer",
    "url": "https://salmon-worm-461509.hostingersite.com/components/simple-timer",
    "thumbnai": "/screenshots/simple-timer"
  },
  {
    "name": "notes-app",
    "path": "/components/notes-app",
    "url": "https://salmon-worm-461509.hostingersite.com/components/notes-app",
    "thumbnai": "/screenshots/notes-app"
  },
  {
    "name": "_project_starter_",
    "path": "/components/_project_starter_",
    "url": "https://salmon-worm-461509.hostingersite.com/components/_project_starter_",
    "thumbnai": "/screenshots/_project_starter_"
  },
  {
    "name": "button-ripple-effect",
    "path": "/components/button-ripple-effect",
    "url": "https://salmon-worm-461509.hostingersite.com/components/button-ripple-effect",
    "thumbnai": "/screenshots/button-ripple-effect"
  },
  {
    "name": "expanding-cards",
    "path": "/components/expanding-cards",
    "url": "https://salmon-worm-461509.hostingersite.com/components/expanding-cards",
    "thumbnai": "/screenshots/expanding-cards"
  },
  {
    "name": "animated-countdown",
    "path": "/components/animated-countdown",
    "url": "https://salmon-worm-461509.hostingersite.com/components/animated-countdown",
    "thumbnai": "/screenshots/animated-countdown"
  },
  {
    "name": "random-image-generator",
    "path": "/components/random-image-generator",
    "url": "https://salmon-worm-461509.hostingersite.com/components/random-image-generator",
    "thumbnai": "/screenshots/random-image-generator"
  },
  {
    "name": "pokedex",
    "path": "/components/pokedex",
    "url": "https://salmon-worm-461509.hostingersite.com/components/pokedex",
    "thumbnai": "/screenshots/pokedex"
  },
  {
    "name": "sound-board",
    "path": "/components/sound-board",
    "url": "https://salmon-worm-461509.hostingersite.com/components/sound-board",
    "thumbnai": "/screenshots/sound-board"
  },
  {
    "name": "animated-navigation",
    "path": "/components/animated-navigation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/animated-navigation",
    "thumbnai": "/screenshots/animated-navigation"
  },
  {
    "name": "auto-text-effect",
    "path": "/components/auto-text-effect",
    "url": "https://salmon-worm-461509.hostingersite.com/components/auto-text-effect",
    "thumbnai": "/screenshots/auto-text-effect"
  },
  {
    "name": "drag-n-drop",
    "path": "/components/drag-n-drop",
    "url": "https://salmon-worm-461509.hostingersite.com/components/drag-n-drop",
    "thumbnai": "/screenshots/drag-n-drop"
  },
  {
    "name": "custom-range-slider",
    "path": "/components/custom-range-slider",
    "url": "https://salmon-worm-461509.hostingersite.com/components/custom-range-slider",
    "thumbnai": "/screenshots/custom-range-slider"
  },
  {
    "name": "image-carousel",
    "path": "/components/image-carousel",
    "url": "https://salmon-worm-461509.hostingersite.com/components/image-carousel",
    "thumbnai": "/screenshots/image-carousel"
  },
  {
    "name": "password-generator",
    "path": "/components/password-generator",
    "url": "https://salmon-worm-461509.hostingersite.com/components/password-generator",
    "thumbnai": "/screenshots/password-generator"
  },
  {
    "name": "hoverboard",
    "path": "/components/hoverboard",
    "url": "https://salmon-worm-461509.hostingersite.com/components/hoverboard",
    "thumbnai": "/screenshots/hoverboard"
  },
  {
    "name": "kinetic-loader",
    "path": "/components/kinetic-loader",
    "url": "https://salmon-worm-461509.hostingersite.com/components/kinetic-loader",
    "thumbnai": "/screenshots/kinetic-loader"
  },
  {
    "name": "split-landing-page",
    "path": "/components/split-landing-page",
    "url": "https://salmon-worm-461509.hostingersite.com/components/split-landing-page",
    "thumbnai": "/screenshots/split-landing-page"
  },
  {
    "name": "background-slider",
    "path": "/components/background-slider",
    "url": "https://salmon-worm-461509.hostingersite.com/components/background-slider",
    "thumbnai": "/screenshots/background-slider"
  },
  {
    "name": "todo-list",
    "path": "/components/todo-list",
    "url": "https://salmon-worm-461509.hostingersite.com/components/todo-list",
    "thumbnai": "/screenshots/todo-list"
  },
  {
    "name": "content-placeholder",
    "path": "/components/content-placeholder",
    "url": "https://salmon-worm-461509.hostingersite.com/components/content-placeholder",
    "thumbnai": "/screenshots/content-placeholder"
  },
  {
    "name": "blurry-loading",
    "path": "/components/blurry-loading",
    "url": "https://salmon-worm-461509.hostingersite.com/components/blurry-loading",
    "thumbnai": "/screenshots/blurry-loading"
  },
  {
    "name": "mobile-tab-navigation",
    "path": "/components/mobile-tab-navigation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/mobile-tab-navigation",
    "thumbnai": "/screenshots/mobile-tab-navigation"
  },
  {
    "name": "form-input-wave",
    "path": "/components/form-input-wave",
    "url": "https://salmon-worm-461509.hostingersite.com/components/form-input-wave",
    "thumbnai": "/screenshots/form-input-wave"
  },
  {
    "name": "progress-steps",
    "path": "/components/progress-steps",
    "url": "https://salmon-worm-461509.hostingersite.com/components/progress-steps",
    "thumbnai": "/screenshots/progress-steps"
  },
  {
    "name": "good-cheap-fast",
    "path": "/components/good-cheap-fast",
    "url": "https://salmon-worm-461509.hostingersite.com/components/good-cheap-fast",
    "thumbnai": "/screenshots/good-cheap-fast"
  },
  {
    "name": "password-strength-background",
    "path": "/components/password-strength-background",
    "url": "https://salmon-worm-461509.hostingersite.com/components/password-strength-background",
    "thumbnai": "/screenshots/password-strength-background"
  },
  {
    "name": "rotating-nav-animation",
    "path": "/components/rotating-nav-animation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/rotating-nav-animation",
    "thumbnai": "/screenshots/rotating-nav-animation"
  },
  {
    "name": "drink-water",
    "path": "/components/drink-water",
    "url": "https://salmon-worm-461509.hostingersite.com/components/drink-water",
    "thumbnai": "/screenshots/drink-water"
  },
  {
    "name": "testimonial-box-switcher",
    "path": "/components/testimonial-box-switcher",
    "url": "https://salmon-worm-461509.hostingersite.com/components/testimonial-box-switcher",
    "thumbnai": "/screenshots/testimonial-box-switcher"
  },
  {
    "name": "event-keycodes",
    "path": "/components/event-keycodes",
    "url": "https://salmon-worm-461509.hostingersite.com/components/event-keycodes",
    "thumbnai": "/screenshots/event-keycodes"
  },
  {
    "name": "drawing-app",
    "path": "/components/drawing-app",
    "url": "https://salmon-worm-461509.hostingersite.com/components/drawing-app",
    "thumbnai": "/screenshots/drawing-app"
  },
  {
    "name": "scroll-animation",
    "path": "/components/scroll-animation",
    "url": "https://salmon-worm-461509.hostingersite.com/components/scroll-animation",
    "thumbnai": "/screenshots/scroll-animation"
  },
  {
    "name": "movie-app",
    "path": "/components/movie-app",
    "url": "https://salmon-worm-461509.hostingersite.com/components/movie-app",
    "thumbnai": "/screenshots/movie-app"
  },
  {
    "name": "github-profiles",
    "path": "/components/github-profiles",
    "url": "https://salmon-worm-461509.hostingersite.com/components/github-profiles",
    "thumbnai": "/screenshots/github-profiles"
  },
  {
    "name": "verify-account-ui",
    "path": "/components/verify-account-ui",
    "url": "https://salmon-worm-461509.hostingersite.com/components/verify-account-ui",
    "thumbnai": "/screenshots/verify-account-ui"
  },
  {
    "name": "insect-catch-game",
    "path": "/components/insect-catch-game",
    "url": "https://salmon-worm-461509.hostingersite.com/components/insect-catch-game",
    "thumbnai": "/screenshots/insect-catch-game"
  },
]

# Directory to save screenshots
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

# Function to take screenshots
def take_screenshots(data):
    # Initialize counters
    total_items = len(data)
    success_count = 0
    failed_count = 0
    failed_items = []

    # Start Playwright
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})  # Set desktop viewport size
        page = context.new_page()

        # Initialize progress bar
        with tqdm(total=total_items, desc="Processing", unit="page") as pbar:
            for item in data:
                name = item["name"]
                url = item["url"]
                screenshot_path = os.path.join(output_dir, f"{name}.png")

                try:
                    # Navigate to the URL
                    page.goto(url, timeout=60000)  # Increase timeout if needed
                    # Wait for the page to fully load
                    page.wait_for_load_state("networkidle")
                    time.sleep(1)  # Optional: Add a delay to ensure all content is loaded
                    # Take a screenshot of the viewport (100dvh x 100dvw)
                    page.screenshot(path=screenshot_path)
                    success_count += 1
                    pbar.set_postfix({"Status": "Success", "Failed": failed_count})
                except Exception as e:
                    failed_count += 1
                    failed_items.append({"name": name, "url": url, "error": str(e)})
                    pbar.set_postfix({"Status": "Failed", "Failed": failed_count})

                # Update progress bar
                pbar.update(1)
                time.sleep(1)  # Optional: Add a delay to avoid overwhelming the server

        # Close the browser
        context.close()
        browser.close()

    # Print summary
    print("\nScreenshot generation completed!")
    print(f"Total pages processed: {total_items}")
    print(f"Successfully processed: {success_count}")
    print(f"Failed to process: {failed_count}")

    # Save failed items to a log file
    if failed_items:
        with open("failed_items.log", "w") as log_file:
            json.dump(failed_items, log_file, indent=4)
        print("Failed items logged to 'failed_items.log'.")

# Run the function
take_screenshots(data)