import React, { useState } from 'react';
import axios from 'axios';

const Weather = () => {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState('');
  const weatherApiUrl = process.env.REACT_APP_WEATHER_API_URL; // Fetch from .env

  const fetchWeather = async () => {
    if (!city) {
      setError('Please enter a city name.');
      return;
    }
    
    try {
      const response = await axios.get(`${weatherApiUrl}/${city}/`);
      setWeather(response.data);
      setError('');
    } catch (err) {
      setError('Failed to fetch weather data. Please check the city name.');
      setWeather(null);
    }
  };

  return (
    <div className="weather-container">
      <h2>Weather Information</h2>
      <input
        type="text"
        placeholder="Enter city name..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>

      {error && <p className="error">{error}</p>}

      {weather && (
        <div className="weather-info">
          <h3>{weather.city}</h3>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Humidity: {weather.humidity}%</p>
          <p>Condition: {weather.description}</p>
        </div>
      )}
    </div>
  );
};

export default Weather;
