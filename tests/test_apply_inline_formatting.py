import pytest
from formatter import apply_inline_formatting

def test_apply_inline_formatting():
    # bold
    assert apply_inline_formatting("This is **bold** text") == "This is <strong>bold</strong> text"
    assert apply_inline_formatting("This is __bold__ text") == "This is <strong>bold</strong> text"

    # italic
    assert apply_inline_formatting("This is *italic* text") == "This is <em>italic</em> text"
    assert apply_inline_formatting("This is _italic_ text") == "This is <em>italic</em> text"

    # bold italic
    assert apply_inline_formatting("This is ***bold+italic*** text") == "This is <strong><em>bold+italic</em></strong> text"
    assert apply_inline_formatting("This is ___bold+italic___ text") == "This is <strong><em>bold+italic</em></strong> text"

    # strike
    assert apply_inline_formatting("This is ~~strike~~ text") == "This is <del>strike</del> text"

    # escaped characters
    assert apply_inline_formatting(r"This is \*not italic\* text") == "This is *not italic* text"
    assert apply_inline_formatting(r"This is \_not italic\_ text") == "This is _not italic_ text"
    assert apply_inline_formatting(r"This is \**not bold\** text") == "This is **not bold** text"
    assert apply_inline_formatting(r"This is \_\_not bold\_\_ text") == "This is __not bold__ text"

    # combined
    text = r"This is ***bold+italic***, **bold**, *italic*, ~~strike~~, and \*not italic\*."
    expected = "This is <strong><em>bold+italic</em></strong>, <strong>bold</strong>, <em>italic</em>, <del>strike</del>, and *not italic*."
    assert apply_inline_formatting(text) == expected

    # links
    assert apply_inline_formatting('[Google](https://google.com)') == '<a href="https://google.com">Google</a>'
    assert apply_inline_formatting('[OpenAI](https://openai.com "AI Research")') == '<a href="https://openai.com" title="AI Research">OpenAI</a>'
