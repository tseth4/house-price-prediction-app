import React, { useState } from "react";
import "./HomePrice.scss"
const HomePricePredictionForm: React.FC = () => {
  const [formData, setFormData] = useState({
    bed: "",
    bath: "",
    acre_lot: "",
    house_size: "",
    state: "",
    zip_code: "",
  });
  const [prediction, setPrediction] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setPrediction(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      console.log("data.prediction: ", data)
      setPrediction(`Predicted Price: ${data.prediction}`);
    } catch (err: any) {
      setError(`Failed to fetch prediction: ${err.message}`);
    }
  };

  return (
    <div className="home-price-container">
      <h1>Home Price Prediction</h1>
      <form className="home-price-container__form" onSubmit={handleSubmit}>
        <label htmlFor="bed">Number of Bedrooms:</label>
        <input
          type="number"
          id="bed"
          name="bed"
          value={formData.bed}
          onChange={handleChange}
          required
          placeholder="e.g., 3"
        />

        <label htmlFor="bath">Number of Bathrooms:</label>
        <input
          type="number"
          id="bath"
          name="bath"
          value={formData.bath}
          onChange={handleChange}
          required
          placeholder="e.g., 2.5"
        />

        <label htmlFor="acre_lot">Lot Size (in acres):</label>
        <input
          type="number"
          id="acre_lot"
          name="acre_lot"
          value={formData.acre_lot}
          onChange={handleChange}
          required
          placeholder="e.g., 0.15"
        />

        <label htmlFor="house_size">House Size (in square feet):</label>
        <input
          type="number"
          id="house_size"
          name="house_size"
          value={formData.house_size}
          onChange={handleChange}
          required
          placeholder="e.g., 1500"
        />

        <label htmlFor="state">State:</label>
        <input
          type="text"
          id="state"
          name="state"
          value={formData.state}
          onChange={handleChange}
          required
          placeholder="e.g., California"
        />

        <label htmlFor="zip_code">Zip Code:</label>
        <input
          type="number"
          id="zip_code"
          name="zip_code"
          value={formData.zip_code}
          onChange={handleChange}
          required
          placeholder="e.g., 90210"
        />

        <button type="submit">Predict Price</button>
      </form>
      {prediction && <p>{prediction}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default HomePricePredictionForm;
