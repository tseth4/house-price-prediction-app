import React from "react";
import "./Button.scss";

interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

const Button: React.FC<ButtonProps> = ({ label, onClick, disabled = false }) => {
  return (
    <button
      className={`button ${disabled ? "disabled" : ""}`}
      onClick={onClick}
      disabled={disabled}
      data-label={label}
    >
      {label}
    </button>
  );
};

export default Button;
