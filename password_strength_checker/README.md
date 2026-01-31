# Password Strength Checker

A modern, interactive web application to check password strength with real-time feedback. Built with Python Flask, HTML, and CSS.

## Features

- **Real-time strength analysis** - Get instant feedback as you type
- **5-level strength classification**: Weak, Mid, Average, Strong, Very Strong
- **Visual strength meter** - Color-coded progress bar
- **Detailed feedback** - Actionable suggestions for improvement
- **Requirements checklist** - Visual indicators for met criteria
- **Password visibility toggle** - Show/hide password option
- **Responsive design** - Works on desktop and mobile devices

## Strength Levels

1. **Weak** - Basic password, needs more complexity
2. **Mid** - Slightly better, could use more variety
3. **Average** - Good foundation, add more character types
4. **Strong** - Solid password with good variety
5. **Very Strong** - Excellent security, well-balanced

## Requirements Checklist

- ✓ Minimum 8 characters
- ✓ Contains lowercase letters (a-z)
- ✓ Contains uppercase letters (A-Z)
- ✓ Contains numbers (0-9)
- ✓ Contains special characters (!@#$%^&*)

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps

1. **Install Flask**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Open in browser**
   - Navigate to `http://localhost:5000` in your web browser

## How It Works

### Backend (app.py)
- Python Flask server handles password strength analysis
- Uses regex patterns to check for character variety
- Detects common password patterns and penalizes them
- Returns detailed feedback and scoring

### Frontend
- Real-time password checking via JavaScript
- Visual indicators update as you type
- AJAX requests send passwords securely to backend
- Requirements checklist updates dynamically

## Password Analysis Criteria

The checker evaluates passwords based on:
- **Length**: 8, 12, and 16 character milestones
- **Character variety**: Lowercase, uppercase, numbers, special characters
- **Pattern detection**: Penalizes sequential patterns (123, abc, etc.)
- **Repetition**: Detects repeated characters
- **Overall complexity**: Scoring system 0-9

## Security Notes

- Passwords are NOT stored on the server
- Uses HTTPS-ready setup (configure in production)
- Only processes passwords for strength evaluation
- No data logging or tracking

## File Structure

```
password_strength_checker/
├── app.py                 # Flask application & password checking logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    └── style.css         # CSS styling
```

## Customization

### Modify Strength Thresholds
Edit the scoring logic in `check_password_strength()` function in `app.py`.

### Change Strength Levels
Adjust the conditions in the "Determine strength level" section to customize what qualifies as each level.

### Customize Requirements
Update the requirements list in `templates/index.html` and validation logic in `app.py`.

### Style Changes
Modify colors, fonts, and layout in `static/style.css`.

## Examples

### Weak Password: `pass`
- Too short
- Only lowercase letters

### Strong Password: `MyPassword@2024`
- 15 characters
- Mix of uppercase, lowercase, numbers, and special characters
- No repeated patterns

### Very Strong Password: `Tr0pic@lSunset#2024`
- 20 characters
- Excellent character variety
- Complex and unique

## Troubleshooting

**Port 5000 already in use?**
```bash
python app.py --port 5001
```

**Module not found error?**
```bash
pip install -r requirements.txt
```

**Styles not loading?**
- Clear browser cache (Ctrl+Shift+Del)
- Hard refresh (Ctrl+F5 or Cmd+Shift+R)

## Future Enhancements

- Password entropy calculation
- Dictionary word detection
- Breach database checking (Have I Been Pwned API)
- Password generation tool
- Multiple language support
- Dark mode theme

## License

Free to use and modify for personal or commercial projects.

## Contact & Support

For issues or suggestions, feel free to reach out!
