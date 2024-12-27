import React, { useState } from 'react';
import "./StateDropdown.scss"
// List of US states
const states = [
  'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
  'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
  'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
  'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
  'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
  'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
  'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
];

interface StateDropdownProps {
  onStateChange: (state: string) => void;
}

const StateDropdown: React.FC<StateDropdownProps> = ({ onStateChange }) => {
  const [selectedState, setSelectedState] = useState("");
  const [isFocused, setIsFocused] = useState(false);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const newState = event.target.value;
    setSelectedState(newState);
    onStateChange(newState);
  };
  return (
    <div className={`state-dropdown ${isFocused || selectedState ? "focused" : ""}`}>
      <label htmlFor="state-select" className="dropdown-label">
        Select a State
      </label>
      <select
        id="state-select"
        className={`dropdown-element ${selectedState ? "dropdown-filled" : ""}`}
        value={selectedState}
        onChange={handleChange}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
      >
        <option value="" disabled>
          -- Select a state --
        </option>
        {states.map((state) => (
          <option key={state} value={state}>
            {state}
          </option>
        ))}
      </select>
    </div>
  );
};

export default StateDropdown;
