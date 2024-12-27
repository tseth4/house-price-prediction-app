import React, { useState, useEffect } from "react";
import Input from "@/components/InputField/InputField";
import StateDropdown from "../StateDropdown/StateDropdown";
import Button from "@/components/Button/Button";
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

  const areAllFieldsFilled = Object.values(formData).every((value) => value.trim() !== "");


  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleStateChange = (selectedState: string) => {
    setFormData((prevData) => ({ ...prevData, state: selectedState }));
  };

  useEffect(() => {
    console.log("formData: ", formData)
  }, [formData])

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
      setPrediction(`${data.prediction}`);
    } catch (err: any) {
      setError(`Failed to fetch prediction: ${err.message}`);
    }
  };

  return (
    <div className="home-price-container">
      <h1>Home Price Prediction</h1>
      <form className="home-price-container__form" onSubmit={handleSubmit}>
        <Input inputType="number" name="bed" label="Bedrooms" value={formData.bed} onChange={handleChange} />
        <Input inputType="number" name="bath" label="Bath" value={formData.bath} onChange={handleChange} />
        <Input inputType="number" name="acre_lot" label="Acre lot (eg.0.15)" value={formData.acre_lot} onChange={handleChange} />
        <Input inputType="number" name="house_size" label="House size (eg. 1500)" value={formData.house_size} onChange={handleChange} />
        <StateDropdown
          onStateChange={handleStateChange}
        />
        <Input inputType="number" name="zip_code" label="Zipcode" value={formData.zip_code} onChange={handleChange} />
        <Button label="Predict Price" onClick={() => { }} disabled={!areAllFieldsFilled} />

      </form>
      <div className="home-price-container-results">
        {prediction && (
          <div className="prediction-container">
            <b>prediction: </b>
            <div></div>
            <p className="prediction-value">$ {prediction}</p>
          </div>
        )}
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    </div>
  );
};

export default HomePricePredictionForm;
