import re
def remove_html_tags(text):
    """Remove HTML tags from a string."""
    import re
    clean = re.compile(r'<[^>]+>')  # Matches HTML tags
    return re.sub(clean, '', text)

def number_to_words(n):
    """Convert a number to its English word representation."""
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    if 0 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + ('-' + ones[n % 10] if n % 10 != 0 else '')
    elif 100 <= n < 1000:
        return ones[n // 100] + ' hundred' + (' and ' + number_to_words(n % 100) if n % 100 != 0 else '')
    elif 1000 <= n < 10000:
        return ones[n // 1000] + ' thousand' + (' ' + number_to_words(n % 1000) if n % 1000 != 0 else '')
    elif n >= 10000:
        return number_to_words(n // 1000) + ' thousand' + (' ' + number_to_words(n % 1000) if n % 1000 != 0 else '')

def convert_year_range_to_words(match):
    """Convert a year range or number to words."""
    matched_text = match.group()
    
    # Check if the match is a year range (e.g., 1955-2000)
    if '-' in matched_text:
        start, end = matched_text.split('-')
        start_words = number_to_words(int(start))
        end_words = number_to_words(int(end))
        return f"{start_words} to {end_words}"
    else:
        # Standalone number
        return number_to_words(int(matched_text))

# Example string
