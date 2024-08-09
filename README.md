<h1>pyWeather</h1>

pyWeather is a web application that provides current weather information for any city globally. Built with a modern and sleek design, the app offers a user-friendly interface to search for weather conditions and view detailed weather statistics. It fetches real-time weather data from the OpenWeatherMap API and displays it dynamically.

## Features

- **Search for Weather:** Enter any city name to get the current weather information.
- **Weather Details:** View comprehensive weather details including:
  - Current temperature
  - Feels like temperature
  - Minimum and maximum temperatures
  - Humidity percentage
  - Wind speed
  - Sunset time
- **Dynamic Images:** Weather conditions are visually represented with appropriate images (e.g., clear, clouds, rain).
- **Error Handling:** Displays an error banner if the city is not found or if there is an issue with the weather API.
- **Responsive Design:** The app is optimized for both desktop and mobile devices.

## Live Preview

You can preview the app online at: [pyWeather](https://pyweather-tgl0.onrender.com/)

## Technologies Used

- **Frontend:** 
  - HTML5
  - CSS3 (with animations and responsive design)
  - JavaScript (ES6)
- **Backend:** 
  - Flask (Python web framework)
  - Requests library (for API calls)
- **API:** 
  - OpenWeatherMap API (for fetching weather data)
- **Fonts & Icons:**
  - Google Fonts
  - Material Symbols Outlined

## How to Run the Application

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/pyWeather.git
   cd pyWeather
   ```
   
2. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```env
   API_KEY=your_openweathermap_api_key
   ```
   
3. **Run the Flask Server:**
   ```bash
   python app.py
   ```
   The server will start on http://0.0.0.0:5000.

4. **Open in Browser:**
   Navigate to http://localhost:5000 in your web browser to use the application.

## Project Structure
- `app.py`: Main Flask application script.
- `static/`: Contains static files such as CSS, JavaScript, and images.
- `templates/`: Contains HTML templates.
- `requirements.txt`: Python dependencies required for the project.
- `.env`: Environment variables for sensitive information.
