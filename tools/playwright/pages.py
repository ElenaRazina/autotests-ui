import allure
from playwright.sync_api import Playwright, Page
from allure_commons.types import AttachmentType
from config import settings


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Page:
    """
    Initialize Playwright page with proper error handling and video attachment.
    
    Args:
        playwright: Playwright instance
        test_name: Name of the test for trace file
        storage_state: Path to browser state file or None
    
    Yields:
        Page: Playwright page instance
    """
    browser = playwright.chromium.launch(headless=settings.headless)
    
    # Use storage_state parameter properly
    context = browser.new_context(
        storage_state=storage_state, 
        record_video_dir=settings.videos_dir
    )
    
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    # Store video path before yielding to avoid errors
    video_path = None
    
    try:
        yield page
    finally:
        # Stop tracing and close browser safely
        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
        
        # Get video path safely before closing browser
        try:
            video_path = page.video.path()
        except Exception:
            video_path = None
        
        browser.close()
        
        # Attach trace file
        try:
            allure.attach.file(
                settings.tracing_dir.joinpath(f'{test_name}.zip'),
                name='trace',
                extension='zip'
            )
        except Exception:
            pass  # Ignore attachment errors
        
        # Attach video file if available
        if video_path:
            try:
                allure.attach.file(
                    video_path,
                    name='video',
                    attachment_type=AttachmentType.WEBM
                )
            except Exception:
                pass  # Ignore attachment errors
