import React from "react";
import PropTypes from "prop-types";
import "./Select.scss";

export const Select = (props) => {
    const {
        name,
        value,
        onSelect,
        options,
        iconUrl,
    } = props;

    return (
        <>
            <select
                name={name}
                value={value}
                onChange={onSelect}
                className="select"
            >
                {options.map(({vlaue: optionValue, label}) => (
                    <option value={optionValue} selected={value === optionValue}>
                        {label}
                    </option>
                ))}
            </select>
            {!!iconUrl && (
                <img classname="select__icon" src={iconUrl} alt="select icon" />
            )}

            <img 
                className="select__arrow"
                src="./images/arrow-down.svg" 
                alt="arrow down" 
            />
        </>
    );
};

Select.propTypes = {
    name: PropTypes.string.isRequired,
    value: PropTypes.string.isRequired,
    onSelect: PropTypes.func.isRequired,
    options: PropTypes.arrayOf(PropTypes.shape({
        value: PropTypes.string,
        label: PropTypes.string,
    })),
    iconUrl: PropTypes.string,
};

Select.defaultProps = {
    options: [],
    iconUrl: "",
}


