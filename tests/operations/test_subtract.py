from calculator import subtract


def test_subtract():
    """Subtracting two positive integers returns their difference."""
    result = subtract(5, 3)
    assert result == 2