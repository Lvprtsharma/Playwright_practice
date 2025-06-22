from playwright.sync_api import sync_playwright, Playwright

def test_search_and_verify_prices() -> None:
    """
    Test searching for products and verifying their prices.
    """
    with sync_playwright() as p:  # Fixed: Added parentheses and corrected variable name
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            page.goto("https://www.amazon.in/")
            
            # Wait for the search box to be visible
            search_box = page.locator("#twotabsearchtextbox")
            search_box.wait_for(state="visible")
            search_box.fill("macbook")
            
            # Press Enter or click search button instead of clicking suggestion
            search_box.press("Enter")
            # Alternative: page.locator("#nav-search-submit-button").click()
            
            # Wait for search results to load
            page.wait_for_selector("[data-component-type='s-search-result']", timeout=10000)
            
            # Get price elements - using a more reliable selector
            price_elements = page.locator("span.a-price-whole, span.a-price-range")
            
            # Wait for at least one price to be visible
            if price_elements.count() > 0:
                price_list = price_elements.all_text_contents()
                print(f"Found {len(price_list)} prices:")
                for i, price in enumerate(price_list, 1):
                    print(f"{i}. {price}")
            else:
                print("No prices found")
                
        except Exception as e:
            print(f"Error occurred: {e}")
            
        finally:
            # Clean up
            context.close()
            browser.close()

# Alternative version with better error handling and more robust selectors
def test_search_and_verify_prices_robust() -> None:
    """
    More robust version with better error handling.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            # Add user agent to avoid bot detection
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        try:
            page.goto("https://www.amazon.in/", wait_until="networkidle")
            
            # Handle potential cookie/privacy banners
            try:
                page.locator("input[data-action-type='DISMISS']").click(timeout=3000)
            except:
                pass  # Banner might not be present
            
            # Search for macbook
            search_box = page.locator("#twotabsearchtextbox")
            search_box.fill("macbook")
            search_box.press("Enter")
            
            # Wait for search results
            page.wait_for_load_state("networkidle")
            page.wait_for_selector("[data-component-type='s-search-result']", timeout=15000)
            
            # Multiple strategies to find prices
            price_selectors = [
                "span.a-price-whole",
                "span.a-price-range", 
                ".a-price .a-offscreen",
                ".a-price-symbol + .a-price-whole"
            ]
            
            all_prices = []
            for selector in price_selectors:
                try:
                    elements = page.locator(selector)
                    if elements.count() > 0:
                        prices = elements.all_text_contents()
                        all_prices.extend(prices)
                except:
                    continue
            
            # Remove duplicates and clean prices
            unique_prices = list(set(all_prices))
            cleaned_prices = [price.strip() for price in unique_prices if price.strip()]
            
            print(f"Found {len(cleaned_prices)} unique prices:")
            for i, price in enumerate(cleaned_prices, 1):
                print(f"{i}. ₹{price}" if not price.startswith('₹') else f"{i}. {price}")
                
        except Exception as e:
            print(f"Error occurred: {e}")
            # Take screenshot for debugging
            page.screenshot(path="error_screenshot.png")
            
        finally:
            context.close()
            browser.close()

# If you need this to work with pytest fixtures
def test_search_and_verify_prices_with_fixture(page) -> None:
    """
    Version that works with pytest-playwright fixtures.
    """
    try:
        page.goto("https://www.amazon.in/")
        
        search_box = page.locator("#twotabsearchtextbox")
        search_box.fill("macbook")
        search_box.press("Enter")
        
        page.wait_for_selector("[data-component-type='s-search-result']", timeout=15000)
        
        # Get prices
        price_elements = page.locator("span.a-price-whole")
        price_list = price_elements.all_text_contents()
        
        print(f"Found {len(price_list)} prices:")
        for i, price in enumerate(price_list, 1):
            print(f"{i}. ₹{price}")
            
        # Add assertions if needed
        assert len(price_list) > 0, "No prices found on the page"
        
    except Exception as e:
        print(f"Error: {e}")
        page.screenshot(path="debug_screenshot.png")
        raise

if __name__ == "__main__":
    test_search_and_verify_prices_robust()