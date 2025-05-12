# Scrape Infinite Scroll: Quotes Web Scraper

This project involves web scraping quotes from an infinite scrolling page using Selenium. The target website is:

🔗 [https://quotes.toscrape.com/scroll](https://quotes.toscrape.com/scroll)

## 🎯 Objective
To extract **all quotes** from a webpage that loads more content as the user scrolls down, using Selenium's `execute_script()` method.

---

## 🔧 Tools Used
- **Python**
- **Selenium**
- **ChromeDriver** (or any browser driver)

---

## 🧠 Key Concepts
- **Infinite Scrolling**: New content is loaded dynamically as the user scrolls.
- **JavaScript Execution**: We simulate scrolling using:
  ```python
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
