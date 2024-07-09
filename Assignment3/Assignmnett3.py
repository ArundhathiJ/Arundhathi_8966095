from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to YouTube
        driver.get("https://www.youtube.com")

        # Test 1: Search for a video
        search_video(driver, "Selenium WebDriver tutorial")

        # Test 2: Click on a video from search results
        click_video(driver)

        # Wait for 10 seconds before pausing
        time.sleep(10)

        # Test 3: Pause the video
        toggle_play_pause(driver)
        print("Paused the video")

        # Wait for 10 seconds
        time.sleep(10)

        # Test 4: Play the video
        toggle_play_pause(driver)
        print("Played the video")

        # Wait for 10 seconds
        time.sleep(10)

        # Test 5: Mute the video
        mute_video(driver)
        print("Muted the video")

        # Wait for 5 seconds
        time.sleep(10)

        # Test 6: Go back to the homepage
        go_back_home(driver)
        print("Navigated back to the YouTube homepage")

    finally:
        # Close the WebDriver
        driver.quit()


def search_video(driver, video_name):
    """Function to search for a video."""
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'search_query')))
    search_bar = driver.find_element(By.NAME, 'search_query')
    search_bar.send_keys(video_name)
    search_bar.send_keys(Keys.RETURN)
    print("Searched for video:", video_name)


def click_video(driver):
    """Function to click on a video from the search results."""
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]')))
    video_title = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    video_title.click()
    print("Clicked on the video")


def toggle_play_pause(driver):
    """Function to toggle play/pause the video."""
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-play-button')))
    play_pause_button = driver.find_element(By.CLASS_NAME, 'ytp-play-button')
    play_pause_button.click()  # This will toggle play/pause


def mute_video(driver):
    """Function to mute the video."""
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-mute-button')))
    mute_button = driver.find_element(By.CLASS_NAME, 'ytp-mute-button')
    if 'ytp-unmute' in mute_button.get_attribute('class'):
        mute_button.click()
        print("Muted the video")
    else:
        print("Video is already muted")


def go_back_home(driver):
    """Function to navigate back to the YouTube homepage."""
    driver.get("https://www.youtube.com")


if __name__ == "__main__":
    main()
