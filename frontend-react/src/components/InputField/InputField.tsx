// InputField.tsx
import React, { useState } from 'react';
import './InputField.scss';

interface InputFieldProps {
  label: string;
  value: string;
  name: string;
  inputType: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const InputField: React.FC<InputFieldProps> = ({ label, value, onChange, inputType, name }) => {
  const [focused, setFocused] = useState(false);

  return (
    <div className={`input-field ${focused || value ? 'focused' : ''}`}>
      <label className="input-label">{label}</label>
      <input
        type={inputType}
        id={name}
        name={name}
        className="input-element"
        value={value}
        onChange={onChange}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
      />
    </div>
  );
};

export default InputField;
